import click
import importlib


@click.command()
@click.argument("day", type=click.IntRange(1, 25))
@click.argument("input", type=click.File("r"))
def main(day, input):
    module = importlib.import_module(f"advent.day_{day:02d}")

    puzzle = module.read_input(input)

    click.echo(f"Part 1: {module.part_one(puzzle)}")
    click.echo(f"Part 2: {module.part_two(puzzle)}")
