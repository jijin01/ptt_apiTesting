import login
import pytest
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


@pytest.mark.parametrize("size", [""])
def test_anomalies_banking(size):
    url = "https://dev-api.pttapp.com/api/anomaly/banking"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "query": "Jijin",
        "fromDate": "01/11/2022",
        "toDate": "30/06/2023",
        "page": "1",
        "size": size
    }

    response = requests.post(url, headers=headers, json=payload)

    assert response.status_code == 200
    assert "content" in response.json()
    results = response.json()["content"]
    assert len(results) > 0
    client_name = results[0]["clientName"]
    assert client_name == "Jijin"
    if client_name == "Jijin":
        print("There are Unresolved Anomalies ")


test_anomalies_banking(size="10")
