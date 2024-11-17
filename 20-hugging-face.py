""" todo
    docstring
"""
from huggingface_hub import HfApi
from transformers import AutoModel


# Create the instance of the API
api = HfApi()

# Return the filtered list from the Hub
models = api.list_models(
    filter=ModelFilter(
        task="text-classification"),
    sort="downloads",
    direction=-1,
    limit=5
)

# Store as a list
modelList = list(api.list_models())

print(modelList[0].modelId)

MODEL_ID = "distilbert-base-uncased-finetuned-sst-2-english"

# Instantiate the AutoModel class
model = AutoModel.from_pretrained(MODEL_ID)

# Save the model
model.save_pretrained(save_direction=f"models/{MODEL_ID}")
