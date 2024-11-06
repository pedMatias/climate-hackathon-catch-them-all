# Climate Communications Tool 🌍

A streamlined tool for NGO communication teams to generate targeted climate change messages for different audience personas using AI assistance.

## Features 🌟

- Simple, intuitive interface for message input
- Pre-defined audience personas with detailed characteristics
- AI-powered content generation using Claude 3.5 Sonnet
- Automated tone and keyword analysis
- Customized article generation
- Content caching for improved performance

## Quick Start 🚀

### Prerequisites

- Python 3.11 or higher
- Anthropic API key (Claude 3.5 Sonnet access)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-org/climate-comms-tool.git
cd climate-comms-tool
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```bash
CLAUDE_API_KEY=your-api-key-here
```

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Usage Guide 📖

1. **Enter Your Message**
   - Type your climate-related message in the text area
   - Keep it concise and focused on a single topic

2. **Select Target Audience**
   - Choose from predefined personas
   - Review persona characteristics and primary concerns

3. **Generate Content**
   - Click "Generate Content" to create tailored communication
   - Review the generated content in five categories:
     - Tone recommendations
     - Key keywords
     - Message feedback
     - Related news types
     - Sample article

## Project Structure 📁

```
├── app.py              # Main Streamlit application
├── config.py           # Configuration settings
├── models.py           # Pydantic data models
├── claude_service.py   # Claude API integration
├── utils.py           # Utility functions
├── personas.py        # Persona definitions
├── requirements.txt   # Project dependencies
├── .env              # Environment variables (not in repo)
└── README.md         # Project documentation
```

## Key Components 🔧

- **Streamlit Interface**: User-friendly web interface
- **Claude 3.5 Sonnet**: AI model for content generation
- **Persona System**: Predefined audience profiles
- **Caching System**: Performance optimization
- **Error Handling**: Robust error management

## Development 👨‍💻

### Adding New Personas

1. Open `config.py`
2. Add new persona definition to `AVAILABLE_PERSONAS`
3. Include all required fields:
   - name
   - description
   - characteristics
   - language_level
   - primary_concerns

### Modifying Prompts

1. Open `claude_service.py`
2. Update the `_build_analysis_prompt` method
3. Ensure JSON response structure remains consistent

## Environment Variables 🔑

Required environment variables:
- `CLAUDE_API_KEY`: Your Anthropic API key

## Troubleshooting 🔍

Common issues and solutions:

1. **API Key Error**
   ```
   ValueError: CLAUDE_API_KEY must be set in environment variables
   ```
   Solution: Ensure `.env` file exists with valid API key

2. **Streamlit Connection Error**
   ```
   Connection error: Failed to connect to Streamlit server
   ```
   Solution: Check if port 8501 is available

3. **Generation Timeout**
   ```
   Error generating content: Request timed out
   ```
   Solution: Check internet connection and API status
