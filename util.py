import click
import json, os

def get_config(key):
	try:
		conf_var = os.environ["PQCLI_CONFIG"]
		cf = open(conf_var + ".json", "r")
	except (KeyError, FileNotFoundError) as e:
		return None
	data = json.load(cf)
	return data.get(key)