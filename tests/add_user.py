import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_user_creation():
    url = 'https://dev-api.pttapp.com/api/create-client'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        "username": "jijin01",
        "email": "jijinvarghese14@gmail.com",
        "name": "JIJIN",
        "clientId": "JV01"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        assert 'success' in response.json()
        print("user created successfully")
    elif response.status_code == 400:
        assert 'errors' in response.json()
        assert 'User account already exists' in response.json()['errors']
        print("User account already exists")

    else:
        print("Something went wrong")


test_user_creation()
