import re
import json
import sys
import os

def load_mappings(filepath):
    mappings = {}
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found.")
        return mappings

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    for line in lines:
        if '|' in line and '---' not in line:
            parts = [p.strip() for p in line.split('|')]
            # | Key | Value | -> ['', 'Key', 'Value', '']
            if len(parts) >= 3:
                key = parts[1]
                val = parts[2]
                if key and val and key != "Activity Type":
                    mappings[key.lower()] = val
    return mappings

def parse_visual_plan(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Mermaid block
    mermaid_match = re.search(r'```mermaid(.*?)```', content, re.DOTALL)
    if mermaid_match:
        graph_content = mermaid_match.group(1)
    else:
        graph_content = content

    # Extract nodes: ID[Label], ID((Label))
    # Using a broad regex that captures content inside the first pair of delimiters
    node_pattern = re.compile(r'([A-Za-z0-9_]+)\s*(?:\[|\(\(|>|\{)\s*(.*?)\s*(?:\]|\)\)|\)|>|\})')

    nodes = {}
    for match in node_pattern.finditer(graph_content):
        node_id = match.group(1)
        label = match.group(2)
        nodes[node_id] = label.strip()

    edges = []
    lines = graph_content.splitlines()
    for line in lines:
        if '-->' in line:
            parts = line.split('-->')
            ids = []
            for part in parts:
                part = part.strip()
                # Extract ID at the start of the part
                m = re.match(r'^([A-Za-z0-9_]+)', part)
                if m:
                    ids.append(m.group(1))

            for i in range(len(ids) - 1):
                edges.append((ids[i], ids[i+1]))

    return nodes, edges

def sort_nodes(nodes, edges):
    if not nodes:
        return []

    targets = set(to_node for from_node, to_node in edges)
    sources = set(from_node for from_node, to_node in edges)

    start_nodes = [n for n in sources if n not in targets]

    start_node = None
    # Look for "start" in label
    for n in nodes:
        if "start" in nodes[n].lower():
            start_node = n
            break

    if not start_node and start_nodes:
        start_node = start_nodes[0]

    if not start_node:
        # Fallback: return definition order (keys)
        return list(nodes.keys())

    ordered = []
    queue = [start_node]
    visited = set()

    adj = {}
    for u, v in edges:
        if u not in adj: adj[u] = []
        adj[u].append(v)

    while queue:
        u = queue.pop(0)
        if u in visited: continue
        visited.add(u)
        ordered.append(u)

        if u in adj:
            for v in adj[u]:
                if v not in visited:
                    queue.append(v)

    # Add disconnected nodes
    for n in nodes:
        if n not in visited:
            ordered.append(n)

    return ordered

def generate_json(nodes, ordered_ids, mappings):
    slides = []
    for node_id in ordered_ids:
        label = nodes.get(node_id, "")

        # Skip purely structural Start/End nodes
        if label.strip().upper() in ["START", "END"]:
            continue

        layout = "split_table" # Default

        found_key = False
        sorted_keys = sorted(mappings.keys(), key=len, reverse=True)

        for key in sorted_keys:
            if key in label.lower():
                layout = mappings[key]
                found_key = True
                break

        if not found_key and "default" in mappings:
             layout = mappings["default"]

        slide = {
            "layout": layout,
            "title": label,
            "content": f"<p>{label}</p>"
        }

        # Add required fields for specific layouts to prevent render errors
        if layout == "video":
            slide["video_id"] = ""
            slide["video_autoplay"] = True
            slide["video_loop"] = True

        if layout in ["match_reorder", "ranking"]:
             slide["left_items"] = [{"text": "Item 1"}]
             slide["right_items"] = [{"text": "Item A"}]
             slide["rationale"] = label

        if layout == "mission":
            slide["mission_title"] = label

        slides.append(slide)

    presentation = {
        "meta": {
            "title": "Generated Presentation"
        },
        "slides": slides
    }
    return presentation

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_plan_to_json.py <path_to_visual_plan.md>")
        sys.exit(1)

    plan_path = sys.argv[1]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    # script_dir = skills/creating-html-presentation/scripts
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))
    mapping_path = os.path.join(repo_root, "knowledge_base", "reveal_activity_matrix.md")

    mappings = load_mappings(mapping_path)
    nodes, edges = parse_visual_plan(plan_path)
    ordered_ids = sort_nodes(nodes, edges)
    presentation_json = generate_json(nodes, ordered_ids, mappings)

    output_dir = os.path.dirname(plan_path)
    output_path = os.path.join(output_dir, "presentation.json")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(presentation_json, f, indent=2)

    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
