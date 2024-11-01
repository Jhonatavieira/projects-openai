# Start your code here!
import os
from openai import OpenAI

# Define the client
client = OpenAI(api_key=os.environ["OPENAI"])

conversation = [
    {
        "role": "system",
        "content": "You are tour guide in Paris,"
        "your resposible to provide all"
        "information about the romantic places,"
        "give the turist detalls about the place",
    },
    {
        "role": "user",
        "content": "What's the best romantic place in Paris to date",
    },
    {
        "role": "assistant",
        "content": "The most romantic place in Paris is Luxembourg Gardens",
    },
]

questions = [
    "What's the best romantiplace to visite in Paris?",
    "What's the famous restaurante in Paris?",
    "Where are I can met people in Paris?"
    "How much cost to visit different places in Paris?"
]


def get_response(prompt):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.0,
        prompt=prompt
    )
    return response


if __name__ == "__main__":
    for question in questions:
        input_dict = {"role": "user", "content": question}
        conversation.append(input_dict)
        response = get_response(input_dict)
        resp = response.choices[0].messange.content
        print(resp)
        resp_assistant = {"role": "assistant", "content": resp}
        conversation.append(resp_assistant)
