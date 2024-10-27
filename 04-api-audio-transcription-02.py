from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

audio_file = open("audio.a4m", "rb")  # Read binary

response = client.audio.transcriptions.create(
    model='whisper-1', file=audio_file
)
print(response.text)
