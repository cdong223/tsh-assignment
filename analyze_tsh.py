def import_data(filename):
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


if __name__ == "__main__":
    import_data("sample_data.txt")
