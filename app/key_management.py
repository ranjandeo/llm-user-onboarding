import os
import requests
import logging


def generate_key(email, alias, api_key):
    """
    Generate an API key for the given user using the Requests library.

    This function sends a POST request to generate an API key associated with the provided email and alias.
    The key will have access to specific models.

    Parameters:
    email (str): The email address of the user for whom the key is to be generated.
    alias (str): An alias for the key.
    API_KEY (str): The API key for authentication.

    Returns:
    requests.Response: The response object from the requests library.
    """
    # Load the URLs from environment variables
    base_url = os.getenv("BASE_URL")
    generate_key_endpoint = os.getenv("GENERATE_KEY_URL")

    if not base_url or not generate_key_endpoint:
        logging.error("BASE_URL or GENERATE_KEY_URL environment variables are not set.")
        raise EnvironmentError(
            "BASE_URL or GENERATE_KEY_URL environment variables are not set."
        )

    # Construct the full API URL
    full_url = f"{base_url}{generate_key_endpoint}"

    # Prepare the data and headers for the POST request
    data_generate_key = {
        "models": ["gpt-4o", "codellama"],
        "user_id": email,
        "key_alias": alias,
    }
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Make the POST request
    try:
        response = requests.post(full_url, headers=headers, json=data_generate_key)
        logging.info(
            f"API key generation request for {email} sent. Status code: {response.status_code}, Response: {response.text}"
        )
        return response.text
    except requests.RequestException as e:
        logging.error(f"Request failed: {str(e)}")
        raise
