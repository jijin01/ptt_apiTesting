import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_lookUp_bankingColumns():
    url = 'https://dev-api.pttapp.com/api/lookup/banking-columns'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    expected_keys = ["_id", "columnName", "dataType", "name", "preferred"]
    json_response = response.json()

    for item in json_response:
        assert all(key in item for key in expected_keys)
    print("Banking columns listed successfully")


test_lookUp_bankingColumns()
