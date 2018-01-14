import json
with open("dummy.json") as f:
	data = json.load(f)
	data["users"][0]["name"]="sagar"

with open("new.json", "w") as new_f:
	json.dump(data, new_f)