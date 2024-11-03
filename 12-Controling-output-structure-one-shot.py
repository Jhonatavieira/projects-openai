from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Function get response OPENAI


def get_response(prompty):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.0,
        massages=prompty,
        max_tokens=100,
    )
    return response


""" In this section, it's necessary to use the controlling output structure
    I'm using the technique ONE-SHOT,
    then I need provide one example to the model"""

prompt = """"
    Q: Extract the odd number from {1, 3, 7, 12, 19}.
    A: Odd number {1, 3, 7, 19}
    Q: Extract the odd number from {3, 5, 11, 12, 16}.
    A:
"""

response = get_response(prompt)
print(response)
