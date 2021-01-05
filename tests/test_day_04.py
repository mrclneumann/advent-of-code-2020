import pytest

from advent.day_04 import read_input


@pytest.fixture()
def input_path(tmp_path):
    p = tmp_path / "input.txt"

    p.write_text(
        "\n".join(
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
    )

    return p


# @pytest.fixture()
# def passports(input_path):
#     return read_input(input_path)


def test_read_input(input_path):
    with input_path.open() as f:
        assert read_input(f) == [
            {
                "ecl": "gry",
                "pid": "860033327",
                "eyr": "2020",
                "hcl": "#fffffd",
                "byr": "1937",
                "iyr": "2017",
                "cid": "147",
                "hgt": "183cm",
            },
            {
                "iyr": "2013",
                "ecl": "amb",
                "cid": "350",
                "eyr": "2023",
                "pid": "028048884",
                "hcl": "#cfa07d",
                "byr": "1929",
            },
            {
                "hcl": "#ae17e1",
                "iyr": "2013",
                "eyr": "2024",
                "ecl": "brn",
                "pid": "760753108",
                "byr": "1931",
                "hgt": "179cm",
            },
            {
                "hcl": "#cfa07d",
                "eyr": "2025",
                "pid": "166559648",
                "iyr": "2011",
                "ecl": "brn",
                "hgt": "59in",
            },
        ]


# def test_num_valid_passports(passports):
#     assert num_valid_passports(passports) == 2
