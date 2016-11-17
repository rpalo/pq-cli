import json, os

def get_config(key):
	with open(os.environ["PQCLI_CONFIG"] + ".json", "r") as config_file:
		data = json.load(config_file)
	return data.get(key)