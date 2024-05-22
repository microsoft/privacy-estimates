from mldesigner import command_component, Input, Output
from datasets import Dataset
from pathlib import Path


@command_component(environment="environment.aml.yaml")
def convert_jsonl_to_hfd(data: Input(type="uri_file"), output: Output(type="uri_folder")):
    """
    Convert a JSONL file to a Hugging Face dataset.
    """
    path = Path(data)
    if path.is_file():
        paths = [path]
    else:
        paths = list(path.glob("*.jsonl")) + list(path.glob("*.json"))
    paths = [str(p) for p in paths]
    Dataset.from_json(paths).save_to_disk(output)


@command_component(environment="environment.aml.yaml")
def convert_hfd_to_jsonl(data: Input(type="uri_folder"), output: Output(type="uri_file")):
    """
    Convert a Hugging Face dataset to a JSONL file.
    """
    Dataset.load_from_disk(data).to_json(output)
