from openai import OpenAI

client = OpenAI(api_key="<OPEN_AI_TOKEN>")

# Create a request to CHAT completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=150,
    messages=[
        {"role": "system",
         "content": "You are a helpful data science tutor."},
        {"role": "user",
         "content": "What is the difference between a for loop and while loop?"
         }
    ]
)

# Extract and print the assistent's text response
print(response.choices[0].message.content)
