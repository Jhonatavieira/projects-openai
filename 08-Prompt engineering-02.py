from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")


def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messagens=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content


res = get_response("Write a poem about ChatGPT")
print(res)
