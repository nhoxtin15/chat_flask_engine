# This is directories for flask back end
## Directories:
- app.py: Flask app file. API endpoint is located here.
- chat_engine: Put the python logic code in the chat_engine directory.
## app.py
This is the main file for the flask app. API endpoint is located here.
### endpoint format:
- /api/chat: POST request. It takes the following json format:
```json
{
    "message": "Hello"
}
```
- format to call:
```python
import requests
response = requests.post("http://back_end:5000/chat", data={"message": "Hello"})
message = response.json()["message"]
```
- response format:
```json
{
    "message": "Hello",
    "status" : 200,
}
```
- status: 200 for success and 400 for failure.

### chat engine
- **Step 1**: Put your python file in the chat_engine directory.
- **Step 2**: Import the python file in the __init__.py
- **Step 3**: Call the function in the app.py file.
- **Note that**: The path should be in the python module format (Take example in demo.py and function calling in app.py file



