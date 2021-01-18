import pytest
from click.testing import CliRunner

from advent.cli import main


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


def test_day_01(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
1721
979
366
299
675
1456
            """.strip()
            )

        result = runner.invoke(main, ["1", "input.txt"])

        assert result.output == "Part 1: 514579\nPart 2: 241861950\n"


def test_day_02(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
            """.strip()
            )

        result = runner.invoke(main, ["2", "input.txt"])

        assert result.output == "Part 1: 2\nPart 2: 1\n"


def test_day_03(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
            """.strip()
            )

        result = runner.invoke(main, ["3", "input.txt"])

        assert result.output == "Part 1: 7\nPart 2: 336\n"


def test_day_04(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
            """.strip()
            )

        result = runner.invoke(main, ["4", "input.txt"])

        assert result.output == "Part 1: 2\nPart 2: 2\n"


def test_day_05(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
            """.strip()
            )

        result = runner.invoke(main, ["5", "input.txt"])

        assert result.output.startswith("Part 1: 820")


def test_day_06(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
abc

a
b
c

ab
ac

a
a
a
a

b
            """.strip()
            )

        result = runner.invoke(main, ["6", "input.txt"])

        assert result.output == "Part 1: 11\nPart 2: 6\n"


def test_day_07(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
            """.strip()
            )

        result = runner.invoke(main, ["7", "input.txt"])

        assert result.output == "Part 1: 4\nPart 2: 32\n"


def test_day_08(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
            """.strip()
            )

        result = runner.invoke(main, ["8", "input.txt"])

        assert result.output == "Part 1: 5\nPart 2: 8\n"


def test_day_09(runner, monkeypatch):
    monkeypatch.setattr("advent.day_09.LEN_PREAMBLE", 5)

    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
            """.strip()
            )

        result = runner.invoke(main, ["9", "input.txt"])

        assert result.output == "Part 1: 127\nPart 2: 62\n"


def test_day_10(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
            """.strip()
            )

        result = runner.invoke(main, ["10", "input.txt"])

        assert result.output == "Part 1: 220\nPart 2: 19208\n"


def test_day_11(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
            """.strip()
            )

        result = runner.invoke(main, ["11", "input.txt"])

        assert result.output == "Part 1: 37\nPart 2: 26\n"


def test_day_12(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
F10
N3
F7
R90
F11
            """.strip()
            )

        result = runner.invoke(main, ["12", "input.txt"])

        assert result.output == "Part 1: 25\nPart 2: 286\n"


@pytest.mark.skip
def test_day_13(runner):
    with runner.isolated_filesystem():
        with open("input.txt", "w") as f:
            f.write(
                """
939
7,13,x,x,59,x,31,19
            """.strip()
            )

        result = runner.invoke(main, ["13", "input.txt"])

        assert result.output == "Part 1: 295\nPart 2: 0\n"


solution_test_data = [
    (1, 989824, 66432240),
    (2, 582, 729),
    (3, 218, 3847183340),
    (4, 230, 156),
    (5, 806, 562),
    (6, 6551, 3358),
    (7, 101, 108636),
    (8, 1753, 733),
    (9, 22406676, 2942387),
    (10, 2048, 1322306994176),
    (11, 2273, 2064),
    (12, 820, 66614),
    (13, 3215, 1001569619313439),
]


@pytest.mark.slow
@pytest.mark.parametrize(
    "day,part_one,part_two",
    solution_test_data,
    ids=(f"day_{day:02d}" for day in (params[0] for params in solution_test_data)),
)
def test_puzzle_solution(day, part_one, part_two, runner):
    result = runner.invoke(main, [str(day), f"./inputs/input_{day:02d}.txt"])

    assert result.output == f"Part 1: {part_one}\nPart 2: {part_two}\n"
