import os
import yaml

def create_files(data, base_path="."):
    # Open file for writing directory structure layout
    with open(os.path.join(base_path, "dir_structure.txt"), "w") as layout:
        for module in data["modules"]:
            for lang_spec in module["language-specific"]:
                language = lang_spec["language"]
                if language in ["python", "rust"]:
                    # Construct file path
                    file_path = os.path.join(base_path, language, lang_spec["filename"])
                    
                    # Create directory if it does not exist
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    
                    # Write directory structure to layout file
                    layout.write(file_path + "\n")
                    
                    # Create and write to file
                    with open(file_path, "w") as f:
                        f.write("# {}\n".format(file_path)) # write file name as a comment

def read_yaml_and_create_files(yaml_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
        create_files(data)

read_yaml_and_create_files('P1.yaml')
