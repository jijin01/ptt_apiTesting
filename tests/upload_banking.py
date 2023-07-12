import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_banking_file_upload():
    get_presigned_url = "https://dev-api.pttapp.com/api/banking/upload/presigned-url?clientId=635132a4dc29b4bad9e74d90&fileName=20230711-Test-api-Banking.xls"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(get_presigned_url, headers=headers)
    assert response.status_code == 200
    print(response.content)

    data = response.json()
    presigned_url = data['presignedUrl']
    file_id = data['fileId']
    with open('C:/Users/91812/pttApp-apiTesting/tests/test_file/20230711-Test-api-Banking.xls', 'rb') as file:
        response = requests.put(presigned_url, files={'file': file})
        assert response.status_code == 200

    body = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "fileName": "20230711-Test-api-Banking.xls",
        "fileId": file_id
    }

    response = requests.post('https://dev-api.pttapp.com/api/banking/upload', headers=headers, json=body)
    print(response.content)
    # assert response.status_code == 200
