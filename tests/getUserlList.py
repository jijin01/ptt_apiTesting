import json
import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_users_list_api():
    url = "https://dev-api.pttapp.com/api/list-user"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200

    data = response.json()
    print("List Of Users is " + json.dumps(data))
    assert isinstance(data, list)
    assert len(data) > 0
    if response.status_code == 200:
        print("Users list printed successfully")


test_users_list_api()
