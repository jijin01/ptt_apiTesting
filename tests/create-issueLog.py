import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_create_issue_log():
    url = "https://dev-api.pttapp.com/api/issue-log"
    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "opened": "Test",
        "shortDescription": "Testing issue log api",
        "priority": "High",
        "resolutionNotes": "Testing",
        "status": "Resolved",
        "dateResolved": "2022-1-1"
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    print(response.json())
    assert "_id" in response.json()
    if "_id" in response.json():
        print("Issue log created successfully")


test_create_issue_log()
