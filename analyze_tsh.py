def create_patient(first, last, age, gender, diag, tsh_list):
    """Create dictionary for a single patient

    Args:
        first (string): first name of patient
        last (string): last name of patient
        age (int): age of patient
        gender (string): gender of patient
        diag (string): patient diagnosis
        tsh_list (float): list of TSH values

    Returns:
        dictionary: patient
    """
    patient = {"First Name":  first,
               "Last Name":  last,
               "Age":  age,
               "Gender": gender,
               "Diagnosis": diag,
               "TSH": tsh_list}
    return patient


def diagnose(tsh_list):
    """Determines thyroid condition of patient based on TSH results

    "hyperthyroidism": any of their tests results is less than 1.0
    "hypothyroidism": any of their test results is greater than 4.0
    "normal thyroid function": all test results are b/w 1.0 and 4.0, inclusive

    Args:
        tsh_list (float): list of TSH values

    Returns:
        string: the diagnosis
    """
    is_normal = True
    for tsh in tsh_list:
        if tsh < 1.0:
            diag = "hyperthyroidism"
            is_normal = False
            break
        elif tsh > 4.0:
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
        tsh_values = f.readline().strip().split(",")
        tsh_values.pop(0)
        tsh_list = []
        for val in tsh_values:
            tsh_list.append(float(val))
        diag = diagnose(tsh_list)


if __name__ == "__main__":
    import_data("sample_data.txt")
