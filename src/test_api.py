from api import client
# from pprint import pprint

# pprint(vars(client))
models = client.models.list()
for model in models:
    print(model.id)
