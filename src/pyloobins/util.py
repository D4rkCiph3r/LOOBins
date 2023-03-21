"""Utility functions that support the CLI and library"""
from datetime import date
import yaml
from .models import LOOBin, Functions, ShellCls, FullPath, Detection, ExternalReference


def validate_loobin(yml_path: str) -> bool:
    """Validates LOOBin YAML file"""
    with open(yml_path, "r", encoding="utf-8") as stream:
        try:
            yml_content = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    try:
        LOOBin(**yml_content) # type: ignore
        return True
    except Exception as exc:
        # TODO add more specific Exception handling
        print(exc)
        return False


def make_template() -> LOOBin:
    """Creates a template LOOBin object"""
    loobin_template = LOOBin(
        Name="Template",
        Description="A short description of the binary goes here.",
        Author="Enter your name or alias here.",
        Created=date.today(),
        Functions=Functions(Shell=ShellCls(Code="Code here.")),
        Full_Path=[FullPath(Path="/enter/binary/path/here")],
        Detections=[
            Detection(
                Source="A detection source (e.g. Sigma)",
                URL="https://urltodetection.here",
            )
        ],
        External_References=[
            ExternalReference(
                Name="Name of external reference.",
                URL="https://urlofexternalreference.here",
            )
        ],
    )
    return loobin_template

def normalize_file_name(title: str)->str:
    """Accepts a binary title and normalizes it for the file name"""
    return title.lower().replace(" ","_")
