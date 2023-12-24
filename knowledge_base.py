```python
# Import necessary libraries
import json
import os

class KnowledgeBase:
    def __init__(self):
        # Load the knowledge bases for the different applications
        self.knowledge_bases = self.load_knowledge_bases()

    def load_knowledge_bases(self):
        # Initialize an empty dictionary to hold the knowledge bases
        knowledge_bases = {}

        # Get the list of knowledge base files
        kb_files = os.listdir('knowledge_bases')

        # Load each knowledge base
        for kb_file in kb_files:
            # Get the name of the application
            app_name = os.path.splitext(kb_file)[0]

            # Open the knowledge base file
            with open(f'knowledge_bases/{kb_file}', 'r') as f:
                # Load the knowledge base
                kb = json.load(f)

                # Add the knowledge base to the dictionary
                knowledge_bases[app_name] = kb

        return knowledge_bases

    def get_info(self, interpreted_query):
        # Initialize an empty dictionary to hold the information
        info = {}

        # Loop over each application in the knowledge base
        for app_name, kb in self.knowledge_bases.items():
            # Check if the interpreted query matches any of the entries in the knowledge base
            for entry in kb:
                if entry['query'] in interpreted_query:
                    # If it does, add the information to the dictionary
                    info[app_name] = entry['info']

        return info
```
