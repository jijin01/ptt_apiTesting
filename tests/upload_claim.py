import login
import requests
import pandas as pd

access_token = login.data["authenticationResult"]["AccessToken"]


def test_claim_file_upload():
    get_presigned_url = "https://dev-api.pttapp.com/api/claim/upload/presigned-url?clientId=635132a4dc29b4bad9e74d90" \
                        "&fileName=20230714-claim-file&claimFromTBR=false"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(get_presigned_url, headers=headers)
    print(response.content)
    assert response.status_code == 200

    data = response.json()
    presigned_url = data['presignedUrl']
    file_id = data['fileId']
    file_path = 'C:/Users/91812/pttApp-apiTesting/tests/test_file/20230714-claim-file.xlsx'
    df = pd.read_excel(file_path)

    with open(file_path, 'rb') as file:
        data = file.read()
        response = requests.put(presigned_url, data=data, headers={"Content-Type": "application/vnd.ms-excel"})
        assert response.status_code == 200

    body = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "fileName": "20230714-claim-file.",
        "fileId": file_id,
        "claimFromTBR": "false"
    }

    response = requests.post('https://dev-api.pttapp.com/api/claim/upload', headers=headers, json=body)
    print(response.content)
    print(response.status_code)
    if response.status_code == 201:
        print("Claim File Uploaded Successsfully")
    elif response.status_code == 400:
        error_message = response.content.decode('utf-8')
        expected_error_message = '{"errors":["Previous scan for the item is not completed."]}\n'
        assert error_message == expected_error_message, f"Expected: {expected_error_message}, Actual: {error_message}"
        print("Error: Previous scan for the item is not completed.")
    elif response.status_code == 409:
        error_message = response.content.decode('utf-8')
        expected_error_message = '{"message":"ClaimFromTBR is not enabled for this client"}\n'
        assert error_message == expected_error_message, f"Expected: {expected_error_message}, Actual: {error_message}"
        print("ClaimFromTBR is not enabled for this client")
    else:
        print("Claim file upload failed")


test_claim_file_upload()
