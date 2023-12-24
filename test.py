```python
# Import necessary libraries
import unittest
import json
from main import app

class TestLLMify(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()

    def test_generate_code(self):
        # Define a test query
        test_query = 'Create a new table in NocoDB'

        # Send a POST request to the /generate endpoint
        response = self.app.post('/generate', json={'query': test_query})

        # Parse the response
        response_data = json.loads(response.data)

        # Check that the response has a 'code' key
        self.assertIn('code', response_data)

        # Check that the generated code is not empty
        self.assertNotEqual(response_data['code'], '')

if __name__ == '__main__':
    # Run the tests
    unittest.main()
```
