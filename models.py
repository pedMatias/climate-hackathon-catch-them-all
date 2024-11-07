from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime

class MessageInput(BaseModel):
    content: str = Field(..., min_length=10, max_length=500)
    selected_personas: List[str]
    country: str = Field(..., description="Target audience's country")

class RelatedNewsItem(BaseModel):
    type: str
    link: Optional[HttpUrl] = None

class GeneratedContent(BaseModel):
    tone: str
    keywords: List[str]
    feedback: str
    related_news: List[RelatedNewsItem]
    article: str
    generated_at: datetime = Field(default_factory=datetime.now)

# Fixed: Made ProcessingError inherit from Exception
class ProcessingError(Exception):
    def __init__(self, error_type: str, message: str):
        self.error_type = error_type
        self.message = message
        self.timestamp = datetime.now()
        super().__init__(self.message)
        
    def to_dict(self):
        return {
            "error_type": self.error_type,
            "message": self.message,
            "timestamp": self.timestamp
        }