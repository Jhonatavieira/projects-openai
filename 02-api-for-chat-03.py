from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens="",
    messages=[
        {"role": "system",
         "content": "You are a helpful Python programming tutor"},
        {"role": "user",
         "content": "What is lower() in Python?"},
        {"role": "assistant",
            "content": "You can use def keyword def and put the instructions"},
        {"role": "user",
         "content": "Explain what the type() function does."}
    ]

)
print(response.choices[0].massage.content)
