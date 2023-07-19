import login
import requests

access_token = login.data["authenticationResult"]["AccessToken"]


def test_banking_transaction_update_api():
    url = "https://dev-api.pttapp.com//api/banking/transaction/64b6733a1d2d6ba3435318fd"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    body = {
        "amount": 4500,
        "status": "Cancelled",
        "bookingStatus": "completed",
        "type": "Testing",
        "currencyCode": "GBP,USD,RS",
        "totalBookingValue": "2000",
        "statusReason": "Testing banking update API"

    }

    response = requests.put(url, json=body, headers=headers)

    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)
    print("Banking Transaction updated successfully")


test_banking_transaction_update_api()
