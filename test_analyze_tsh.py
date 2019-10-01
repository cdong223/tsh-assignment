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
