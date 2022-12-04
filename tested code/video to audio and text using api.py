import os
import sys
import requests
from time import sleep
from pprint import pprint

API_KEY = '0f41dfcd4ba447c1a5bba0acd51ab17e'
AUDIO_FILE = '1.mp4'
UPLOAD_ENDPOINT = 'https://api.assemblyai.com/v2/upload'
TRANSCRIPT_ENDPOINT = 'https://api.assemblyai.com/v2/transcript'
OUTPUT_TRANSCRIPT_FILE = '1.txt'


def read_audio_file(file):
    """Helper method that reads in audio files"""
    with open(file, 'rb') as f:
        while True:
            data = f.read(5242880)
            if not data:
                break
            yield data


headers = {
    'authorization': API_KEY,
    'content-type': 'application/json'
}

res_upload = requests.post(
    UPLOAD_ENDPOINT,
    headers=headers,
    data=read_audio_file(AUDIO_FILE)
)
pprint(res_upload.json())
upload_url = res_upload.json()['upload_url']

res_transcript = requests.post(
    TRANSCRIPT_ENDPOINT,
    headers=headers,
    json={
        'audio_url': upload_url,
        'content_safety': True,
    },
)
res_transcript_json = res_transcript.json()
pprint(res_transcript_json)

status = ''
while status != 'completed':
    res_result = requests.get(
        os.path.join(TRANSCRIPT_ENDPOINT +'/', res_transcript_json['id']),
        headers=headers
    )
    status = res_result.json()['status']
    print(f'Status: {status}')

    if status == 'error':
        sys.exit('Audio file failed to process.')
    elif status != 'completed':
        sleep(10)
pprint(res_result.json())

with open(OUTPUT_TRANSCRIPT_FILE, 'w') as f:
    f.write(res_result.json()['text'])

print(f'Transcript file saved under {OUTPUT_TRANSCRIPT_FILE}')