import allure


@allure.feature("API")
@allure.story("Booking")
def test_create_booking_via_api(booking_client):
    payload = {
        "firstname": "Paul",
        "lastname": "Znaev",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-06-01",
            "checkout": "2026-06-07",
        },
        "additionalneeds": "Breakfast",
    }

    response = booking_client.create_booking(payload)

    assert response.status_code == 200, response.text

    response_body = response.json()

    assert "bookingid" in response_body
    assert response_body["booking"]["firstname"] == payload["firstname"]
    assert response_body["booking"]["lastname"] == payload["lastname"]