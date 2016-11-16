import click
import pytest
from click.testing import CliRunner

# Load the main module
import os, sys
sys.path.insert(0, os.path.abspath('..'))

import main

# Begin Tests
def test_hi():
	# Test case for hi command
	runner = CliRunner()
	result = runner.invoke(main.pqcli, ['hi'])
	assert result.exit_code == 0
	assert result.output == 'Hi Buddy!\n'
	result = runner.invoke(main.pqcli, ['hi', 'Ryan'])
	assert result.exit_code == 0
	assert result.output == 'Hi Ryan!\n'
	result = runner.invoke(main.pqcli, ['hi', 'Ryan', '-c', 3])
	assert result.exit_code == 0
	assert result.output == 'Hi Ryan!\nHi Ryan!\nHi Ryan!\n'
	result = runner.invoke(main.pqcli, ['hi', 'Ryan', '--count', 3])
	assert result.exit_code == 0
	assert result.output == 'Hi Ryan!\nHi Ryan!\nHi Ryan!\n'


