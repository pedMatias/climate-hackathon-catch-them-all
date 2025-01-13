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
    "rural_person": {
        "name": "Rural Person",
        "description": "Individuals living in rural areas who are closely connected to the land and concerned about the impact of climate change on agriculture and local ecosystems",
        "characteristics": ["land_stewardship", "resourcefulness", "community_minded"],
        "language_level": "simple",
        "primary_concerns": ["water availability", "crop yields", "soil health", "wildlife impact"],
        "icon": "🌾"
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
    "senior": {
        "name": "Senior Citizen",
        "description": "Experienced individuals with traditional values and environmental concerns",
        "characteristics": ["traditional", "value_conscious", "community_oriented"],
        "language_level": "simple",
        "primary_concerns": ["health", "cost_of_living", "community_impact"],
        "icon": "👴",
    },
    "youth": {
        "name": "Youth",
        "description": "Young individuals who are passionate about climate action, social change, and the future of the planet",
        "characteristics": ["idealistic", "tech-savvy", "socially_active"],
        "language_level": "informal",
        "primary_concerns": ["future impact", "social justice", "sustainable living"],
        "icon": "🌍"
    },
    "educated_person": {
        "name": "Educated person",
        "description": "People with master's degree or PhD who want to communicate climate issues effectively",
        "characteristics": ["knowledge_sharing", "analytical", "community_impact"],
        "language_level": "academic",
        "primary_concerns": ["education", "research", "public_awareness"],
        "icon": "🏛️",
    },
    "no_degree_person": {
        "name": "No Degree Person",
        "description": "Individuals with practical experience who are interested in straightforward climate information",
        "characteristics": ["practical_mindset", "hands-on", "community_oriented"],
        "language_level": "simple",
        "primary_concerns": ["local environmental impact", "job security", "cost of living"],
        "icon": "🛠️"
    },
    "high_income_person": {
        "name": "High Income Person",
        "description": "Professionals and individuals with high disposable income who prioritize sustainable luxury and innovative climate solutions",
        "characteristics": ["innovation_focused", "environmentally_conscious", "future_oriented"],
        "language_level": "professional",
        "primary_concerns": ["sustainable investments", "green technology", "luxury eco-friendly products"],
        "icon": "💼"
    },
    "low_income_person": {
        "name": "Low Income Person",
        "description": "Individuals with limited disposable income who are concerned about the affordability and direct impact of climate change on daily life",
        "characteristics": ["cost_sensitive", "community_oriented", "practical_mindset"],
        "language_level": "simple",
        "primary_concerns": ["energy costs", "health impacts", "local environmental issues"],
        "icon": "🏠"
    }
}

# Cache Configuration
CACHE_TTL = 3600  # 1 hour

# UI Configuration
THEME_COLOR = "#1abc9c"
SECONDARY_COLOR = "#2c3e50"
BACKGROUND_COLOR = "#f8f9fa"
