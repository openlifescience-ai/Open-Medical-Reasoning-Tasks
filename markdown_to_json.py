import os
import json
import re
from pyparser import *

def process_tasks(tasks_folders, json_folder):
    # Create the JSON folder if it doesn't exist
    os.makedirs(json_folder, exist_ok=True)
    
    for tasks_folder in tasks_folders:
        # Get a list of all markdown files in the tasks folder
        md_files = [f for f in os.listdir(tasks_folder) if f.endswith('.md')]
        
        for md_file in md_files:
            # Construct full paths for markdown and json files
            md_path = os.path.join(tasks_folder, md_file)
            json_file = md_file.replace('.md', '.json')
            json_path = os.path.join(json_folder, json_file)
            
            # Check if JSON file needs to be created or updated
            if not os.path.exists(json_path) or os.path.getmtime(md_path) > os.path.getmtime(json_path):
                print(f"Processing {md_file} from {tasks_folder}...")
                
                try:
                    # Read the markdown file
                    with open(md_path, 'r', encoding='utf-8') as md_file:
                        markdown_content = md_file.read()
                    
                    # Parse markdown to JSON
                    json_content = parse_markdown_to_json(markdown_content)
                    
                    # Write the JSON content to file
                    with open(json_path, 'w', encoding='utf-8') as json_file:
                        json.dump(json_content, json_file, indent=2, ensure_ascii=False, separators=(',', ': '))
                        json_file.write('\n')  # Add a final newline
                    
                    print(f"Successfully converted and saved {json_file}")
                except MarkdownParsingError as e:
                    # Handle specific markdown parsing errors
                    print(f"Error processing {md_file} from {tasks_folder}: {str(e)}")
                except Exception as e:
                    # Handle any other unexpected errors
                    print(f"Unexpected error processing {md_file} from {tasks_folder}: {str(e)}")
            else:
                # Skip processing if JSON file is up to date
                print(f"Skipping {md_file} from {tasks_folder} - JSON file already up to date")

if __name__ == "__main__":
    # Define folder paths
    tasks_folders = [
        "core_medical_reasoning_tasks",
        "specialized_medical_tasks",
        "subject_specific_medical_tasks"
    ]
    json_folder = "medical-tasks-json"
    
    # Run the main processing function
    process_tasks(tasks_folders, json_folder)