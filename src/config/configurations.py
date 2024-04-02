import os
from dotenv import load_dotenv

load_dotenv()

# Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY', '')

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
