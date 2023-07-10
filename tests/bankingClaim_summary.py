import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


import requests

def test_bankingClaim_summary_api():
    url = 'https://dev-api.pttapp.com/api/reports/banking-claim-summary?client=635132a4dc29b4bad9e74d90&fromDate=2023-01-01&toDate=2023-07-07&page=1&size=100'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    print(f"The status code is: {response.status_code}")

    data = response.json()
    content = data["content"]

    client_name = None
    for item in content:
        if "clientName" in item:
            client_name = item["clientName"]
            break

    expected_client_name = "Jijin"
    assert client_name == expected_client_name, f"Expected clientName: {expected_client_name}, Actual clientName: {client_name}"

    if client_name == expected_client_name:
        print("Banking And Claim Summary Report Listed Successfully")
    else:
        print("Something went wrong")



    export_url = 'https://dev-api.pttapp.com/api/reports/banking-claim-summary/export?client=635132a4dc29b4bad9e74d90&fromDate=2023-01-01&toDate=2023-07-07'

    export_response = requests.get(export_url, headers=headers)
    print(f"Export API status code: {export_response.status_code}")
    print(f"Export API response content: {export_response.content}")

    try:
        assert export_response.status_code == 200
        expected_filename = "[Content_Types].xml"
        assert expected_filename in export_response.content.decode('latin-1'), f"Expected filename '{expected_filename}' not found in response content."

        print("Banking And Claim Summary Report exported Successfully")
    except AssertionError:
        print("Export API test failed. Banking And Claim Summary Reports Export Failed.")


test_bankingClaim_summary_api()
