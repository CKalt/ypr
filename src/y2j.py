import yaml
import json
import sys

def convert_yaml_to_json(yaml_file, json_file):
    try:
        with open(yaml_file, 'r') as f:
            yaml_data = f.read()
            json_data = json.dumps(yaml.safe_load(yaml_data), indent=4)

        with open(json_file, 'w') as f:
            f.write(json_data)

        print("Conversion successful!")
    except yaml.YAMLError as e:
        print("Error while converting YAML to JSON:", str(e))
    except FileNotFoundError as e:
        print("File not found:", str(e))
    except IOError as e:
        print("Error while reading/writing the file:", str(e))

# Example usage
if len(sys.argv) != 3:
    print("Usage: python yaml_to_json.py <input_yaml_file> <output_json_file>")
else:
    input_yaml_file = sys.argv[1]
    output_json_file = sys.argv[2]
    convert_yaml_to_json(input_yaml_file, output_json_file)
