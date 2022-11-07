import logging, json

import azure.functions as func
import requests

FILE_WATCHER_URL = 'http://localhost:7071/api/file-watcher'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Request with method {req.method} received.")
    try:
        if req.method == "POST":
            data = requests.post(FILE_WATCHER_URL, json=req.get_json())
        else:
            data = requests.get(FILE_WATCHER_URL)
        return func.HttpResponse(json.dumps(data.json()), headers={"content-type": "application/json"})
    except requests.exceptions.HTTPError as e:
        logging.error(e.response.text)
        return func.HttpResponse(json.dumps({"status": None, "message": e.response.text, "error": e.response.text}),
                                 headers={"content-type": "application/json"})
