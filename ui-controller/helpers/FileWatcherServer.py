import subprocess, logging

FILE_WATCHER_URL = 'http://localhost:7071/api/file-watcher'
AZ_FUNCTION_NAME = 'GLFileWatcher'
AZ_RESOURCE_GROUP = 'glfilewatcher'
AZ_SUBSCRIPTION = '708036b4-934d-4b70-bf81-7bd4e72ac862'

# TODO: replace with python SDK APIs instead of using azure cli

def get_file_watcher_status():
    cmd = f"az functionapp show --name {AZ_FUNCTION_NAME} --resource-group {AZ_RESOURCE_GROUP} --subscription {AZ_SUBSCRIPTION} --query state"
    status = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    logging.info(f"status: {status.decode('utf-8').strip()}")
    return status.decode('utf-8').strip().replace('"', '')  # "Running", "Stopped"


def start_file_watcher():
    cmd = f"az functionapp start --name {AZ_FUNCTION_NAME} --resource-group {AZ_RESOURCE_GROUP} --subscription {AZ_SUBSCRIPTION}"
    comp_proc = subprocess.run(cmd, shell=True)
    if comp_proc.returncode == 0:
        return "running"
    return "error"


def stop_file_watcher():
    cmd = f"az functionapp stop --name {AZ_FUNCTION_NAME} --resource-group {AZ_RESOURCE_GROUP} --subscription {AZ_SUBSCRIPTION}"
    comp_proc = subprocess.run(cmd, shell=True)
    if comp_proc.returncode == 0:
        return "stopped"
    return "error"
