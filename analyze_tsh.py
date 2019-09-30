def diagnose(tsh_list):
    """Determines thyroid condition of patient based on TSH results

    "hyperthyroidism": any of their tests results is less than 1.0
    "hypothyroidism": any of their test results is greater than 4.0
    "normal thyroid function": all test results are b/w 1.0 and 4.0, inclusive

    Args:
        tsh_list (string): list of TSH values

    Returns:
        string: the diagnosis
    """
    is_normal = True
    for tsh in tsh_list:
        if float(tsh) < 1.0:
            diag = "hyperthyroidism"
            is_normal = False
            break
        elif float(tsh) > 4.0:
            diag = "hypothyroidism"
            is_normal = False
            break
    if is_normal is True:
        diag = "normal thyroid function"
    return diag


def import_data(filename):
    """Parses data file and pulls data for each patient listed

    Args:
        filename (string): name of file to be parsed

    Returns:
        None
    """
    f = open(filename, "r")
    file_end = False
    while file_end is False:
        name_input = f.readline().strip()
        if name_input == "END":
            file_end = True
            break
        name = name_input.split(" ")
        first = name[0]
        last = name[1]
        age = int(f.readline())
        gender = f.readline().strip()
        tsh_list = f.readline().strip().split(",")
        tsh_list.pop(0)
        diag = diagnose(tsh_list)


if __name__ == "__main__":
    import_data("sample_data.txt")
