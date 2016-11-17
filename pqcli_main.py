import click
import helpers
from time import sleep
import os

@click.group()
def pqcli():
	pass

@pqcli.command()
@click.option('-n', '--name')
@click.option('-c', '--count', default=1)
def hi(name, count):
	if not name:
		name = helpers.get_config("USER_NAME")
	for _ in range(count):
		click.echo("Hi {}!".format(name))

@pqcli.command()
def spi():
	path = os.path.join(os.path.dirname(__file__),'resources','spi.md')
	click.launch(path)
	click.echo("Showing SPI finish table")

@pqcli.command()
@click.argument('keywords', nargs=-1)
def open(keywords):
	options = helpers.get_config("OPEN_FILES")
	successes = 0
	for keyword in keywords:
		if keyword in options:
			if click.launch(options[keyword]) == 0:
				successes += 1
				click.echo("Opened {}".format(keyword))
			else:
				click.echo("{} failed!".format(keyword))
		else:
			click.echo("{} not in file list!".format(keyword))
	click.echo("Successfully opened {} of {}".format(successes, len(keywords)))
		


if __name__ == "__main__":
	pqcli()