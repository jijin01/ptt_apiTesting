import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_get_dashboard_details():
    url = 'https://dev-api.pttapp.com/api/dashboard/details?currency=EUR'
    header = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=header)
    assert response.status_code == 200
    print(response.status_code)
    print(response.json())
    data = response.json()
    assert 'clientsCount' in data
    assert isinstance(data['clientsCount'], int)

    assert 'totalClaims' in data
    assert isinstance(data['totalClaims'], float)

    assert 'totalClients' in data
    assert isinstance(data['totalClients'], int)

    assert 'totalPayments' in data
    assert isinstance(data['totalPayments'], float)

    assert 'unhandledAnomalies' in data
    assert isinstance(data['unhandledAnomalies'], int)

    if data == response.json():
        print("Dashboard Data Is Available")


test_get_dashboard_details()
