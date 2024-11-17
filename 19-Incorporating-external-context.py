client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = """You are a customer service chatbot for MyPersonalDelivery,
                a delivery service that offers a wide range of delivery options
                for various items. You should respond to user queries in a gentle way."""

context_question = """What types of items can be delivered 
                    using MyPersonalDelivery?"""
context_answer = """We deliver everything from everyday essentials such as groceries,
                 medications, and documents to larger items like electronics, clothing,
                 and furniture. However, please note that we currently do not offer
                 delivery for hazardous materials or extremely 
                 ragile items requiring special handling."""

# Add the context to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system_prompt},
              {"role": "user", "content": context_question},
              {"role": "assistant", "content": context_answer},
              {"role": "user", "content": "Do you deliver furniture?"}])
response = response.choices[0].message.content
print(response)
