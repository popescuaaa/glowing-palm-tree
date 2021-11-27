from flask import Flask, request, jsonify, Response
from api import exchange, query, account
from plaid.api import plaid_api
from dotenv import load_dotenv
import plaid
import flask
import os


app = Flask(__name__)


"""
 Plaid API client 
"""

load_dotenv(
    dotenv_path=".env", verbose=True
)

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': os.getenv('PLAID_CLIENT_ID'),
        'secret': os.getenv('PLAID_SECRET'),
        'plaidVersion': '2020-09-14'
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)


@app.route("/")
def health_check():
    return {"message": "Healthy"}


@app.route("/api/exchange", methods=['POST'])
def exchange():
    """
    - Allowed Methods: POST
    - Takes a json body with a Plaid public_token and exchanges it for an
    access_token, which you should store in memory
    - Example body: {“public_token”: “<public_token>”}
    - Returns a 201 status code and nothing else.
    - Plaid’s documentation on the exchange endpoint
    """
    public_token = request.form['public_token']
    print(public_token)
    return Response(status=201)


@app.route("/api/query", methods=['POST'])
def query():
    """
    - Allowed Methods: POST
    - Takes no body, but initiates the API to query the Plaid investment endpoint for
    investments and transactions data for the stored public_token. Store the results
    in memory.
    - If called before “/exchange”, returns a 404
    - Returns a 201 status code and nothing else.
    - Plaid’s documentation on the investments endpoints.
    """
    data = request.get_json()
    return jsonify(data)


@app.route("/api/account", methods=['GET'])
def account():
    """
    - Allowed Methods: GET
    - Returns a 200 status code and a json body with the stored account data.
    - If called before “/query”, returns a 404
    - Returns a 200 status code and a json body with the stored account data.
    """
    data = request.get_json()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
