import json

def load_keybinds(file_path="keybinds.json"):
    with open(file_path, "r") as file:
        return json.load(file)

def apply_keybinds(root, keybinds, actions):
    for action_name, key_combo in keybinds.items():
        if action_name in actions:
            root.bind(f"<{key_combo}>", actions[action_name])

def format_keybinds(keybinds: dict) -> str:
    return "\n".join(f"{action} : {combo}" for action, combo in keybinds.items())
