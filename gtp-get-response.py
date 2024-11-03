# from openai import OpenAI

# ChatGPT get response


class ChatGptConn:
    def __init__(self, prompts, generate, end_point):
        self.prompts = prompts,
        self.generate = generate,
        self.end_point = end_point


"""
    This function provide the chatgpt response and this
    function is pattern for all python modules

    Arg:
        prompt: "recive the prompts"
        func: "recive the type of model"
        endpoint: "chatgtp and point"
"""


# def get_response(self):
#     client = OpenAI(api_key="<OPENAI_API_KEY>")

#     response = f"Client.{self.generate}.completions.create"(
#         "model = {self.end_point}",

#     )
