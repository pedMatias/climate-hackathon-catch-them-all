# Simplified Climate Communications Tool - Technical Specification

## 1. Technical Stack

### Backend
- **Python 3.11+**
- **Key Libraries:**
  - FastAPI for API endpoints
  - Anthropic SDK for Claude 3.5 Sonnet integration
  - Pydantic for data validation
  - SQLite for lightweight storage
- **Chain of Thought Implementation:**
  ```python
  class ClimateMessageProcessor:
      def __init__(self):
          self.client = anthropic.Client(api_key="your-key")
          
      async def process_message(self, message: str, persona: str):
          # Step 1: Analyze message context
          context_prompt = self._build_context_prompt(message, persona)
          context_analysis = await self._get_claude_response(context_prompt)
          
          # Step 2: Generate tone and keywords
          tone_prompt = self._build_tone_prompt(context_analysis, persona)
          tone_keywords = await self._get_claude_response(tone_prompt)
          
          # Step 3: Generate article and feedback
          article_prompt = self._build_article_prompt(
              message, persona, tone_keywords
          )
          final_content = await self._get_claude_response(article_prompt)
          
          return self._parse_response(final_content)
```

### Frontend Option 1: Streamlit
```python
import streamlit as st

def main():
    st.title("Climate Communications Tool")
    
    # Step 1: Message Input
    message = st.text_area("Enter your climate message:")
    
    # Step 2: Persona Selection
    personas = ["Portuguese Agricultural Farmers", "Urban Residents", 
                "Small Business Owners", "Students"]
    selected_persona = st.selectbox("Select target audience:", personas)
    
    if st.button("Generate Content"):
        with st.spinner("Generating..."):
            results = process_message(message, selected_persona)
            
        # Display results in tabs
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Tone", "Keywords", "Feedback", "News", "Article"
        ])
        with tab1:
            st.write(results["tone"])
        # ... similar for other tabs
```

### Frontend Option 2: FastUI
```python
from fastui import FastUI, components as c

def create_app():
    app = FastUI()
    
    @app.page("/")
    async def home():
        return [
            c.Heading("Climate Communications Tool"),
            c.TextArea("message", label="Enter your climate message"),
            c.Select(
                "persona",
                options=["Portuguese Agricultural Farmers", "Urban Residents"],
                label="Select target audience"
            ),
            c.Button("Generate", on_click="generate_content")
        ]
    
    return app
```

## 2. Core Data Models
```python
from pydantic import BaseModel
from typing import List

class MessageInput(BaseModel):
    content: str
    selected_personas: List[str]

class GeneratedContent(BaseModel):
    tone: str
    keywords: List[str]
    feedback: str
    related_news: List[str]
    article: str
```

## 3. Claude Prompts Structure

### Context Analysis Prompt
```python
def _build_context_prompt(message: str, persona: str) -> str:
    return f"""As a climate communications expert, analyze this message:
    Message: {message}
    Target Audience: {persona}
    
    Think step by step:
    1. What are the key environmental themes?
    2. How does this relate to the target audience?
    3. What are potential sensitivities?
    
    Provide analysis in JSON format."""
```

### Tone and Keywords Prompt
```python
def _build_tone_prompt(context: str, persona: str) -> str:
    return f"""Based on this context and persona:
    Context: {context}
    Persona: {persona}
    
    Generate:
    1. Appropriate tone for communication
    2. Key phrases and words that resonate
    3. Language level adjustments needed
    
    Provide response in JSON format."""
```

## 4. Implementation Timeline (4 weeks)

### Week 1
- Set up Python backend with FastAPI
- Implement Claude integration
- Create basic prompt templates

### Week 2
- Implement core message processing logic
- Set up Streamlit/FastUI frontend
- Basic UI flow implementation

### Week 3
- Integrate frontend and backend
- Implement persona definitions
- Add basic error handling

### Week 4
- Testing and refinement
- Performance optimization
- Documentation

## 5. Deployment
- Deploy on lightweight cloud service (e.g., DigitalOcean, Heroku)
- Use Docker for containerization
- Simple SQLite database for storage
- Environment variables for API keys

## 6. MVP Features
1. Single-page interface
2. Support for 8 basic personas
3. Chain of thought processing using Claude
4. Basic error handling
5. Simple content generation
6. Session-based storage

## 7. Future Optimizations
1. Caching frequently used responses
2. Batch processing for multiple personas
3. Export functionality
4. Basic analytics
5. User feedback collection