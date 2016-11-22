import click
import util
from time import sleep
import os

@click.group()
def pqcli():
	"""A CLI helper for automating tasks at ProtoQuick"""
	pass

@pqcli.command()
@click.option('-n', '--name')
@click.option('-c', '--count', default=1)
def hi(name, count):
	"""Greets <name> or USER_NAME cheerfully <count> times."""
	if not name:
		name = util.get_config("USER_NAME")
	if name == None:
		raise click.FileError("PQCLI_CONFIG", hint="Error within the config.")
	for _ in range(count):
		click.echo("Hi {}!".format(name))

@pqcli.command()
def spi():
	"""Shows a SPI surface finish cheat sheet."""
	path = os.path.join(os.path.dirname(__file__),'resources','spi.md')
	click.launch(path)
	click.echo("Showing SPI finish table")

@pqcli.command()
@click.argument('keywords', nargs=-1)
def open(keywords):
	"""Takes in unlimited <keywords>, which match to the configured
	OPEN_FILES map.  Attempts to open each of them in their native
	application."""
	options = util.get_config("OPEN_FILES")
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

@pqcli.command()
@click.option('-w', '--weight', 
				help='Weight (in grams) per part',
				type=float,
				prompt="Weight (in grams) per part")
@click.option('-p', '--price',
				help='Material price ($/lb)',
				type=float,
				prompt="Material price ($/lb)")
@click.option('-m', '--markup',
				help="% material markup (0-100+)",
				type=float,
				prompt="% Material Markup (0-100+)")
@click.option('--seconds',
				help="Compute seconds/part for E2 instead of $",
				is_flag=True)
def cost(weight, price, markup, seconds):
	"""Calculates part cost based on <weight>, <price> of material,
	and <markup> percentage.  Can return seconds for E2 as well."""
	lb_per_part = weight/454.0
	dollar_per_part = lb_per_part * price * (markup + 100)/100.0
	if seconds:
		# Assume a material rate of $100/hour
		hours_per_part = dollar_per_part/100.0
		seconds_per_part = hours_per_part*3600
		click.echo("{:0.3f}".format(seconds_per_part))
	else:
		click.echo("{:0.3f}".format(dollar_per_part))

		


if __name__ == "__main__":
	pqcli()