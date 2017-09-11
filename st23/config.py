from st23.University import University


# Замена switch/case
def setup(university: University):
    return [
        {
            'value': 0,
            'text': 'add object',
            'actions': [
                {
                    'value': 0,
                    'text': 'add student',
                    'func': university.add_student
                }, {
                    'value': 1,
                    'text': 'add teacher',
                    'func': university.add_teacher
                }
            ]
        }, {
            'value': 1,
            'text': 'edit object',
            'actions': [
                {
                    'value': 0,
                    'text': 'edit university',
                    'func': university.edit
                }, {
                    'value': 1,
                    'text': 'edit man',
                    'func': university.edit_mans
                }
            ]
        }, {
            'value': 2,
            'text': 'remove object',
            'func': university.remove_man
        }, {
            'value': 3,
            'text': 'show all objects',
            'func': university.show_people
        }, {
            'value': 4,
            'text': 'save to file',
            'func': university.save_list
        }, {
            'value': 5,
            'text': 'load from file',
            'func': university.get_list
        }, {
            'value': 6,
            'text': 'clear list',
            'func': university.clear_men
        }
    ]
