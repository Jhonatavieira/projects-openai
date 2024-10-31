from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

story = """In a distant galaxy, there was a brave space explorer named Alex.
       Alex had spent years traveling through the cosmos,
       discovering new planets and meeting alien species. One fateful day,
       while exploring an uncharted asteroid belt,
       Alex stumbled upon a peculiar object that would change the course
       of their interstellar journey forever..."""


def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messagens=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content


prompt = f"Complete the story delimited by triple backticks ```{story}```"

response = get_response(prompt)
print("\n Original story", story)
print("\n Generated History", response)
