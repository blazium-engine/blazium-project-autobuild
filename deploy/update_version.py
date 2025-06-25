import subprocess
import re
import os

# Get the total number of commits in the repository
commit_count = subprocess.check_output(["git", "rev-list", "--count", "HEAD"]).decode("utf-8").strip()

# Define the base version (e.g., 1.0)
base_version = "1.2"

# Create the version string
version = f"{base_version}.{commit_count}"

# Update the version in project.godot
with open("project.godot", "r") as file:
    content = file.read()

# Replace the version string in project.godot
content = re.sub(
    r'config/version="([^"]+)"',
    f'config/version="{version}"',
    content
)

store_name = os.environ.get("STORE_NAME", "")

# Update the store name
content = re.sub(
    r'game/store_name=""',
    f'game/store_name="{store_name}"',
    content
)

# Replace game/lobby_server_local=true with false if it appears
content = re.sub(
    r"game/lobby_server_local=true",
    "game/lobby_server_local=false",
    content
)

# Write the updated content back to project.godot
with open("project.godot", "w") as file:
    file.write(content)

print(f"Updated version to: {version}")

# Update android version version/code from export_presets.cfg

with open("export_presets.cfg", "r") as file:
    content = file.read()

content = re.sub(
    r'version/code=\d+',
    f'version/code={commit_count}',
    content
)

with open("export_presets.cfg", "w") as file:
    file.write(content)

print(f"Updated android version to: {commit_count}")
print(f"Updated store_name to: {store_name}")
# Put it in env var GAME_VERSION
with open("version.txt", "w") as file:
    file.write(version)
