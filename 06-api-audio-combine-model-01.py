from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

audio_file = open("audio.m4a", "rb")

# White an appropriate prompt to help the model
prompt = "This audio is about recent World bank report"

response = client.audio.translations.create(
    model="whisper-1",
    file=audio_file,
    prompt=prompt

)
print(response.text)
