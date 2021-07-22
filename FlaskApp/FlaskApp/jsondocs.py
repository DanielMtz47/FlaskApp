import os
import json

root_path = os.getcwd()

json_path = os.path.join(root_path, "jsondocs")

docs = os.listdir(json_path)
# list containing all the names of the json docs
keyword = "subnet, SKU, "

# iterate the list of docs
for doc in docs:
    doc_path = os.path.join(json_path, doc)
    # open the json doc and load its content with json.load(file)
    with open(doc_path, 'r') as f:
        jsdoc = json.load(f)

        # Represent the content of the json as a string
        jsdoct_str = json.dumps(jsdoc, indent=2)
        # search for a keyword on a doc
        if(keyword in jsdoct_str):
            print(f"keyword '{keyword}' in {doc}")




