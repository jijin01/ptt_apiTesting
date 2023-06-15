import login
import requests
import re
profile_url = "https://dev.pttapp.com/user-profile"  # Replace with the actual profile URL


def validate_profile(profile_data, expected_name, expected_username, expected_email, expected_profile_url):
    # Extract profile information from the data
    avatar = profile_data["avatar"]
    name = profile_data["name"]
    username = profile_data["username"]
    email = profile_data["email"]
    profile_url = profile_data["profile_url"]

    # Validate profile picture URL
    response = requests.get(avatar)
    assert response.status_code == 200, "Profile picture URL is invalid"

    # Validate name, username, email, and profile URL
    assert name == expected_name, f"Name assertion failed. Expected: {expected_name}, Actual: {name}"
    assert username == expected_username, f"Username assertion failed. Expected: {expected_username}, Actual: {username}"
    assert email == expected_email, f"Email assertion failed. Expected: {expected_email}, Actual: {email}"
    assert profile_url == expected_profile_url, f"Profile URL assertion failed. Expected: {expected_profile_url}, Actual: {profile_url}"

    # Validate email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    assert re.match(email_pattern, email), "Email format is invalid"

    # Additional validations...
    # Add your desired additional validations here

# Example profile data
profile_data = {
    "avatar": "https://dev.pttapp.com/static/media/profile_pic.9999920b.webp",
    "name": "NISMAL",
    "username": "nismal",
    "email": "nismal.m@edstem.com",
    "profile_url": "https://dev.pttapp.com/user-profile"
 }

# Define the expected data
expected_name = "NISMAL"
expected_username = "nismal"
expected_email = "nismal.m@edstem.com"
expected_profile_url = "https://dev.pttapp.com/user-profile"

# Validate the profile page
validate_profile(profile_data, expected_name, expected_username, expected_email, expected_profile_url)



