import requests

# URL of the form's action endpoint
url = "https://efg770.github.io/index.html"

# Data to fill in the form
form_data = {
    "delek1": "Value for delek1",
    "delek2": "Value for delek2"
}

# Send a POST request with the form data
response = requests.post(url, data=form_data)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response Text:", response.text)