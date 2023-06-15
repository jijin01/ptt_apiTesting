import requests

payload = {"username": "nismal", "password": "Simple2022$"}
url = "https://dev-api.pttapp.com/api/"
response = requests.post(url + "login", json=payload)
data = response.json()
access_token = data["authenticationResult"]["AccessToken"]
print("AccessToken is: " + access_token)
expected_username = "nismal"
expected_password = "Simple2022$"


def login(username, password):
    url = "https://dev-api.pttapp.com/api/"
    response = requests.post(url + "login", json=payload)

    data = {
        "username": username,
        "password": password
    }

    if response.status_code == 200 and data["username"] == expected_username and data["password"] == expected_password:
       print("Login successful - Expected username and password match the actual values")
       assert data["username"] == expected_username, f"Username assertion failed. Expected: {expected_username}, Actual: {data['username']}"
       assert data["password"] == expected_password, f"Password assertion failed. Expected: {expected_password}, Actual: {data['password']}"


    else:
        print("Login failed - invalid credentials")


login("nismal", "Simple2022$")







