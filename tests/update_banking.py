import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_banking_update_api():
    url = "https://dev-api.pttapp.com//api/banking/update"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    body = {
        "bankingId": "64b6732d7eb37dfcabbf75c5",
        "notes": "testing api",
        "status": "Submitted",
        "assignedTo": "63595f916a01b7ace483bdd5"
    }

    response = requests.put(url, json=body, headers=headers)

    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)
    print("Banking Details updated successfully")


test_banking_update_api()
