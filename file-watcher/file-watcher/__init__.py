import json
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    action_name = req.params.get('action')
    if not action_name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            action_name = req_body.get('action')

    if action_name == "start":
        return func.HttpResponse(json.dumps({ "status": "running", "message": None, "error": None }))
    elif action_name == "stop": 
        return func.HttpResponse(json.dumps({ "status": "stopped", "message": None, "error": None }))
    else:
        return func.HttpResponse(json.dumps({ "status": "running", "message": None, "error": None }))
