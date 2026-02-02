import os
import json
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

FRONTLINE_SENDER = "notifications@mail11.frontlineed.com"

TICKET_BEARER_TOKEN = os.getenv("TICKET_BEARER_TOKEN")
TICKET_API_URL = os.getenv("TICKET_API_URL")

if not TICKET_API_URL or not TICKET_BEARER_TOKEN:
    raise RuntimeError("Missing TICKET_API_URL or TICKET_BEARER_TOKEN")

headers = {
    "Authorization": f"Bearer {TICKET_BEARER_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

payload = {
    "ticket_subject": "Testing API",
    "ticket_description": "New hire setup for ",
}

def create_ticket_api():
    try:
        response = requests.post(
            TICKET_API_URL,
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        ticket_info = response.json()
        logging.info(f"Ticket created successfully: {ticket_info}")
        return ticket_info

    except requests.exceptions.RequestException as e:
        if getattr(e, "response", None) is not None:
            logging.error(f"Response body: {e.response.text}")
        logging.error(f"Error creating ticket: {e}")
        return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    create_ticket_api()
