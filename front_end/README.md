# streamlit directories

## The streamlit application:

- **app.py**: Streamlit app file. Streamlit app is located here.

## How to call api in the back_end
- **URL**: "http://back_end:5000/" + end_point
- **Example**: 
```python
import requests
response_packages = requests.post("http://back_end:5000/chat", data={"message": "Hello"})
message = response_packages.json()["message"]
```
- **Note that**: You must use data instead of json
```python
    response_packages = requests.post("http://back_end:5000/chat", data={"message": "Hello"})
    # instead of
    response_packages = requests.post("http://back_end:5000/chat", json={"message": "Hello"})
```
