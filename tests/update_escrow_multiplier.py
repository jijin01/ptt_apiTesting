import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_update_escrow_multiplier():
    url = 'https://dev-api.pttapp.com/api/client/636cc22bd412435f13cb3030/escrow_multiplier'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        "date": "2023-07-17",
        "multiplier": 5
    }
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200
    if response.status_code == 200:
        print("Escrow Multiplier Updated Successfully")
    else:
        print("Updation Failed")


