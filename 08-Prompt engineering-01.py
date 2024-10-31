from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")


def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messanges=prompt
    )
    return response


# Prompt
conversation_messages = [
    {"role": "system", "content": "You are helpful event management assistant"},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": ""}
]

res = get_response(conversation_messages)
print(res.choices[0].message.content)
