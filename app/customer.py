import os
import requests
import logging


def create_new_customer(email, alias, api_key):
    """
    Create a new customer using the provided email and alias using the Requests library.

    This function sends a POST request to create a new customer with the given email and alias.
    It logs the request details and the response received.

    Parameters:
    email (str): The email address of the new customer.
    alias (str): An alias for the new customer.
    API_KEY (str): The API key for authentication.

    Returns:
    requests.Response: The response object from the requests library.
    """
    # Load the URLs from environment variables
    base_url = os.getenv("BASE_URL")
    customer_api_endpoint = os.getenv("CUSTOMER_API_URL")

    if not base_url or not customer_api_endpoint:
        logging.error("BASE_URL or CUSTOMER_API_URL environment variables are not set.")
        raise EnvironmentError(
            "BASE_URL or CUSTOMER_API_URL environment variables are not set."
        )

    # Construct the full API URL
    full_url = f"{base_url}{customer_api_endpoint}"

    # Prepare the data and headers for the POST request
    data_new_customer = {"user_id": email, "alias": alias}
    headers = {
        "accept": "application/json",
        "API-Key": api_key,
        "Content-Type": "application/json",
    }

    # Make the POST request
    try:
        response = requests.post(full_url, headers=headers, json=data_new_customer)
        logging.info(
            f"Customer creation request for {email} sent. Status code: {response.status_code}, Response: {response.text}"
        )
        return response.text
    except requests.RequestException as e:
        logging.error(f"Request failed: {str(e)}")
        raise
