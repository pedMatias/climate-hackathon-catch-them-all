from config import AVAILABLE_PERSONAS

def get_persona_options():
    """Return persona options for selectbox"""
    return list(AVAILABLE_PERSONAS.keys())

def get_persona_data(persona_key: str):
    """Get detailed persona data"""
    return AVAILABLE_PERSONAS.get(persona_key)

def display_persona_info(persona_key: str):
    """Display persona information in Streamlit"""
    persona = get_persona_data(persona_key)
    if persona:
        return f"""
        **{persona['name']}**
        
        {persona['description']}
        
        **Primary Concerns:**
        - {' '.join(persona['primary_concerns'])}
        
        **Language Level:** {persona['language_level']}
        """
    return "Persona not found"