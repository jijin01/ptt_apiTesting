import login
import requests
import pytest

access_token = login.data["authenticationResult"]["AccessToken"]


def test_claim_details_api():
    url = 'https://dev-api.pttapp.com/api/claim/details/649137cf0fe5229602dcb66e'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    print(f"The status code is: {response.status_code}")
    assert response.json()["_id"] == "649137cf0fe5229602dcb66e"
    if response.json()["_id"] == "649137cf0fe5229602dcb66e":
        print("Claim details listed successfully")
    else:
        print("Invalid Claim ID")


test_claim_details_api()
