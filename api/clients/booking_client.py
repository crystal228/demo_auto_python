import requests


class BookingClient:
    def __init__(self, api_url: str):
        self.api_url = api_url.rstrip("/")

    def create_booking(self, payload: dict) -> requests.Response:
        return requests.post(
            f"{self.api_url}/booking",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10,
        )

    def get_booking(self, booking_id: int) -> requests.Response:
        return requests.get(
            f"{self.api_url}/booking/{booking_id}",
            timeout=10,
        )