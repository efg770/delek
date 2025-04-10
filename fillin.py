import webbrowser
import urllib.parse

# Base URL of the form
base_url = "https://efg770.github.io"

# Data to fill in the form
form_data = {
    "delek1": "025566998",
    "delek2": "0585551234"
}

# Encode the data as query parameters
query_string = urllib.parse.urlencode(form_data)

# Construct the full URL with query parameters
full_url = f"{base_url}?{query_string}"

# Open the URL in the default web browser
webbrowser.open(full_url)

print("Opened URL:", full_url)