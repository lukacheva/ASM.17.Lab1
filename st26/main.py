from .Container import Container

container = Container()

EXIT = "9"

menu = {
    "1": ("Add player", container.add_player),
    "2": ("Add goalkeeper", container.add_goalkeeper),
    "3": ("Edit player", container.edit_player),
    "4": ("Remove player", container.remove_player),
    "5": ("Show players list", container.show_container),
    "6": ("Write players list to file", container.write_container_to_file),
    "7": ("Read players  list from file", container.read_container_from_file),
    "8": ("Clear players list", container.clear_container),
    EXIT: ("Exit", None)
}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
        try:
            user_input = input(">>")
            if user_input == EXIT:
                break
            else:
                menu[user_input][1]()

        except Exception as ex:
            print("Exception raised: ", ex)


if __name__ == "__main__":
    main()