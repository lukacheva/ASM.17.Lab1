from .Film import Film


def main():
    new_blockbuster = Film()

    menu_actions = [
        '[0] - Print film name\n',
        '[1] - Edit film name\n',
        '[2] - Add new actor\n',
        '[3] - Edit actor\n',
        '[4] - Remove actor\n',
        '[5] - Print all actors\n',
        '[6] - Remove all actors\n',
        '[7] - Save actors to file\n',
        '[8] - Load actors to file\n',
        '[9] - Quit menu\n'
    ]

    actions = [
        new_blockbuster.print_film_name,
        new_blockbuster.enter_film_name,
        new_blockbuster.add_new_actor,
        new_blockbuster.edit_actor,
        new_blockbuster.remove_actor,
        new_blockbuster.print_all_actors,
        new_blockbuster.remove_all_actors,
        new_blockbuster.save_actors_to_file,
        new_blockbuster.load_actors_from_file
    ]

    while True:
        print('\nWhat action do you want to perform: \n%s' % ''.join(menu_actions))
        try:
            action_digit = int(input('Input one digit: '))
            if action_digit == 9:
                break
            actions[action_digit]()
        except:
            print('Wrong input data.')


if __name__ == '__main__':
    main()
