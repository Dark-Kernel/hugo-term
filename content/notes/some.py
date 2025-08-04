import os
import re
from datetime import datetime

def convert_header(content):
    front_matter = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not front_matter:
        return content

    fm = front_matter.group(1)
    lines = fm.splitlines()
    new_lines = []
    tags = []

    for line in lines:
        if line.startswith("Title:"):
            title = line[6:].strip()
            new_lines.append(f'Title: "{title}"')
        elif line.startswith("Published:"):
            date_str = line[10:].strip()
            date_only = date_str.split()[0]
            new_lines.append(f'Published: {date_only}')
        elif line.startswith("Author:"):
            author = line[7:].strip()
            new_lines.append(f'author: {author}')
        elif line.startswith("Tag:") or line.startswith("Tags:"):
            tag_raw = line.split(":", 1)[1].strip()
            tag_list = [t.strip().strip('"\'') for t in tag_raw.split(',')]
            if "go" in tag_list and "golang" not in tag_list:
                tag_list.append("golang")
            tags = tag_list
        else:
            continue

    # Extract description from post body
    body = re.sub(r'^---\n.*?\n---', '', content, flags=re.DOTALL).strip()
    description = body.split('\n')[0][:150].strip().replace('"', "'")
    new_lines.append(f'description: "{description}"')

    if tags:
        tags_str = ', '.join(f'"{t}"' for t in tags)
        new_lines.append(f'tags: [{tags_str}]')

    new_front = "---\n" + "\n".join(new_lines) + "\n---"
    new_content = re.sub(r'^---\n.*?\n---', new_front, content, flags=re.DOTALL)
    return new_content

# Path to directory containing markdown files
path = "2-notes"

for filename in os.listdir(path):
    if filename.endswith(".md"):
        full_path = os.path.join(path, filename)
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = convert_header(content)

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

