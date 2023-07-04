import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_client_files_api():
    url = 'https://dev-api.pttapp.com/api/reports/client-files?client=635132a4dc29b4bad9e74d90&fromDate=2023-03-20&toDate=2023-07-04&page=1&size=3'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(f"The status code is: {response.status_code}")
    assert "content" in response.json()
    results = response.json()["content"]
    assert len(results) > 0
    Client_name = results[0]["clientName"]
    assert Client_name == "Jijin"

    if Client_name == "Jijin":
        print("Client file Report Listed Successfully")
    else:
        print("Something went wrong")

    export_url = 'https://dev-api.pttapp.com/api/reports/client-files/export?client=635132a4dc29b4bad9e74d90&fromDate=2023-03-20&toDate=2023-07-04&page=1&size=3'

    response = requests.get(export_url, headers=headers, )
    assert response.status_code == 200
    print(response.status_code)
    print(response.content)

    expected_filename = "[Content_Types].xml"
    assert expected_filename in response.content.decode('latin-1'), f"Expected filename '{expected_filename}' not " \
                                                                    f"found in response content."
    if expected_filename in response.content.decode('latin-1'):
        print("Client file exported Successfully")

    assert len(response.content) > 0, "Response content is empty."


test_client_files_api()
