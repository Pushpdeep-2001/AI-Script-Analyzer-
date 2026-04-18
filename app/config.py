import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    """Central configuration class for the application."""
    
    def __init__(self):
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        self.MODEL = os.getenv("MODEL")
        
        # Project metadata
        self.PROJECT_NAME = "AI Script Analyzer"
        self.VERSION = "1.0.0"

# Create a singleton instance
settings = Config()
