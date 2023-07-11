import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_latest_claim_search():
    url = "https://dev-api.pttapp.com/api/claim/search/latest"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        "query": None,
        "client": "635132a4dc29b4bad9e74d90",
        "status": "Submitted",
        "assignedTo": "Nithin",
        "fromDate": "2023-06-11",
        "toDate": "2023-07-15",
        "page": 1,
        "size": 4
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert 'totalElements' in data
    if 'totalElements' in data:
        print("Latest Claims Listed Successfully")


test_latest_claim_search()

