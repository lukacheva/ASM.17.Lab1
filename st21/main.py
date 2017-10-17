from .prison import *

prison = prison()

menu = {
	"1": ("Add prisoner", prison.add_prisoner),
    "2": ("Add overseer", prison.add_overseer),
    "3": ("Remove guy", prison.remove_person),
    "4": ("Edit guy", prison.edit_person),
    "5": ("Print list to console", prison.print_list),
    "6": ("Write list to file", prison.write_to_file),
    "7": ("Read list from file", prison.read_from_file),
    "8": ("Clear list", prison.clear_list),
    "9": ("Exit", "")
	}

def main():
    while True:
        for key in menu:
            print(key + " - " + menu[key][0])
            
        cur_input = input("")
        if int(cur_input) == 9:
            break
        menu[cur_input][1]()
        
