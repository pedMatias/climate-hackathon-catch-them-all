import streamlit as st
import logging
from config import (
    APP_TITLE,
    APP_SUBTITLE,
    THEME_COLOR,
    SECONDARY_COLOR,
    BACKGROUND_COLOR,
)
from models import MessageInput, ProcessingError
from claude_service import ClaudeService
from utils import (
    init_session_state,
    cache_result,
    get_cached_result,
    display_error,
    create_cache_key,
)
from personas import get_persona_options, get_persona_data, display_persona_info

# Initialize services
claude_service = ClaudeService()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def set_page_style():
    """Set custom page styling"""
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }}
        .header-container {{
            background: linear-gradient(135deg, {THEME_COLOR}, {SECONDARY_COLOR});
            padding: 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            text-align: center;
        }}
        .header-container h1 {{
            color: white;
            margin-bottom: 0.5rem;
        }}
        .header-container p {{
            color: rgba(255,255,255,0.9);
        }}
        .summary-header {{
            background: white;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .section-title {{
            background: white;
            padding: 1rem;
            border-radius: 10px;
            margin: 2rem 0 1rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .persona-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            padding: 1rem 0;
        }}
        .persona-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            cursor: pointer;
            transition: transform 0.2s;
        }}
        .persona-card:hover {{
            transform: translateY(-5px);
        }}
        .persona-card.selected {{
            border: 2px solid {THEME_COLOR};
        }}
        .result-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .nav-button {{
            background: white;
            color: {THEME_COLOR};
            border: 2px solid {THEME_COLOR};
            padding: 0.5rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .nav-button:hover {{
            background: {THEME_COLOR};
            color: white;
        }}
        </style>
    """,
        unsafe_allow_html=True,
    )


def init_session_vars():
    """Initialize session state variables"""
    if "page" not in st.session_state:
        st.session_state.page = "main"
    if "message" not in st.session_state:
        st.session_state.message = ""
    if "selected_persona" not in st.session_state:
        st.session_state.selected_persona = None
    if "selected_country" not in st.session_state:
        st.session_state.selected_country = None
    if "processing" not in st.session_state:
        st.session_state.processing = False
    if "generated_content" not in st.session_state:
        st.session_state.generated_content = None
    if "error" not in st.session_state:
        st.session_state.error = None


def render_main_page():
    """Render main page with welcome message and input"""
    st.markdown(
        """
        <div class="header-container">
            <h1>🌍 Climate Communications Tool</h1>
            <p>Create impactful climate messages tailored to your audience</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Step 1: Country selection
    st.markdown(
        """
        <div class="section-title">
            <h2>🌎 Select Target Country</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    country = st.selectbox(
        "Choose the country of your target audience:",
        ["France", "UK", "Spain", "Poland"],
        key="country",
    )
    st.session_state.selected_country = country

    st.markdown(
        """
        <div class="section-title">
            <h2>📝 Compose Your Message</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    message = st.text_area(
        "What do you want to write today:",
        value=st.session_state.message,
        height=150,
        placeholder="Share your topic here...",
        help="Write the message you want to communicate about (max 500 characters)",
        max_chars=500,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Next →", use_container_width=True, type="primary"):
            if not message:
                st.error("Please enter your climate message")
            else:
                st.session_state.message = message
                st.session_state.page = "persona"
                st.rerun()


def render_persona_page():
    """Render persona selection page"""
    # Back button
    if st.button("← Back to Message", type="secondary"):
        st.session_state.page = "main"
        st.rerun()

    st.markdown(
        """
        <div class="section-title">
            <h2>👥 Choose Your Target Audience</h2>
        </div>
        <p>Select the audience you want to reach with your message</p>
    """,
        unsafe_allow_html=True,
    )

    st.write(f"**Selected Country:** {st.session_state.selected_country}")

    personas = get_persona_options()
    cols = st.columns(4)
    for i, persona_key in enumerate(personas):
        persona_data = get_persona_data(persona_key)
        with cols[i % 4]:
            if st.button(
                f"{persona_data['icon']}\n\n{persona_data['name']}",
                key=f"persona_{persona_key}",
                help=persona_data["description"],
                use_container_width=True,
                type=(
                    "secondary"
                    if persona_key != st.session_state.selected_persona
                    else "primary"
                ),
            ):
                st.session_state.selected_persona = persona_key

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(
            "Generate Content →",
            use_container_width=True,
            type="primary",
            disabled=not st.session_state.selected_persona,
        ):
            try:
                st.session_state.processing = True
                cache_key = create_cache_key(
                    st.session_state.message, st.session_state.selected_persona
                )
                cached_result = get_cached_result(cache_key)

                if cached_result:
                    st.session_state.generated_content = cached_result
                else:
                    with st.spinner("✨ Crafting your personalized content..."):
                        content = generate_content(
                            st.session_state.message,
                            st.session_state.selected_persona,
                            st.session_state.selected_country,
                        )
                        st.session_state.generated_content = content
                        cache_result(cache_key, content)

                st.session_state.page = "results"
                st.rerun()
            except Exception as e:
                st.error(f"Error generating content: {str(e)}")
            finally:
                st.session_state.processing = False


def render_results_page():
    """Render results page"""
    # Back to main menu button
    if st.button("← Main Menu", type="secondary"):
        st.session_state.page = "main"
        st.session_state.message = ""
        st.session_state.selected_persona = None
        st.session_state.generated_content = None
        st.rerun()

    # Summary header
    persona_data = get_persona_data(st.session_state.selected_persona)
    st.markdown(
        f"""
        <div class="summary-header">
            <small>Message: "{st.session_state.message}"</small><br>
            <small>Audience: {persona_data['icon']} {persona_data['name']}</small>
        </div>
    """,
        unsafe_allow_html=True,
    )

    content = st.session_state.generated_content

    # Tone Card
    st.markdown(
        """
        <div class="result-card">
            <h3>💭 Recommended Tone</h3>
    """,
        unsafe_allow_html=True,
    )
    st.write(content.tone)
    st.markdown("</div>", unsafe_allow_html=True)

    # Keywords and Feedback in columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="result-card">
                <h3>🎯 Key Keywords</h3>
        """,
            unsafe_allow_html=True,
        )
        for keyword in content.keywords:
            st.markdown(f"- {keyword}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="result-card">
                <h3>💡 Message Feedback</h3>
        """,
            unsafe_allow_html=True,
        )
        st.write(content.feedback)
        st.markdown("</div>", unsafe_allow_html=True)

    # Related News
    st.markdown(
        """
        <div class="result-card">
            <h3>📰 Related News Types</h3>
    """,
        unsafe_allow_html=True,
    )
    for news in content.related_news:
        st.markdown(f"- {news}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Article with markdown support
    st.markdown(
        """
        <div class="result-card">
            <h3>📝 Generated Article</h3>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(content.article)
    st.markdown("</div>", unsafe_allow_html=True)


def generate_content(message: str, persona_key: str, country: str):
    """Generate content using Claude service"""
    try:
        persona_data = get_persona_data(persona_key)
        if not persona_data:
            raise ValueError("Invalid persona selected")

        message_input = MessageInput(content=message, selected_personas=[persona_key], country=country)

        return claude_service.generate_content(message_input, persona_data)
    except Exception as e:
        logging.error(f"Error generating content: {e}")
        raise ProcessingError(error_type="generation_error", message=str(e))


def main():
    # Initialize session state and styling
    init_session_state()
    init_session_vars()
    set_page_style()

    # Render appropriate page based on state
    if st.session_state.page == "main":
        render_main_page()
    elif st.session_state.page == "persona":
        render_persona_page()
    elif st.session_state.page == "results":
        render_results_page()


if __name__ == "__main__":
    main()
