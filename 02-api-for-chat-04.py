from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")


messages = [{"role": "system", "content": "You are a helpful math tutor."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

for q in user_msgs:
    print("User: ", q)

    # Create a dictionary for the user massage from q and append to massages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)

    # API request
    response = client.chat.completions.create(
        modul="gpt-4o-mini",
        max_tokens=100,
        messages=messages,
    )
    # Convert the assistant's massage to a dict and append to messages
    assistant_dict = {"role": "assistant",
                      "content": response.choices[0].message.content}

    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")
