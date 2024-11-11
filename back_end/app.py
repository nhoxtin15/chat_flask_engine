from flask import Flask, render_template, request
from chat_engine import *
app = Flask(__name__)


#api here

@app.route('/chat', methods=['POST'])
def chat():
    """
    This function is called when the user sends a message to the chatbot.
    :param: {
    - message: str
    }
    :return: {
        message: str,
        status: int
    }
    """
    message = request.form['message']

    #return json
    return {"message": demo.foo(message), "status": 200}





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)