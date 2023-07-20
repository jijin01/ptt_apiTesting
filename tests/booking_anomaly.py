import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_booking_anomaly_api():
    url = "https://dev-api.pttapp.com/api/booking/anomalies"
    header = {
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "bookingReference": "HAY-3739474",
        "query": ""
    }

    response = requests.post(url, json=payload, headers=header)
    assert response.status_code == 200, f"API call failed with status code {response.status_code}"
    data = response.json()

    assert "anomalies" in data, "No 'anomalies' key in the response"
    assert isinstance(data["anomalies"], list), "'anomalies' should be a list"
    anomaly = data["anomalies"][0]

    assert "anomalyCategory" in anomaly, "No 'anomalyCategory' key in the anomaly"
    assert anomaly["anomalyCategory"] == "claims", "Unexpected 'anomalyCategory' value"
    print("Booking Anomalies Created Successfully")


test_booking_anomaly_api()
