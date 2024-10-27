from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

audio_file = open("audio.wav", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

audio_transcription = "What is text language? " + audio_response.text

# Create a request to the API to identify the language spoken
chat_response = client.chat.completions.create(
    model="whisper-1",
    prompt=audio_transcription
)
print(chat_response.choices[0].message.content)
