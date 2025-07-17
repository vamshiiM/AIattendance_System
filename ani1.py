from google.oauth2 import id_token
from google.auth.transport import requests

# Replace 'YOUR_CLIENT_ID' with your actual client ID obtained from Google Cloud Console
CLIENT_ID = 'YOUR_CLIENT_ID'


def verify_google_token(token):
    try:
        # Specify your client ID in the 'audience' parameter
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), audience=CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Invalid issuer.')

        # User's email address
        email = idinfo['email']

        # User's unique Google ID
        google_id = idinfo['sub']

        return {'email': email, 'google_id': google_id}
    except ValueError as e:
        print(str(e))
        return None


# Example usage:
token = 'YOUR_ID_TOKEN'  # Replace with the actual ID token obtained during authentication
user_info = verify_google_token(token)

if user_info:
    print("Authentication successful!")
    print("Email:", user_info['email'])
    print("Google ID:", user_info['google_id'])
else:
    print("Authentication failed.")
