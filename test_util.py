import pytest

# Load the util module
import os, sys
sys.path.insert(0, os.path.abspath('..'))

import util

def test_get_config():
	os.environ["PQCLI_CONFIG"] = ";adsfa;sdfja;"
	assert util.get_config("USER_NAME") == None
	del(os.environ["PQCLI_CONFIG"])
	assert util.get_config("USER_NAME") == None
	os.environ["PQCLI_CONFIG"] = "config_test"
	assert util.get_config("USER_NAME") == "TEST"
	assert util.get_config("ABSDLFKJDASKLF") == None