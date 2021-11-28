from flask import Response


def api_method(param: str):
    """
    This is a sample API method.
    """
    return Response(response="Hello World! I have received: {}!".format(param), status=200, mimetype="text/plain")
