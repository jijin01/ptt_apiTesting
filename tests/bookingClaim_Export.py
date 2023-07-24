import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_booking_claim_export_api():
    url = 'https://dev-api.pttapp.com/api/booking/claims/export'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "bookingReference": "3669195",
        "query": "null"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    expected_filename = "[Content_Types].xml"
    assert expected_filename in response.content.decode('latin-1'), f"Expected filename '{expected_filename}' not " \
                                                                    f"found in response content."
    if expected_filename in response.content.decode('latin-1'):
        print("Booking Claim exported Successfully")

    assert len(response.content) > 0, "Response content is empty."


test_booking_claim_export_api()
