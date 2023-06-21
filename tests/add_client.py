import login
import pytest
import requests
import json
import random

access_token = login.data["authenticationResult"]["AccessToken"]


@pytest.fixture
def base_url():
    return "https://dev-api.pttapp.com/api/"


@pytest.fixture
def auth_token():
    return access_token


def generate_random_number():
    return random.randint(1000, 9999)


def test_create_client(base_url, auth_token):
    step1_url = base_url + "client/basic-info"
    # step2_url = base_url + "/step/2"
    # step3_url = base_url + "/step/3"
    # step4_url = base_url + "/step/4"
    # step5_url = base_url + "/step/5"
    # step6_url = base_url + "/step/6"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Connection": "keep-alive",

    }
    random_number = generate_random_number()

    step1_data = {
        "friendlyName": f"Alex_{random_number}",

        "fullName": f"ALEX George_{random_number}",

        "typeOfTrustAccount": "61ef4e0da0d0ef7c56884319",

        "cId": f"abC0M1_{random_number}",

        "existingClient": False,

        "create": True,

        "goLiveDate": "2027-05-03",

        "reuseOldBooking": False,

    }
    try:

        step1_response = requests.put(step1_url, json=step1_data, headers=headers)
        print(step1_response.content)
        print(step1_response.status_code)

        try:
            response_json = step1_response.json()
            print("The response is :" + json.dumps(response_json))
            assert "clientId" in response_json
            print("Valid response: clientId exists in the response.")



        except json.JSONDecodeError:
            print("Response is not in JSON format")
            # Handle the response that is not in JSON format
            # ...
    except requests.exceptions.RequestException as e:
        print("Error:", e)


test_create_client("base_url", auth_token)
