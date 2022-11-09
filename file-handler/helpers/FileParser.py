TRIGGER = "TRG"
MEDICAL = "M"
DENTAL = "D"
HOSPITAL = "H"
PRESCRIPTION = "P"

## File Types
file_types = {
    "trigger": {
        "type_id": "TRG",
        "key": [],
        "header": [
            "Data File Name",
            "File Type",
            "Record Count",
            "Checksum"
        ],
        "data": [
            {"name": "Data File Name", "type": "string", "required": True},
            {"name": "File Type", "type": "string", "required": True},
            {"name": "Record Count", "type": "numeric", "required": True},
            {"name": "Checksum", "type": "string", "required": True}
        ]
    },
    "medical": {
        "type_id": "M",
        "key": ["ClaimNumber", "PatientId", "ProviderId", "ProcedureDate", "ProcedureCode"],
        "header": ["ClaimType", "ClaimNumber", "ClaimDate", "PatientId", "ProviderId", "ClaimAmount",
                   "ProcedureDate", "ProcedureCode"],
        "data": [
            {"name": "ClaimType", "type": "string", "required": True},
            {"name": "ClaimNumber", "type": "numeric", "required": True},
            {"name": "ClaimDate", "type": "date", "required": True},
            {"name": "PatientId", "type": "numeric", "required": True},
            {"name": "ProviderId", "type": "numeric", "required": True},
            {"name": "ClaimAmount", "type": "numeric", "required": True},
            {"name": "ProcedureDate", "type": "date", "required": True},
            {"name": "ProcedureCode", "type": "string", "required": True}
        ]
    },
    "dental": {
        "type_id": "D",
        "key": ["ClaimNumber", "PatientId", "ProviderId", "ProcedureDate", "ProcedureCode"],
        "header": ["ClaimType", "ClaimNumber", "ClaimDate", "PatientId", "ProviderId", "ClaimAmount",
                   "ProcedureDate", "ProcedureCode"],
        "data": [
            {"name": "ClaimType", "type": "string", "required": True},
            {"name": "ClaimNumber", "type": "numeric", "required": True},
            {"name": "ClaimDate", "type": "date", "required": True},
            {"name": "PatientId", "type": "numeric", "required": True},
            {"name": "ProviderId", "type": "numeric", "required": True},
            {"name": "ClaimAmount", "type": "numeric", "required": True},
            {"name": "ProcedureDate", "type": "date", "required": True},
            {"name": "ProcedureCode", "type": "string", "required": True}
        ]
    },
    "hospital": {
        "type_id": "H",
        "key": ["ClaimNumber", "PatientId", "ProviderId", "ProcedureDate", "ProcedureCode"],
        "header": ["ClaimType", "ClaimNumber", "ClaimDate", "PatientId", "ProviderId", "ClaimAmount",
                   "ProcedureDate", "ProcedureCode"],
        "data": [
            {"name": "ClaimType", "type": "string", "required": True},
            {"name": "ClaimNumber", "type": "numeric", "required": True},
            {"name": "ClaimDate", "type": "date", "required": True},
            {"name": "PatientId", "type": "numeric", "required": True},
            {"name": "ProviderId", "type": "numeric", "required": True},
            {"name": "ClaimAmount", "type": "numeric", "required": True},
            {"name": "ProcedureDate", "type": "date", "required": True},
            {"name": "ProcedureCode", "type": "string", "required": True}
        ]
    },
    "prescription": {
        "type_id": "P",
        "key": ["ClaimNumber", "PatientId", "ProviderId", "ProcedureDate", "ProcedureCode"],
        "header": ["ClaimType", "ClaimNumber", "ClaimDate", "PatientId", "ProviderId", "ClaimAmount", "DrugId"],
        "data": [
            {"name": "ClaimType", "type": "string", "required": True},
            {"name": "ClaimNumber", "type": "numeric", "required": True},
            {"name": "ClaimDate", "type": "date", "required": True},
            {"name": "PatientId", "type": "numeric", "required": True},
            {"name": "ProviderId", "type": "numeric", "required": True},
            {"name": "ClaimAmount", "type": "numeric", "required": True},
            {"name": "DrugId", "type": "numeric", "required": True}
        ]
    }
}


def get_file_type(file):
    return TRIGGER


def get_data_file_meta(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        if len(lines) >= 2:
            return lines[1].split('|')
        return None
