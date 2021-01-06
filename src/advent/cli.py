import click
import importlib


@click.command(help="Advent of Code 2020 Puzzle Solver")
@click.argument("calendar_day", type=click.IntRange(1, 25))
@click.argument("input_file", type=click.File("r"))
def main(calendar_day, input_file):
    module = importlib.import_module(f"advent.day_{calendar_day:02d}")

    puzzle = module.read_input(input_file)

    click.echo(f"Part 1: {module.part_one(puzzle)}")
    click.echo(f"Part 2: {module.part_two(puzzle)}")
