from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>",
                organization="",
                project="")

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    max_tokens=100,
    temperature=0.5,
    prompt="What is the openAi API?"

)
print(response)
print(response.choices[0].text)  # Extract text
print(response.usage)  # Extepend tokens
print(response.usage.total_tokens)  # Extract all tokens used
