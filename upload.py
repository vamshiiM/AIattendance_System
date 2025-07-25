import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Define the required variables
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'trans-shuttle-434103-k2-005ddfae3887.json'
PARENT_FOLDER_ID = "1v-pT76VObBJWj5f-7lfeNW0nMsI5nnvq"


def authenticate():
    # Authenticate using the service account file
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds


def upload_photo(file_path):
    # Authenticate and build the service
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    # Define the file metadata
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [PARENT_FOLDER_ID],
    }

    # Create MediaFileUpload object
    media = MediaFileUpload(file_path, resumable=True)

    try:
        # Upload the file
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        print(f'File ID: {file.get("id")}')

    except Exception as e:
        print(f'An error occurred: {e}')


# Path to the file you want to upload
upload_photo("tr.jpg")