import anthropic
from typing import Dict, Any
import json
import logging
from config import CLAUDE_API_KEY
from models import MessageInput, GeneratedContent
import ssl

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ClaudeService:
    def __init__(self):
        try:
            self.client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
            logger.info("Anthropic client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Anthropic client: {e}")
            raise

    def _get_response(self, prompt: str) -> str:
        try:
            logger.debug(f"Sending prompt: {prompt}")
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            logger.info("Message received successfully")

            # Extract text from content, handling both single and multiple content blocks
            if isinstance(message.content, list):
                # If multiple content blocks, concatenate their text
                response_text = " ".join(
                    block.text for block in message.content if hasattr(block, "text")
                )
            elif hasattr(message.content, "text"):
                # If single content block
                response_text = message.content.text
            else:
                # Fallback to string representation if unexpected format
                response_text = str(message.content)

            return response_text
        except Exception as e:
            logger.error(f"Error getting Claude response: {e}")
            raise Exception(f"Error getting Claude response: {str(e)}")

    def _build_analysis_prompt(self, message: str, persona: Dict[str, Any]) -> str:
        return f"""As a climate communications expert, analyze this message and provide guidance:

Message: {message}
Target Audience: {persona['name']}

Audience Characteristics:
- Primary concerns: {', '.join(persona['primary_concerns'])}
- Language level: {persona['language_level']}
- Key characteristics: {', '.join(persona['characteristics'])}

Please provide a complete analysis including:
1. Appropriate tone for this audience
2. Key phrases and keywords that will resonate
3. Specific feedback on message effectiveness
4. Types of news stories that would interest this audience
5. A sample article tailored to this audience

Respond STRICTLY in the following JSON format:
{{
    "tone": "description of appropriate tone",
    "keywords": ["list", "of", "keywords"],
    "feedback": "specific feedback on message",
    "related_news": ["list", "of", "news", "types"],
    "article": "complete sample article"
}}

Important: Ensure the response is a valid JSON object that can be parsed directly."""

    def generate_content(
        self, message_input: MessageInput, persona_data: Dict[str, Any]
    ) -> GeneratedContent:
        try:
            prompt = self._build_analysis_prompt(message_input.content, persona_data)
            response = self._get_response(prompt)

            # Attempt to parse the JSON response
            try:
                # Strip any leading/trailing whitespace or code block markers
                response = response.strip("```json\n```\n").strip()
                content = json.loads(response)
                return GeneratedContent(**content)
            except json.JSONDecodeError as json_error:
                logger.error(f"Failed to parse Claude response as JSON: {json_error}")
                logger.error(f"Problematic response: {response}")
                raise ValueError(
                    f"Failed to parse Claude response as JSON: {json_error}"
                )

        except Exception as e:
            logger.error(f"Error generating content: {e}")
            raise Exception(f"Error generating content: {str(e)}")
