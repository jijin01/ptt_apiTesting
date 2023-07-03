import login
import requests
import pytest

access_token = login.data["authenticationResult"]["AccessToken"]

def test_claim_details_api():
    url = 'https://dev-api.pttapp.com/api/reports/trust-balance?client=635132a4dc29b4bad9e74d90&currency=GBP'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    print(f"The status code is: {response.status_code}")
    assert "content" in response.json()
    results = response.json()["content"]
    assert len(results) > 0
    client_ID = results[0]["cId"]
    assert client_ID == "JV01"

    if client_ID == "JV01":
        print("Trust Balance Report Listed Successfully")
    else:
        print("Something went wrong")

    export_url = 'https://dev-api.pttapp.com/api/reports/trust-balance/export?client=635132a4dc29b4bad9e74d90'
    export_params = {
        "currency": "GBP"
    }

    export_response = requests.get(export_url, headers=headers, params=export_params)
    print(f"Export API status code: {export_response.status_code}")
    print(f"Export API response content: {export_response.json()}")

    try:
        assert export_response.status_code == 202 or export_response.status_code == 409
        message = export_response.json()["message"]
        assert message == "Generation of Trust Balance Reports initiated." or message == "TBR is already under generation for the selected filters"
        print("Export API test passed. Trust Balance Reports generation initiation successful.")
    except AssertionError:
        print("Export API test failed. Trust Balance Reports generation initiation unsuccessful.")

test_claim_details_api()
