import streamlit as st
from typing import Dict, Any
import json
from datetime import datetime, timedelta
from config import CACHE_TTL

def init_session_state():
    """Initialize session state variables"""
    if 'generated_content' not in st.session_state:
        st.session_state.generated_content = None
    if 'processing' not in st.session_state:
        st.session_state.processing = False
    if 'error' not in st.session_state:
        st.session_state.error = None

def cache_result(key: str, content: Dict[str, Any]):
    """Cache the generated content with timestamp"""
    st.session_state[f"cache_{key}"] = {
        "content": content,
        "timestamp": datetime.now()
    }

def get_cached_result(key: str) -> Dict[str, Any]:
    """Retrieve cached content if still valid"""
    cache_key = f"cache_{key}"
    if cache_key in st.session_state:
        cached = st.session_state[cache_key]
        if datetime.now() - cached["timestamp"] < timedelta(seconds=CACHE_TTL):
            return cached["content"]
    return None

def display_error(error: str):
    """Display error message in Streamlit"""
    st.error(f"Error: {error}")

def create_cache_key(message: str, persona: str) -> str:
    """Create a unique cache key for the message-persona combination"""
    return f"{message}_{persona}".replace(" ", "_")[:50]