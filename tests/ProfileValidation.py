import login
import requests
import re
access_token = login.data["authenticationResult"]["AccessToken"]

def validate_profile(profile_data, expected_name, expected_username, expected_email, expected_profile_url):

    name = profile_data["name"]
    username = profile_data["username"]
    email = profile_data["email"]
    profile_url = profile_data["profile_url"]
    response = requests.get(profile_url)
    assert response.status_code == 200, "Profile URL is invalid"
    if response.status_code == 200:
        print("Profile Url Is Valid")
    assert name == expected_name, f"Name assertion failed. Expected: {expected_name}, Actual: {name}"
    assert username == expected_username, f"Username assertion failed. Expected: {expected_username}, Actual: {username}"
    assert email == expected_email, f"Email assertion failed. Expected: {expected_email}, Actual: {email}"
    assert profile_url == expected_profile_url, f"Profile URL assertion failed. Expected: {expected_profile_url}, Actual: {profile_url}"

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    assert re.match(email_pattern, email), "Email format is invalid"


profile_data = {
    "name": "NISMAL",
    "username": "nismal",
    "email": "nismal.m@edstem.com",
    "profile_url": "https://dev.pttapp.com/user-profile"
 }

expected_name = "NISMAL"
expected_username = "nismal"
expected_email = "nismal.m@edstem.com"
expected_profile_url = "https://dev.pttapp.com/user-profile"
validate_profile(profile_data, expected_name, expected_username, expected_email, expected_profile_url)
print("GOT ALL PROFILE DATA")



