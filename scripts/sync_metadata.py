import json
import yaml
import sys
import os
from datetime import datetime

METADATA_FILE = "project-metadata.yml"

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f) or {}

def save_yaml(path, data):
    with open(path, 'w') as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

def sync_from_course_engine(manifest):
    """Map Course Engine manifest.json to project-metadata.yml"""
    updates = {}
    
    course = manifest.get("course", {})
    if course.get("title"): updates["project_title"] = course.get("title")
    if course.get("version"): updates["project_version"] = course.get("version")
    
    audit = manifest.get("governance_audit", {})
    if audit:
        updates["ai_governance"] = {
            "scoping_health": f"{audit.get('score', 0)}/100 [{audit.get('health', 'Unknown')}]",
            "policy_summary": f"Audit found {len(audit.get('findings', []))} findings.",
        }
    
    builder = manifest.get("builder", {})
    if builder:
        updates["audit_trail"] = {
            "source_tool": "Course Engine",
            "builder_version": builder.get("version", "N/A"),
            "transformation_integrity": "N/A",
            "manifest_sha256": "Captured"
        }
        
    return updates

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/sync_metadata.py <manifest.json>")
        sys.exit(1)
        
    source_path = sys.argv[1]
    if not os.path.exists(source_path):
        print(f"Error: Source file {source_path} not found.")
        sys.exit(1)
        
    source_data = load_json(source_path)
    current_meta = load_yaml(METADATA_FILE)
    
    # Determine source type and map
    # For v1, we assume Course Engine manifest if 'manifest_version' is present
    if "manifest_version" in source_data:
        new_values = sync_from_course_engine(source_data)
    else:
        print("Error: Unknown JSON format. Supporting Course Engine manifest.json in v1.")
        sys.exit(1)
        
    # Warn and Merge
    changes = []
    for k, v in new_values.items():
        if k in current_meta and current_meta[k] != v and current_meta[k] not in ["Not specified", "unknown", "N/A", "REPLACE THIS: Lead Author"]:
             print(f"WARNING: Overwriting manual value for '{k}':")
             print(f"  Old: {current_meta[k]}")
             print(f"  New: {v}")
        
        if current_meta.get(k) != v:
            changes.append(f"{k}: -> {v}")
            current_meta[k] = v
            
    current_meta["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    if not changes:
        print("No changes detected. Metadata is already in sync.")
    else:
        save_yaml(METADATA_FILE, current_meta)
        print("\nSync Complete. Sync Report:")
        for c in changes:
            print(f" - {c}")
        print(f"\nUpdated {METADATA_FILE}")

if __name__ == "__main__":
    main()
