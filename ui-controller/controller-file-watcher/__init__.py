import json

import azure.functions as func
import requests

from ..helpers.FileWatcherServer import *


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Request with method {req.method} received.")
    try:
        if req.method == "POST":
            action = req.get_json()["action"]
            if action == "start":
                status = start_file_watcher()
                return func.HttpResponse(json.dumps({"status": status.lower(), "message": None, "error": None}))
            elif action == "stop":
                status = stop_file_watcher()
                return func.HttpResponse(json.dumps({"status": status.lower(), "message": None, "error": None}))
            else:
                # defaults to check status
                status = get_file_watcher_status()
                return func.HttpResponse(json.dumps({"status": status.lower(), "message": None, "error": None}))
        else:
            # defaults to check status
            status = get_file_watcher_status()
            return func.HttpResponse(json.dumps({"status": status.lower(), "message": None, "error": None}))
    except requests.exceptions.HTTPError as e:
        logging.error(e.response.text)
        return func.HttpResponse(json.dumps({"status": None, "message": e.response.text, "error": e.response.text}),
                                 headers={"content-type": "application/json"})
    except subprocess.CalledProcessError as cpe:
        logging.error(f"Error has occurred: {cpe}")
        return func.HttpResponse(json.dumps(
            {"status": None, "message": f"{req.get_json()['action']} file watcher has encountered issue",
             "error": "UnexpectedServerError"}),
                                 headers={"content-type": "application/json"})
    except Exception as e:
        logging.error(f"Caught an exception: {e}")
        logging.error(f"Error has occurred: {e}")
        return func.HttpResponse(json.dumps(
            {"status": None, "message": "Unexpected error has occurred",
             "error": "UnexpectedServerError"}),
            headers={"content-type": "application/json"})
