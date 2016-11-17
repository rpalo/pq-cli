import click
from time import sleep

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
@click.option('-c','--count', default=10)
def progress(count):
	with click.progressbar(length=count) as bar:
		for _ in range(count):
			sleep(1)
			bar.update(1)

if __name__ == '__main__':
	pqcli()