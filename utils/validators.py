import os
import logging
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def check_api_key():
    """
    Check and retrieve the OPEN_AI_API_KEY from environment variables.
    """
    # API_KEY = os.getenv("OPEN_AI_API_KEY")
    api_key = os.getenv("OPEN_AI_API_KEY")

    if not api_key:
        logging.error("Environment variable 'OPEN_AI_API_KEY' is not set.")
        raise EnvironmentError("Environment variable 'OPEN_AI_API_KEY' is not set.")
    else:
        logging.debug("API Key has been feteched from environment")
    return api_key


def is_valid_email(email):
    """
    Validate whether the given email is well-formed and belongs to an allowed domain.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        return False
    allowed_domains = ["gmail.com"]
    return any(email.endswith(f"@{domain}") for domain in allowed_domains)
