import login
import pytest
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


@pytest.fixture
def api_url():
    return "https://dev-api.pttapp.com/api/logout"


def test_logout(api_url):

    header = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(api_url, access_token, headers=header)

    assert response.status_code == 200
    if response.status_code == 200:
        print(response.status_code)
        print("logOut Successful")
        print(response.content)


