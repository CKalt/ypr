import yaml
import json
import sys

def parse_yaml(yaml_file):
    # Parse the YAML file
    with open(yaml_file, 'r') as file:
        yaml_content = yaml.safe_load(file)

    # Extract file paths for Rust and Python
    rust_files = []
    python_files = []

    for module in yaml_content['modules']:
        for language in module['language-specific']:
            for lang, details in language.items():
                if lang == 'rust':
                    for detail in details:
                        if 'filename' in detail:
                            rust_files.append(detail['filename'])
                elif lang == 'python':
                    for detail in details:
                        if 'filename' in detail:
                            python_files.append(detail['filename'])

    # Prepare the final JSON object
    final_json = {
        "rust": rust_files,
        "python": python_files
    }

    return final_json

def write_json(json_content, json_file):
    # Write the JSON file
    with open(json_file, 'w') as file:
        json.dump(json_content, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file.yaml>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = "output.json"

    json_content = parse_yaml(input_file)
    write_json(json_content, output_file)
