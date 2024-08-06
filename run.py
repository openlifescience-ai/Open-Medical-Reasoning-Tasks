import os
import json
import re
from parser import parse_markdown_to_json

def process_tasks(tasks_folder, json_folder):
    os.makedirs(json_folder, exist_ok=True)
    md_files = [f for f in os.listdir(tasks_folder) if f.endswith('.md')]

    for md_file in md_files:
        md_path = os.path.join(tasks_folder, md_file)
        json_file = md_file.replace('.md', '.json')
        json_path = os.path.join(json_folder, json_file)

        if not os.path.exists(json_path) or os.path.getmtime(md_path) > os.path.getmtime(json_path):
            print(f"Processing {md_file}...")
            
            try:
                with open(md_path, 'r', encoding='utf-8') as md_file:
                    markdown_content = md_file.read()

                json_content = parse_markdown_to_json(markdown_content)

                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(json_content, json_file, indent=2, ensure_ascii=False)
                
                print(f"Successfully converted and saved {json_file}")
            except MarkdownParsingError as e:
                print(f"Error processing {md_file}: {str(e)}")
            except Exception as e:
                print(f"Unexpected error processing {md_file}: {str(e)}")
        else:
            print(f"Skipping {md_file} - JSON file already up to date")

if __name__ == "__main__":
    tasks_folder = "tasks"
    json_folder = "tasks-json"
    process_tasks(tasks_folder, json_folder)
