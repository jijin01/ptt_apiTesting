import login
import pytest
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_client_export_api():
    url = 'https://dev-api.pttapp.com/api/client/search/export'
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    body = {
        "query": None
    }

    response = requests.post(url, headers=headers, json=body)
    assert response.status_code == 200
    print(response.status_code)
    print(response.content)

    expected_filename = "[Content_Types].xml"
    assert expected_filename in response.content.decode('latin-1'), f"Expected filename '{expected_filename}' not " \
                                                                    f"found in response content."
    if expected_filename in response.content.decode('latin-1'):
        print("Client list exported Successfully")

    assert len(response.content) > 0, "Response content is empty."


pytest.main(['-v'])
