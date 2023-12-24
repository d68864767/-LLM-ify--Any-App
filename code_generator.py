```python
# Import necessary libraries
from jinja2 import Environment, FileSystemLoader

class CodeGenerator:
    def __init__(self):
        # Load the templates for the different applications
        self.templates = self.load_templates()

    def load_templates(self):
        # Initialize an empty dictionary to hold the templates
        templates = {}

        # Get the list of template files
        template_files = os.listdir('templates')

        # Load each template
        for template_file in template_files:
            # Get the name of the application
            app_name = os.path.splitext(template_file)[0]

            # Create a new Jinja2 environment
            env = Environment(loader=FileSystemLoader('templates'))

            # Load the template
            template = env.get_template(template_file)

            # Add the template to the dictionary
            templates[app_name] = template

        return templates

    def generate_code(self, info):
        # Initialize an empty string to hold the generated code
        code = ''

        # Loop over each application in the info
        for app_name, app_info in info.items():
            # Get the template for the application
            template = self.templates.get(app_name)

            # If a template was found, render it with the app info
            if template:
                code += template.render(app_info)

        return code
```
