import json
import pandas as pd


def process_uploaded_file(uploaded_file):
    """Lê e interpreta o arquivo enviado, isolando a regra de negócio da interface UI."""
    main_type, sub_type = uploaded_file.type.split("/")

    match (main_type, sub_type):
        case ("text", "csv"):
            return "dataframe", pd.read_csv(uploaded_file)

        case ("text", "x-python"):
            return "code", uploaded_file.read().decode("utf-8")

        case ("application", "json"):
            return "json", json.loads(uploaded_file.read())

        case ("video", _):
            return "video", uploaded_file

        case ("audio", _):
            return "audio", uploaded_file

        case _:
            return "unsupported", None