import pytest
from advent.cli import main
from click.testing import CliRunner


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


def write_input_file(lines):
    with open("input.txt", "w") as f:
        f.writelines(line + "\n" for line in lines)


def test_day_01(runner):
    with runner.isolated_filesystem():
        write_input_file(
            [
                "1721",
                "979",
                "366",
                "299",
                "675",
                "1456",
            ]
        )

        result = runner.invoke(main, ["1", "input.txt"])

        assert result.output == "Part 1: 514579\nPart 2: 241861950\n"


def test_day_02(runner):
    with runner.isolated_filesystem():
        write_input_file(
            [
                "1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc",
            ]
        )

        result = runner.invoke(main, ["2", "input.txt"])

        assert result.output == "Part 1: 2\nPart 2: 1\n"


def test_day_03(runner):
    with runner.isolated_filesystem():
        write_input_file(
            [
                "..##.......",
                "#...#...#..",
                ".#....#..#.",
                "..#.#...#.#,",
                ".#...##..#.",
                "..#.##.....",
                ".#.#.#....#",
                ".#........#",
                "#.##...#...",
                "#...##....#",
                ".#..#...#.#",
            ]
        )

        result = runner.invoke(main, ["3", "input.txt"])

        assert result.output == "Part 1: 7\nPart 2: 336\n"


def test_day_04(runner):
    with runner.isolated_filesystem():
        write_input_file(
            [
                "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
                "byr:1937 iyr:2017 cid:147 hgt:183cm",
                "",
                "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
                "hcl:#cfa07d byr:1929",
                "",
                "hcl:#ae17e1 iyr:2013",
                "eyr:2024",
                "ecl:brn pid:760753108 byr:1931",
                "hgt:179cm",
                "",
                "hcl:#cfa07d eyr:2025 pid:166559648",
                "iyr:2011 ecl:brn hgt:59in",
            ]
        )

        result = runner.invoke(main, ["4", "input.txt"])

        assert result.output == "Part 1: 2\nPart 2: 2\n"


def test_day_05(runner):
    with runner.isolated_filesystem():
        write_input_file(["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"])

        result = runner.invoke(main, ["5", "input.txt"])

        assert result.output.startswith("Part 1: 820")


def test_day_06(runner):
    with runner.isolated_filesystem():
        write_input_file(
            [
                "abc",
                "",
                "a",
                "b",
                "c",
                "",
                "ab",
                "ac",
                "",
                "a",
                "a",
                "a",
                "a",
                "",
                "b",
            ]
        )

        result = runner.invoke(main, ["6", "input.txt"])

        assert result.output == "Part 1: 11\nPart 2: 6\n"


solution_test_data = [
    (1, 989824, 66432240),
    (2, 582, 729),
    (3, 218, 3847183340),
    (4, 230, 156),
    (5, 806, 562),
    (6, 6551, 3358),
]


@pytest.mark.parametrize(
    "day,part_one,part_two",
    solution_test_data,
    ids=(f"day_{day:02d}" for day in (params[0] for params in solution_test_data)),
)
def test_puzzle_solution(day, part_one, part_two, runner):
    result = runner.invoke(main, [str(day), f"./inputs/input_{day:02d}.txt"])

    assert result.output == f"Part 1: {part_one}\nPart 2: {part_two}\n"
