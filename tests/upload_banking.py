import login
import requests
import pandas as pd

access_token = login.data["authenticationResult"]["AccessToken"]


def test_banking_file_upload():
    get_presigned_url = "https://dev-api.pttapp.com/api/banking/upload/presigned-url?clientId" \
                        "=63595f916a01b7ace483bcb1&fileName=20230711-Test-api-Banking."
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(get_presigned_url, headers=headers)
    assert response.status_code == 200
    print(response.content)

    data = response.json()
    presigned_url = data['presignedUrl']
    file_id = data['fileId']
    file_path = 'C:/Users/91812/pttApp-apiTesting/tests/test_file/20230711-Test-api-Banking.xls'
    df = pd.read_excel(file_path)

    with open(file_path, 'rb') as file:
        data = file.read()
        response = requests.put(presigned_url, data=data, headers={"Content-Type": "application/vnd.ms-excel"})
        assert response.status_code == 200

    body = {
        "clientId": "63595f916a01b7ace483bcb1",
        "fileName": "20230711-Test-api-Banking",
        "fileId": file_id
    }

    response = requests.post('https://dev-api.pttapp.com/api/banking/upload', headers=headers, json=body)
    print(response.content)
    if response.status_code == 201:
        print("Banking File Uploaded Successsfully")
    elif response.status_code == 400:
        error_message = response.content.decode('utf-8')
        expected_error_message = '{"errors":["Previous scan for the item is not completed."]}\n'
        assert error_message == expected_error_message, f"Expected: {expected_error_message}, Actual: {error_message}"
        print("Error: Previous scan for the item is not completed.")
    else:
        print("Banking file upload failed")


test_banking_file_upload()
