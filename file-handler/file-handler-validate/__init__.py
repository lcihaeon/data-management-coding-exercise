import logging

import azure.functions as func
from ..helpers.FileParser import *


def main(req: func.HttpRequest, transferblob: func.InputStream) -> func.HttpResponse:

    # This function is triggered when a queue message is present

    # Step 1: Download file if not present

    # Step 2: Determine file type. If type is not (M|D|H|P), record an error
    # with open('../test/DentalClaims.trg') as test_file:
    with open('./tests/DentalClaims.csv') as test_file:
        f_type = get_file_type(test_file)

    # Step 3: Validate file Integrity, could use http call to perform the action
    # validate_integrity(data_files)

    # Step 4: Validate file completeness, could use http call to perform the action
    # validate_completeness(data_files)

    # Step 5: Copy file from transfer to staging container, delete from transfer container

    return func.HttpResponse(
        "Files are validate",
        status_code=200
    )
