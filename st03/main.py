from .Army import Staff
import sys

Military_unit=Staff()
menu = {"1":("Add object", Military_unit.add),
        "2":("Edit", Military_unit.edit),
        "3":("Delete object", Military_unit.delete),
        "4":("Show list", Military_unit.out),
        "5":("Save to file", Military_unit.write),
        "6":("Load from file", Military_unit.read),
        "7":("Exit", sys.exit)}


def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
        user_input = input("")
        menu[user_input][1]()

if __name__ == "__main__":
    main()
