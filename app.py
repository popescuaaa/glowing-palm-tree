from flask import Flask, request
from dotenv import load_dotenv
from api import api_method

""" Load .env file """
load_dotenv(
    dotenv_path='.env', verbose=True
)


""" Create Flask app """
app = Flask(__name__)


@app.route("/")
def health_check():
    return {"message": "Healthy"}


@app.route("/api/example", methods=['POST'])
def example():
    param = request.form['param']
    return api_method.api_method(param=param)


""" Run Flask app """
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
