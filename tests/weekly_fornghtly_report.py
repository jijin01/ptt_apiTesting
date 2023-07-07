import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_wkly_forngtly_api():
    url = 'https://dev-api.pttapp.com/api/reports/weekly-fortnightly?client=635132a4dc29b4bad9e74d90&fromDate=2023-01-01&toDate=2023-07-07&currency=GBP'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    print(f"The status code is: {response.status_code}")

    data = response.json()
    client_Name = data["clientName"]
    expected_client_Name = "Jijin"
    assert client_Name == expected_client_Name, f"Expected clientName: {expected_client_Name}, Actual clientName: {client_Name}"

    if client_Name == expected_client_Name:
        print("Weekly-Fortnightly Report Listed Successfully")
    else:
        print("Something went wrong")

    banking_amount = data["bankingAmount"]
    claim_amount = data["claimAmount"]

    print(f"Banking Amount: {banking_amount}")
    print(f"Claim Amount: {claim_amount}")

    export_url = 'https://dev-api.pttapp.com/api/reports/weekly-fortnightly/export?client=635132a4dc29b4bad9e74d90&fromDate=2023-01-01&toDate=2023-07-07&currency=GBP'

    export_response = requests.get(export_url, headers=headers)
    print(f"Export API status code: {export_response.status_code}")
    print(f"Export API response content: {export_response.content}")

    try:
        assert export_response.status_code == 200
        expected_filename = "[Content_Types].xml"
        assert expected_filename in export_response.content.decode('latin-1'), f"Expected filename '{expected_filename}' not found in response content."

        print("Weekly-Fortnightly Report exported Successfully")
    except AssertionError:
        print("Export API test failed. Weekly-Fortnightly Reports Export Failed.")


test_wkly_forngtly_api()
