import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_client_files_api():
    url = 'https://dev-api.pttapp.com/api/reports/bank-reconciliation?client=635132a4dc29b4bad9e74d90&currency=GBP' \
          '&fromDate=2023-01-01&toDate=2023-07-17'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(f"The status code is: {response.status_code}")
    response_data = response.json()
    Client_name = response_data.get("clientName", None)
    assert Client_name == "Jijin"

    if Client_name == "Jijin":
        print("Bank Reconciliation Report Listed Successfully")
    else:
        print("Something went wrong")

    export_url = 'https://dev-api.pttapp.com/api/reports/bank-reconciliation/export?client=635132a4dc29b4bad9e74d90' \
                 '&currency=GBP&fromDate=2023-01-01&toDate=2023-07-17'

    response = requests.get(export_url, headers=headers)
    assert response.status_code == 200
    print(response.status_code)
    print(response.content)

    expected_filename = "[Content_Types].xml"
    assert expected_filename in response.content.decode(
        'latin-1'), f"Expected filename '{expected_filename}' not found in response content."
    if expected_filename in response.content.decode('latin-1'):
        print("Bank Reconciliation Report exported Successfully")

    assert len(response.content) > 0, "Response content is empty."


test_client_files_api()
