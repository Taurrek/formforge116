import json

with open("public/avatar_state.json") as f:
    avatar_data = json.dumps(json.load(f), indent=2)

with open("dist/index.html", "r") as f:
    html = f.read()

# Replace first empty object {} in index.html (used by AvatarStream)
html = html.replace("{}", avatar_data, 1)

with open("dist/index.html", "w") as f:
    f.write(html)

print("✅ Avatar data injected into offline HTML.")
