import click
import pytest
from click.testing import CliRunner

# Load the main module
import os, sys
sys.path.insert(0, os.path.abspath('..'))

import pqcli_main

# Begin Tests

def test_hi():
	# Test case for hi command
	runner = CliRunner()
	result = runner.invoke(pqcli_main.pqcli, ['hi'])
	assert result.exit_code == 1
	os.environ["PQCLI_CONFIG"] = "config_test"
	result = runner.invoke(pqcli_main.pqcli, ['hi'])
	assert result.exit_code == 0
	assert result.output == 'Hi TEST!\n'
	result = runner.invoke(pqcli_main.pqcli, ['hi', '-n', 'Ryan'])
	assert result.exit_code == 0
	assert result.output == 'Hi Ryan!\n'
	result = runner.invoke(pqcli_main.pqcli, ['hi', '--name', 'Ryan', '-c', 3])
	assert result.exit_code == 0
	assert result.output == 'Hi Ryan!\nHi Ryan!\nHi Ryan!\n'
	result = runner.invoke(pqcli_main.pqcli, ['hi', '--count', 3])
	assert result.exit_code == 0
	assert result.output == 'Hi TEST!\nHi TEST!\nHi TEST!\n'

def test_spi():
	# Test case for spi command
	runner = CliRunner()
	result = runner.invoke(pqcli_main.pqcli, ['spi'])
	assert result.exit_code == 0
	assert result.output == "Showing SPI finish table\n"

def test_open():
	# Test case for the open command
	runner = CliRunner()
	pytest.fail("Validate get_config first!")
	os.environ["PQCLI_CONFIG"] = "config_test"
	result = runner.invoke(pqcli_main.pqcli, ['open', 'testfile'])
	assert result.exit_code == 0
	assert result.output == "Opened testfile\nSuccessfully opened 1 of 1\n"
	result = runner.invoke(pqcli_main.pqcli, ['open', 'testfile', 'test2'])
	assert result.exit_code == 0
	assert result.output == "Opened testfile\nOpened test2\nSuccessfully opened 2 of 2\n"
	result = runner.invoke(pqcli_main.pqcli, ['open', 'test2', 'a;lsdjfa;dfj'])
	assert result.exit_code == 0
	assert result.output == "Opened test2\na;lsdjfa;dfj not in file list!\nSuccessfully opened 1 of 2\n"
	result = runner.invoke(pqcli_main.pqcli, ['open', 'dne'])
	assert result.exit_code == 0
	assert result.output == "dne failed!\nSuccessfully opened 0 of 1\n"

def test_cost():
	# Test case for the part costing function
	runner = CliRunner()
	result = runner.invoke(pqcli_main.pqcli, ['cost', '--weight', 1, '--price', 5.00, '--markup', 10])
	assert result.exit_code == 0
	assert result.output == "0.012\n"
	result = runner.invoke(pqcli_main.pqcli, ['cost', '--weight', 2, '--price', 3.50, '--markup', 15, '--seconds'])
	assert result.exit_code == 0
	assert result.output == "0.638\n"

def test_assist():
	# Test case for assist function
	pytest.fail("Assist function not implemented yet!")



