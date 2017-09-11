from .Company import Company

company = Company()

EXIT_CODE = "9"

menu = {
    "1": ("Add employee", company.add_employee),
    "2": ("Add supervisor", company.add_supervisor),
    "3": ("Remove person", company.remove_person),
    "4": ("Edit person", company.edit_person),
    "5": ("Print list", company.print_staff),
    "6": ("Write list to file", company.write_to_file),
    "7": ("Read list from file", company.read_from_file),
    "8": ("Clear list", company.clear_staff),
    EXIT_CODE: ("Exit", None)
}


def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
        try:
            user_input = input(">>")
            if user_input == EXIT_CODE:
                break
            else:
                menu[user_input][1]()

        except Exception as ex:
            print("Exception raised: ", ex)


if __name__ == "__main__":
    main()
