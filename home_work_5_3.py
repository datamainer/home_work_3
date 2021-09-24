def generation_people():
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]

    classes = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]

    list_index = 1

    for people in range(len(tutors)):
        if len(classes) > people:
            yield redactor_try(tutors[list_index], classes[list_index])
            list_index += 1

        else:
            yield redactor_false(tutors[list_index])
            list_index += 1


def redactor_try(tutors_list, classes_list):
    print(next(f'({tutors_list} : {classes_list})'))

    return tutors_list, classes_list


def redactor_false(tutors_list):
    print(next(f'({tutors_list} : None'))

    return tutors_list


generation_people()









