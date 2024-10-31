from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")


def get_response(self, prompt):
    response = client.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens="",
        prompt=prompt
    )
    return response


instructions = """Determine the language and generate a suitable title"""
format_output = """Separeta the text using the format
               'Text:'<the text> 
               'Language:'<the language>
               'Title:'<the title> 
               """

text = """Les noms sont presque toujours accompagnés d’un article
        ou d’un autre déterminant. Celui-ci indique le genre du nom
        (masculin ou féminin) et le nombre (singulier ou pluriel).
        Il y a des articles définis"""


prompt = instructions + format_output + f"```{text}```"

response = get_response(prompt)
