import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_booking_claims_api():
    url = "https://dev-api.pttapp.com/api/booking/claims"
    header = {
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "bookingReference": "HAY-3739474",
        "query": ""
    }

    response = requests.post(url, json=payload, headers=header)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    json_response = response.json()
    assert 'claims' in json_response, "Key 'claims' not found in the response"
    assert isinstance(json_response['claims'], list) and len(json_response['claims']) >= 0, "Invalid 'claims' data"
    assert 'count' in json_response, "Key 'count' not found in the response"
    assert isinstance(json_response['count'], int) and json_response['count'] >= 0, "Invalid 'count' data"
    first_claim = json_response['claims'][0]
    assert 'amount' in first_claim, "Key 'amount' not found in the claim data"
    assert isinstance(first_claim['amount'], float) and first_claim['amount'] >= 0, "Invalid 'amount' data"
    print("Booking Claims Created Successfully")

test_booking_claims_api()