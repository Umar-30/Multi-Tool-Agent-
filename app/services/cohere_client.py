import cohere

from app.config import settings


co = cohere.Client(
    settings.COHERE_API_KEY
)