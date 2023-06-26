import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_search_api():
    url = 'https://dev-api.pttapp.com/api/booking/search'
    payload = {"clientId": "635132a4dc29b4bad9e74d90", "bookingReference": "20261725"}
    header = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.post(url, json=payload, headers=header)
    assert response.status_code == 200
    print(response.status_code)
    print(response.json())
    data = response.json()
    assert data['_id'] == '649408fb8057ea2ae917867f'
    assert data['clientName'] == 'Jijin'
    if data['clientName'] == 'Jijin':
        print("Booking is Valid")


test_search_api()
