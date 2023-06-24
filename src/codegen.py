import yaml
import os
import sys

def create_project_skeleton(config_file):
    with open(config_file, 'r') as ypr_file:
        config = yaml.safe_load(ypr_file)

    # Get project name from the file name
    project_name = os.path.splitext(os.path.basename(config_file))[0]

    # Check if project directory already exists
    if os.path.exists(project_name):
        print(f"Error: Directory '{project_name}' already exists.")
        sys.exit(1)
    
    # Create project directory
    os.makedirs(project_name)

    # According to P1.ypr, structure always has the project name as the first key
    project_structure = config.get('structure', {}).get(project_name, [])
    
    # For each language or project file in the structure
    for structure_item in project_structure:
        # If the item is a string, it's a file, simply create it
        if isinstance(structure_item, str):
            with open(f'{project_name}/{structure_item}', 'w') as f:
                pass  # replace with actual file content generation
        # If the item is a dictionary, it's a language
        elif isinstance(structure_item, dict):
            for language, language_files in structure_item.items():
                # Create language directory
                os.makedirs(f'{project_name}/{language}')
                # For each file or directory in the language
                for language_file in language_files:
                    # If the item is a string, it's a file, simply create it
                    if isinstance(language_file, str):
                        with open(f'{project_name}/{language}/{language_file}', 'w') as f:
                            pass  # replace with actual file content generation
                    # If the item is a dictionary, it's a directory
                    elif isinstance(language_file, dict):
                        for directory, directory_files in language_file.items():
                            # Create directory
                            os.makedirs(f'{project_name}/{language}/{directory}')
                            # For each file in the directory
                            for directory_file in directory_files:
                                with open(f'{project_name}/{language}/{directory}/{directory_file}', 'w') as f:
                                    pass  # replace with actual file content generation

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python codegen.py Px.ypr')
        sys.exit(1)

    ypr_file = sys.argv[1]
    create_project_skeleton(ypr_file)
