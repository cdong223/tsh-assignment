import pytest


@pytest.mark.parametrize("tsh_values, expected", [
                                ([2.6, 1.5, 1.2, 3.9, 2.0, 3.1, 3.7, 2.5, 2.1,
                                    4.0], "normal thyroid function"),
                                ([3.9, 2.2, 2.3, 2.2, 0.6, 0.4, 3.2, 2.6, 3.8,
                                    0.9, 2.3], "hyperthyroidism"),
                                ([2.6, 5.1, 1.1, 3.7, 4.9, 3.6, 3.5, 4.0, 2.4],
                                    "hypothyroidism"),
                                ([4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
                                    4.0, 4.9], "hypothyroidism"),
                                ([0.3, 2.5, 1.7, 2.8, 2.7, 1.2, 3.9, 1.2, 3.8,
                                    2.4, 2.0], "hyperthyroidism"),
                                ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                    1.0], "normal thyroid function"),
                                ([2.7, 3.2, 2.5, 2.3, 5.8, 3.4, 2.3, 1.2, 1.5,
                                    2.2, 3.0], "hypothyroidism"),
                                ([0.3, 0.5, 0.7, 0.7, 0.1, 0.2, 0.2, 0.1, 0.5,
                                    0.6, 0.5], "hyperthyroidism"),
                                ([4.1, 4.5, 4.5, 4.6, 4.6, 4.8, 4.3, 4.7, 4.2,
                                    4.4, 4.5], "hypothyroidism"),
                                ([4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
                                    4.0, 0.2], "hyperthyroidism")
])
def test_diagnose(tsh_values, expected):
    from analyze_tsh import diagnose
    result = diagnose(tsh_values)
    assert result == expected


def read_in_data(file):
    f = open(file, 'r')
    name_input = f.readline()
    age_input = f.readline()
    gender_input = f.readline()
    tsh_input = f.readline()
    return name_input, age_input, gender_input, tsh_input


@pytest.mark.parametrize("file, expected", [
                                ("testdata.txt", ('Anne', 'Boynton', 45,
                                                  'Female',
                                                  'normal thyroid function',
                                                  [1.8, 1.9, 2.8, 3.0, 3.0,
                                                   3.4, 3.5, 3.6, 3.6, 4.0])),
                                ("testdata2.txt", ('Kamal', 'Solaiman', 31,
                                                   'Male', 'hyperthyroidism',
                                                   [0.4, 0.9, 1.4, 1.8, 2.3,
                                                    2.5, 2.7, 3.0, 3.1, 3.1,
                                                    3.8])),
                                ("testdata3.txt", ('Kyaw', 'Win', 54, 'Male',
                                                   'normal thyroid function',
                                                   [1.0, 1.1, 1.3, 1.4, 1.9,
                                                    2.5, 2.6, 2.7, 3.5])),
                                ("testdata4.txt", ('Larissa', 'Webb', 46,
                                                   'Female', 'hypothyroidism',
                                                   [2.1, 2.9, 3.5, 4.1, 6.3,
                                                    6.3, 6.7, 6.9, 7.1, 7.2,
                                                    7.6])),
                                ("testdata5.txt", ('Livia', 'Villarroel', 62,
                                                   'Female', 'hyperthyroidism',
                                                   [0.2, 0.7, 0.8, 1.5, 2.0,
                                                    2.4, 2.5, 2.7, 2.8, 2.9,
                                                    3.8])),
                                ("testdata6.txt", ('Catherine', 'Su', 44,
                                                   'Female',
                                                   'normal thyroid function',
                                                   [1.1, 2.0, 2.1, 2.4, 2.4,
                                                    3.0, 3.5, 3.7, 3.9, 3.9])),
                                ("testdata7.txt", ('Francisco', 'Valle', 35,
                                                   'Male', 'hypothyroidism',
                                                   [2.4, 2.5, 2.7, 3.3, 4.0,
                                                    4.2, 4.5, 5.2, 5.2, 5.3,
                                                    5.8])),
                                ("testdata8.txt", ('Julian', 'Thomson', 64,
                                                   'Male', 'hyperthyroidism',
                                                   [0.2, 0.2, 0.6, 0.6, 1.0,
                                                    1.1, 2.2, 3.5, 3.5, 3.5,
                                                    3.7])),
                                ("testdata9.txt", ('Monte', 'Swarup', 51,
                                                   'Male', 'hypothyroidism',
                                                   [2.4, 3.1, 3.5, 3.6, 4.2,
                                                    4.3, 4.5, 4.8, 5.5, 5.6,
                                                    5.7])),
                                ("testdata10.txt", ('Jeffrey', 'Bond', 77,
                                                    'Male', 'hyperthyroidism',
                                                    [0.2, 0.2, 0.5, 1.0, 1.4,
                                                     2.0, 2.0, 2.2, 2.3, 2.4,
                                                     2.6]))
])
def test_format_data(file, expected):
    from analyze_tsh import format_data
    name_input, age_input, gender_input, tsh_input = read_in_data(file)
    result = format_data(name_input, age_input, gender_input, tsh_input)
