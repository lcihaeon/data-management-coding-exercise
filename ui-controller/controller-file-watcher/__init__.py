import logging, json

import azure.functions as func
import requests, subprocess
import pdb

FILE_WATCHER_URL = 'http://localhost:7071/api/file-watcher'
AZ_FUNCTION_NAME = 'GLFileWatcher'
AZ_RESOURCE_GROUP = 'glfilewatcher'
AZ_SUBSCRIPTION = '708036b4-934d-4b70-bf81-7bd4e72ac862'


def get_file_watcher_status():
    cmd = f"az functionapp show --name {AZ_FUNCTION_NAME} --resource-group {AZ_RESOURCE_GROUP} --subscription {AZ_SUBSCRIPTION} --query state"
    status = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    # pdb.set_trace()
    logging.info(f"status: {status.decode('utf-8').strip()}")
    return status.decode('utf-8').strip().replace('"', '')  # "Running", "Stopped"
    # return "Running"  # "Running", "Stopped"


def start_file_watcher():
    cmd = f"az functionapp start --name {AZ_FUNCTION_NAME} --resource-group {AZ_RESOURCE_GROUP} --subscription {AZ_SUBSCRIPTION}"
    comp_proc = subprocess.run(cmd, shell=True)
    if comp_proc.returncode == 0:
        return "running"
    return "error"
    # pdb.set_trace()


def stop_file_watcher():
    cmd = f"az functionapp stop --name {AZ_FUNCTION_NAME} --resource-group {AZ_RESOURCE_GROUP} --subscription {AZ_SUBSCRIPTION}"
    comp_proc = subprocess.run(cmd, shell=True)
    if comp_proc.returncode == 0:
        return "stopped"
    return "error"
    # pdb.set_trace()


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Request with method {req.method} received.")
    try:
        # if req.method == "POST":
        #     data = requests.post(FILE_WATCHER_URL, json=req.get_json())
        # else:
        #     data = requests.get(FILE_WATCHER_URL)
        # return func.HttpResponse(json.dumps(data.json()), headers={"content-type": "application/json"})
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
