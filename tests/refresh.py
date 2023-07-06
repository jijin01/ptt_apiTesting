import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]
refresh_token = login.data["authenticationResult"]["RefreshToken"]


def test_refresh():
    url = 'https://dev-api.pttapp.com/api/refresh'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    payload = {"refreshToken": refresh_token

    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    print(response.status_code)
    print(response.content)
    assert "AuthenticationResult" in response.json()
    if "AuthenticationResult" in response.json():
        print("Refresh Successfully")
    else:
        print("Invalid Refresh Token")


test_refresh()
