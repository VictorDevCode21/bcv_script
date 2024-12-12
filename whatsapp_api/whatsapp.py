import os

from dotenv import load_dotenv
from requests import post


class Whatsapp:
    """
    A class to handle WhatsApp message sending using the WhatsApp API.

    Attributes:
    message (str): The message to be sent.
    """

    def __init__(self, message):
        """
        Initializes the Whatsapp object with a message.

        Args:
            message (str): The message to send.
        """
        self.message = message

    def get_information(self):
        """
        Retrieves necessary information from environment variables for sending the message.

        Returns:
            tuple: A tuple containing the receiver's phone number, sender's phone number, and API key.

        Raises:
            KeyError: If any of the required environment variables are missing.
        """

        # Load .env variables
        load_dotenv()  # Ensure environment variables are loaded

        receiver_phone = os.getenv("receiver_phone_number")
        sender_phone = os.getenv("sender_phone_number")
        api_key = os.getenv("api_key")

        if not all([receiver_phone, sender_phone, api_key]):
            raise KeyError(
                "One or more environment variables are missing: 'receiver_phone_number', 'sender_phone_number', 'api_key'."
            )

        return receiver_phone, sender_phone, api_key

    def send_message(self):
        """
        Sends a message using the WhatsApp API.

        Returns:
            dict: The API response as a dictionary.
        """
        try:
            receiver_phone, sender_phone, api_key = self.get_information()

            # Construct API request
            url = f"https://graph.facebook.com/v21.0/{sender_phone}/messages"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "messaging_product": "whatsapp",
                "to": receiver_phone,
                "type": "template",
                "template": {
                    "name": "bcv_price",
                    "language": {"code": "es"},
                    "components": [
                        {
                            "type": "header",
                            "parameters": [
                                {"type": "text", "text": self.message}  # message
                            ],
                        }
                    ],
                },
            }

            # Debugging: Print the payload to verify its structure
            print("Payload:", payload)

            # Send the message
            response = post(url, headers=headers, json=payload)

            # Check the response
            if response.status_code == 200:
                print("\nSuccessfully sent:", response.json())
            else:
                print(f"Failed to send message: {response.status_code}")
                print(response.json())

            return response.json()

        except KeyError as e:
            print(f"Error: {e}")
            return {"error": str(e)}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {"error": str(e)}
