import json
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Request with method {req.method} received.")
    if req.method == "POST":
        action = req.get_json()["action"]
        if action == "start":
            return func.HttpResponse(json.dumps({"status": "running", "message": None, "error": None}))
        elif action == "stop":
            return func.HttpResponse(json.dumps({"status": "stopped", "message": None, "error": None}))
        else:
            # defaults to check status
            return func.HttpResponse(json.dumps({"status": "running", "message": None, "error": None}))
    else:
        # defaults to check status
        return func.HttpResponse(json.dumps({"status": "running", "message": None, "error": None}))
