import click

@click.group()
def pqcli():
	pass

@pqcli.command()
@click.argument('name', default="Buddy")
@click.option('-c', '--count', default=1)
def hi(name, count):
	for _ in range(count):
		click.echo("Hi {}!".format(name))

if __name__ == '__main__':
	pqcli()