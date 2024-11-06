import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
if not CLAUDE_API_KEY:
    raise ValueError("CLAUDE_API_KEY must be set in environment variables")

# App Configuration
APP_TITLE = "Climate Communications Tool"
APP_SUBTITLE = "Craft targeted climate messages for different audiences"

# Personas Configuration
AVAILABLE_PERSONAS = {
    "pt_farmer": {
        "name": "Portuguese Agricultural Farmer",
        "description": "Traditional farmers focused on sustainable practices and cost efficiency",
        "characteristics": [
            "practical_mindset",
            "cost_sensitive",
            "traditional_values",
        ],
        "language_level": "simple",
        "primary_concerns": ["water_scarcity", "energy_costs", "crop_yields"],
        "icon": "🌾",
    },
    "urban_resident": {
        "name": "Urban Resident",
        "description": "City dwellers interested in sustainable lifestyle choices",
        "characteristics": [
            "tech_savvy",
            "environmentally_conscious",
            "busy_lifestyle",
        ],
        "language_level": "moderate",
        "primary_concerns": ["air_quality", "recycling", "green_spaces"],
        "icon": "🏢",
    },
    "business_owner": {
        "name": "Small Business Owner",
        "description": "Entrepreneurs looking to balance sustainability with profitability",
        "characteristics": [
            "profit_oriented",
            "efficiency_focused",
            "community_minded",
        ],
        "language_level": "professional",
        "primary_concerns": ["energy_efficiency", "waste_reduction", "cost_savings"],
        "icon": "💼",
    },
    "student": {
        "name": "University Student",
        "description": "Young adults passionate about climate action and social change",
        "characteristics": ["idealistic", "tech_native", "socially_conscious"],
        "language_level": "academic",
        "primary_concerns": ["future_impact", "sustainable_living", "social_justice"],
        "icon": "📚",
    },
    "parent": {
        "name": "Parent",
        "description": "Parents concerned about their children's environmental future",
        "characteristics": ["family_oriented", "safety_conscious", "long_term_planner"],
        "language_level": "simple",
        "primary_concerns": [
            "health_impacts",
            "future_generations",
            "clean_environment",
        ],
        "icon": "👨‍👩‍👧‍👦",
    },
    "senior": {
        "name": "Senior Citizen",
        "description": "Experienced individuals with traditional values and environmental concerns",
        "characteristics": ["traditional", "value_conscious", "community_oriented"],
        "language_level": "simple",
        "primary_concerns": ["health", "cost_of_living", "community_impact"],
        "icon": "👴",
    },
    "tech_professional": {
        "name": "Tech Professional",
        "description": "Technology workers interested in innovative climate solutions",
        "characteristics": ["innovation_focused", "data_driven", "solution_oriented"],
        "language_level": "technical",
        "primary_concerns": ["technological_solutions", "data_analysis", "efficiency"],
        "icon": "💻",
    },
    "educator": {
        "name": "Educator",
        "description": "Teachers and professors who want to communicate climate issues effectively",
        "characteristics": ["knowledge_sharing", "analytical", "community_impact"],
        "language_level": "academic",
        "primary_concerns": ["education", "research", "public_awareness"],
        "icon": "👩‍🏫",
    },
}

# Cache Configuration
CACHE_TTL = 3600  # 1 hour

# UI Configuration
THEME_COLOR = "#1abc9c"
SECONDARY_COLOR = "#2c3e50"
BACKGROUND_COLOR = "#f8f9fa"
