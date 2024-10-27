from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

audio_file = open("audio.m4a", "rb")

# Create a transcription from the audio_file
response = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file
)
print(response.text)
