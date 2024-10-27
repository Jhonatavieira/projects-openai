from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

instruction = """
import numpy as np

heights_dict = {"Mark": 1.76, "Steve": 1.88, "Adnan":1.73}
heights = heights_dict.values()
print(np.mean(heights))
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=100,
    messages=[
        {"role": "system",
         "content": "Explain what this Python code does in one sentence?"
         },
        {"role": "user",
         "content": instruction
         }
    ]
)

# print the assistent response
response.choices[0].message.content
