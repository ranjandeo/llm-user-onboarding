import logging
from utils.logger import configure_logger
from app.excel_operations import (
    load_excel,
    save_invalid_emails,
    process_emails,
)
from utils.validators import check_api_key

configure_logger()
logging.info("Starting the script execution")

API_KEY = check_api_key()
FILE_NAME = "./data/users.xlsx"
SHEET_NAME = "Users"


def main():
    wb, sheet = load_excel(FILE_NAME, SHEET_NAME)
    invalid_emails = process_emails(wb, sheet, FILE_NAME, API_KEY)
    save_invalid_emails(wb, invalid_emails, FILE_NAME)
    logging.info("Script execution finished")


if __name__ == "__main__":
    main()
