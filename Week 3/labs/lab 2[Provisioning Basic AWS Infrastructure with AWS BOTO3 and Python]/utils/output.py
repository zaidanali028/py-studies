# utils/outputs.py
from typing import Dict

# print resources outpus
def print_resource_outputs(resources: Dict[str, str]) -> None:
    for resource_name, resource_value in resources.items():
        print(f"{resource_name}: {resource_value}")