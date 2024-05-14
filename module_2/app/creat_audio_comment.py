import requests


def audio_comm(comment):
    API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-rus"
    headers = {"Authorization": f"Bearer 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"}


    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content


    audio_bytes = query({
        "inputs": comment,
    })
    # You can access the audio with IPython.display for example
    return audio_bytes
    #with open('myfile.wav', mode='bx') as f:
    #    f.write(audio_bytes)