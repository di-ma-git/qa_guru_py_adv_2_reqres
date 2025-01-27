import requests
import pytest

# https://reqres.in/api/users/2

# {
# "data": {
# "id": 2,
# "email": "janet.weaver@reqres.in",
# "first_name": "Janet",
# "last_name": "Weaver",
# "avatar": "https://reqres.in/img/faces/2-image.jpg"
# },
# "support": {
# "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
# "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
# }



@pytest.mark.parametrize("user_id, expected_email", [
    (2, "janet.weaver@reqres.in"),
])
def test_user_data(user_id, expected_email):
    # url = f"https://reqres.in/api/users/{user_id}"
    url = f"http://0.0.0.0:8000/api/users/{user_id}"

    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")
    assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"

    body = response.json()
    assert "data" in body, f"Response body does not contain 'data' key"

    data = body["data"]
    assert data["id"] == user_id, f"Expected id {user_id} but got {data['id']}"
    assert data["email"] == expected_email, f"Expected email {expected_email} but got {data['email']}"


# def test_user_data():
#     url = "https://reqres.in/api/users/2"
#     id = 2
#     email = "janet.weaver@reqres.in"
#
#     response = requests.get(url)
#     body = response.json()
#     data = body["data"]
#
#     assert data["id"] == id
#     assert data["email"] == email








