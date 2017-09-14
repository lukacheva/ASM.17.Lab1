from .Zoo import Zoo
from .MenuItem import MenuItem
import os

zoo = Zoo()

def create_menu():
    menu = []
    menu.append(MenuItem(1, "Add animal", zoo.add_animal))
    menu.append(MenuItem(2, "Add bird", zoo.add_bird))
    menu.append(MenuItem(3, "Edit animal", zoo.edit_animal))
    menu.append(MenuItem(4, "Remove animal", zoo.remove_animal))
    menu.append(MenuItem(5, "Show zoo", zoo.show_zoo))
    menu.append(MenuItem(6, "Read zoo from file", zoo.read_zoo_from_file))
    menu.append(MenuItem(7, "Write zoo to file", zoo.write_zoo_to_file))
    menu.append(MenuItem(8, "Clear zoo", zoo.clear_zoo))
    menu.append(MenuItem(0, "Exit", None))
    return menu

def show_menu(menu):
    for item_menu in menu:
        print('{} - {}'.format(item_menu.id, item_menu.text))

def cover_print(text):
    os.system('cls')
    print(text)
    input()
    os.system('cls')

def main():
    menu = create_menu()
    id_list = [item.id for item in menu]
    while (True):
        show_menu(menu)
        try:
            selected_id = int(input())
            if (selected_id not in id_list):
                raise ValueError
            if (selected_id == 0):
                return
            os.system('cls')
            menu[selected_id - 1].func()
            print("\nPress enter to return to the menu...")
            input()
            os.system('cls')
        except ValueError:
            cover_print("Error! That was no valid value.\n\nPress enter to return to the menu...")
        except IndexError:
            cover_print("An animal with this id doesn't exist!\n\nPress enter to return to the menu...")
        except FileNotFoundError:
            cover_print("Error! File not found!\n\nPress enter to return to the menu...")


if __name__ == "__main__": 
    main()
