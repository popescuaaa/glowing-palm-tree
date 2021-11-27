import json
import os
from flask import jsonify
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.api import plaid_api
from dotenv import load_dotenv
import plaid


access_token = None


def exchange_token(public_token: str, client: plaid_api.PlaidApi):
    global access_token
    try:
        exchange_request = ItemPublicTokenExchangeRequest(
            public_token=public_token)
        exchange_response = client.item_public_token_exchange(exchange_request)
        access_token = exchange_response['access_token']
        item_id = exchange_response['item_id']
        return jsonify(exchange_response.to_dict())
    except plaid.ApiException as e:
        return json.loads(e.body)


if __name__ == '__main__':
    exchange_token('public_token')
    print(access_token)
    print(type(access_token))
