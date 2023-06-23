import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_client_search():
    url = 'https://dev-api.pttapp.com/api/client/search'
    payload = {'clientName': 'Jijin'}
    header = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.post(url, json=payload, headers=header)
    assert response.status_code == 200
    assert any('Jijin' in client['friendlyName'] for client in response.json()['content'])
    if any('Jijin' in client['friendlyName'] for client in response.json()['content']):
        print("User found in the userList")


test_client_search()
