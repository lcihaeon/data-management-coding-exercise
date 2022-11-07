import logging, json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )

    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
    except ValueError:
        pass

    logging.info(req_body)

    if isinstance(req_body, list) and len(req_body) > 0:
        # TODO: deal with len > 2
        data = { "valid": True, "message": None, "error": None }

    # data = add_todos(req_body.get('task'))
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
