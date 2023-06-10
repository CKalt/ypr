import sys
import yaml
import jsonschema
import json

def validate_yaml(yaml_data, schema_data):
    try:
        yaml_object = yaml.safe_load(yaml_data)
        jsonschema.validate(yaml_object, schema_data)
        print("YAML document is valid against the schema.")
    except jsonschema.ValidationError as e:
        print(f"YAML document is not valid against the schema. Error: {e}")
    except yaml.YAMLError as e:
        print(f"Error while parsing YAML document: {e}")

def print_usage():
    print("Usage: python validate_yaml.py <schema_file> <yaml_file>")

# Check if the script is called with the correct arguments
if len(sys.argv) != 3:
    print_usage()
else:
    # Load the JSON schema
    schema_file = sys.argv[1]
    with open(schema_file, "r") as schema_file:
        schema_data = json.load(schema_file)

    # Load the YAML document
    yaml_file = sys.argv[2]
    with open(yaml_file, "r") as yaml_file:
        yaml_data = yaml_file.read()

    # Validate the YAML document against the JSON schema
    validate_yaml(yaml_data, schema_data)
