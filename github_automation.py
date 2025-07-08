import requests
import base64

# GitHub credentials
TOKEN = 'Enter your token'
USERNAME = 'ShakirDev32'
REPO = 'Enter repository name'
FILEPATH = 'Path of a file'  # Local file path
TARGET_PATH = 'twhere to upload'   # Where to upload inside the repo
def upload_to_github():
    with open(FILEPATH, 'rb') as file:
        content = base64.b64encode(file.read()).decode('utf-8')

    url = f'https://api.github.com/repos/{USERNAME}/{REPO}/contents/{TARGET_PATH}'

    headers = {
        'Authorization': f'token {TOKEN}',
        'Content-Type': 'application/json'
}

    data = {
        'message': 'Added Python script for text-to-speech using pyttsx3',
        'content': content,
        'branch': 'main' # ✅ specifying branch is important
}

    response = requests.put(url, headers=headers, json=data)
    print("➡  Uploading to:", url)

     
    if response.status_code == 201:
        print("✅ File uploaded successfully!")
    else:
        print(f"❌ Upload failed: {response.status_code}\n{response.text}")
upload_to_github()
