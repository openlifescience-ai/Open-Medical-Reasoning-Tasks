import os
import json
import re
from parser import parse_markdown_to_json

def process_tasks(tasks_folder, json_folder):
    # Ensure the JSON folder exists
    os.makedirs(json_folder, exist_ok=True)

    # Get all markdown files in the tasks folder
    md_files = [f for f in os.listdir(tasks_folder) if f.endswith('.md')]

    for md_file in md_files:
        md_path = os.path.join(tasks_folder, md_file)
        json_file = md_file.replace('.md', '.json')
        json_path = os.path.join(json_folder, json_file)

        # Check if JSON file doesn't exist or is older than the markdown file
        if not os.path.exists(json_path) or os.path.getmtime(md_path) > os.path.getmtime(json_path):
            print(f"Converting {md_file} to JSON...")
            
            # Read markdown content
            with open(md_path, 'r', encoding='utf-8') as md_file:
                markdown_content = md_file.read()

            # Convert to JSON
            json_content = parse_markdown_to_json(markdown_content)

            # Save JSON file
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_content, json_file, indent=2, ensure_ascii=False)
            
            print(f"Saved {json_file}")
        else:
            print(f"Skipping {md_file} - JSON file already up to date")

if __name__ == "__main__":
    tasks_folder = "tasks"
    json_folder = "tasks-json"
    process_tasks(tasks_folder, json_folder)
