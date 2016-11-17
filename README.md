# PQ CLI
A CLI to help automate and speed up monotonous tasks at ProtoQuick.

This is built on the [Click Framework](http://click.pocoo.org/), so see the documentation for more background.  

## Current Commands
For a comprehensive list of available commands and options, simply type `pqcli` or `pqcli --help`.

* __hi__: Greets the user

## Adding Commands
Currently, the way to add a command is to insert it to the bottom of the `pqcli.py` file.  Commands should follow the following format:

```python
@pqcli.command()
@pqcli.option('--count', default=1, help='number of greetings')
@pqcli.argument('name')
def hello(name):
    for x in range(count):
        click.echo("Hello {}".format(name))
```
As the project grows and the number of commands increases, I hope to expand the project structure to a more robust foldery structure, with each command getting its own module.  Put that in the TODOS.

## Tests
My goal is to develop the PQ CLI via TDD, so *in theory* the tests will be written before the actual functions, and they can be found in `test_pqcli.py`.  As above, it is my plan to move this to a more modular project structure as more and more commands get created.  Eventually, each command subtree will have its own test module.

## Future Plans
* Fill in the README
* Create Tests
* Create command: open COC
* Update command: open COC to open a list of forms
* Create command: part cost calculater
* Update command: part cost calculater to use SQLITE db of saved

## Additional Resources
1. [The Click Documentation](http://click.pocoo.org/)
