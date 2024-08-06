import re
import json

def parse_markdown_to_json(markdown_text):
    # Initialize the JSON structure
    task = {
        "name": "",
        "description": "",
        "modality": "",
        "diagram": None,
        "citations": None,
        "examples": [],
        "tags": []
    }

    # Extract name
    name_match = re.search(r'^#\s+(.+)$', markdown_text, re.MULTILINE)
    if name_match:
        task["name"] = name_match.group(1).strip()

    # Extract description
    desc_match = re.search(r'## Description:\s*(.+?)(?=##)', markdown_text, re.DOTALL)
    if desc_match:
        task["description"] = desc_match.group(1).strip()

    # Extract modality
    modality_match = re.search(r'## Modality:\s*(.+?)(?=##)', markdown_text, re.DOTALL)
    if modality_match:
        task["modality"] = modality_match.group(1).strip()

    # Extract diagram (if present)
    diagram_match = re.search(r'## Diagram \(Optional\):\s*(.+?)(?=##)', markdown_text, re.DOTALL)
    if diagram_match:
        task["diagram"] = diagram_match.group(1).strip() or None

    # Extract citations (if present)
    citations_match = re.search(r'## Citations \(Optional\):\s*(.+?)(?=##)', markdown_text, re.DOTALL)
    if citations_match:
        citations = citations_match.group(1).strip()
        task["citations"] = [citation.strip()[2:] for citation in citations.split('\n') if citation.strip().startswith('-')]

    # Extract examples
    examples_match = re.search(r'## Examples:(.*?)(?=## Tags:)', markdown_text, re.DOTALL)
    if examples_match:
        examples_text = examples_match.group(1)
        examples = re.split(r'###\s+Example\s+\d+:', examples_text)[1:]  # Split by example headers
        for example in examples:
            input_match = re.search(r'Input:\s*```(.+?)```', example, re.DOTALL)
            output_match = re.search(r'Output:\s*```(.+?)```', example, re.DOTALL)
            if input_match and output_match:
                task["examples"].append([{
                    "input": input_match.group(1).strip(),
                    "output": output_match.group(1).strip()
                }])

    # Extract tags
    tags_match = re.search(r'## Tags:(.+?)$', markdown_text, re.DOTALL)
    if tags_match:
        tags = tags_match.group(1).strip()
        task["tags"] = [tag.strip()[2:] for tag in tags.split('\n') if tag.strip().startswith('-')]

    return task
