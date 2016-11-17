import click
from time import sleep
import os

@click.group()
def pqcli():
	pass

@pqcli.command()
@click.argument('name', default="Buddy")
@click.option('-c', '--count', default=1)
def hi(name, count):
	for _ in range(count):
		click.echo("Hi {}!".format(name))

@pqcli.command()
def spi():
	path = os.path.join(os.path.dirname(__file__),'resources','spi.md')
	click.launch(path)
	click.echo("Showing SPI finish table")

if __name__ == '__main__':
	pqcli()