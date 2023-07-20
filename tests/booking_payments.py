import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_booking_payment_api():
    url = "https://dev-api.pttapp.com/api/booking/payments"
    header = {
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "bookingReference": "3669195",
        "query": "null"
    }

    response = requests.post(url, json=payload, headers=header)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    key_to_assert = "count"
    assert key_to_assert in data, f"Key '{key_to_assert}' not found in the response"
    assert isinstance(data[key_to_assert], int), f"Value for key '{key_to_assert}' is not an integer"
    assert data[key_to_assert] == 0, f"Expected value 0 for key '{key_to_assert}', but got {data[key_to_assert]}"
    print("Booking Payments Created Successfully")


test_booking_payment_api()
