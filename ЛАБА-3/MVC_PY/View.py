import datetime


def start_menu():
    sm = int(input(" 1 to insert        \n"
                   " 2 to insert random \n"
                   " 3 to update        \n"
                   " 4 to delete        \n"
                   " 5 to select table  \n"
                   " 6 to search        \n"
                   " 7 to end           \n"
                   "Input: "))
    if sm < 1 or sm > 7:
        err()
        start_menu()
    else:

        return sm


def tables():
    choice_table = int(input("Select a table:\n"
                             "    1 = Cash Register\n"
                             "    2 = Railway carriage\n"
                             "    3 = Railway station\n"
                             "    4 = Ticket\n"
                             "    5 = Train\n"
                             "Input: "))
    if choice_table < 1 or choice_table > 5:
        err()
        tables()
    else:
        return choice_table


def input_insert(table):
    if table == 1:
        name = str(input("Input new name of the cashier: "))
        tickets = int(input("Input new number of tickets for sale: "))
        id_cr = int(input("Input new id_cr: "))
        id_rs = int(input("Input new id_rs: "))

        inp = [name, tickets, id_cr, id_rs]
        return inp

    elif table == 2:
        type_rc = str(input("Input new type of RC: "))
        num = int(input("Input new number of seats: "))
        id_rc = int(input("Input new id_rc: "))
        id_train = int(input("Input new train id: "))

        inp = [type_rc, num, id_rc, id_train]
        return inp

    elif table == 3:

        name = str(input("Input new name: "))
        address = str(input("Input new address: "))
        id_rs = int(input("Input new rs id: "))

        inp = [name, address, id_rs]
        return inp

    elif table == 4:
        time_entry = input("Input a time of departure in HH:MM format: ")
        hour, minute = map(int, time_entry.split(':'))
        dep = datetime.time(hour, minute)
        place = str(input("Input new place of departure and arrival: "))
        id_tick = int(input("Input new ticket id: "))
        id_rc = int(input("Input new rc id: "))
        id_cr = int(input("Input new cr id: "))

        inp = [dep, place, id_tick, id_rc, id_cr]
        return inp

    elif table == 5:
        type_r = str(input("Input new type of railway: "))
        id_train = int(input("Input new train id: "))
        id_rs = int(input("Input new rs id: "))

        inp = [type_r, id_train, id_rs]
        return inp


def count_rand():
    count = int(input("Input amount of data to generate: "))
    return count


def input_update(table):
    new = None
    if table == 1:
        id_cr = int(input("Num of cr id: "))
        column = int(input("1 = to upd name of the cashier\n"
                           "2 = to upd number of tickets for sale\n"
                           "3 = to upd id_rs\n"
                           "Input:"))

        if column == 1:
            new = str(input("New: "))
        elif column == 3 or column == 2:
            new = int(input("New: "))
        else:
            err()
            input_update(table)

        inp = [id_cr, column, new]
        return inp

    elif table == 2:
        id_rc = int(input("Num of rc id: "))
        column = int(input("1 = to upd type\n"
                           "2 = to upd number of seats\n"
                           "3 = to upd train id\n"
                           "Input:"))

        if column == 1:
            new = str(input("New: "))
        elif column == 3 or column == 2:
            new = int(input("New: "))
        else:
            err()
            input_update(table)

        inp = [id_rc, column, new]
        return inp

    elif table == 3:
        id_rs = int(input("Num of rs id: "))
        column = int(input("1 = to upd name\n"
                           "2 = to upd address\n"
                           "Input:"))

        if column == 1 or column == 2:
            new = str(input("New: "))
        else:
            err()
            input_update(table)

        inp = [id_rs, column, new]
        return inp

    elif table == 4:
        id_t = int(input("Num of ticket id: "))
        column = int(input("1 = to upd time of departure\n"
                           "2 = to upd place of departure and arrival\n"
                           "3 = to upd id rc\n"
                           "4 = to upd id cr\n"
                           "Input:"))

        if column == 1:
            time_entry = input("New time in HH:MM format: ")
            hour, minute = map(int, time_entry.split(':'))
            new = datetime.time(hour, minute)
        elif column == 2:
            new = str(input("New: "))
        elif column == 3 or column == 4:
            new = int(input("New: "))
        else:
            err()
            input_update(table)

        inp = [id_t, column, new]
        return inp

    elif table == 5:
        id_cr = int(input("Num of train id: "))
        column = int(input("1 = to upd type of railway\n"
                           "2 = to upd id_rs\n"
                           "Input:"))

        if column == 1:
            new = str(input("New: "))
        elif column == 2:
            new = int(input("New: "))
        else:
            err()
            input_update(table)

        inp = [id_cr, column, new]
        return inp


def del_id():
    nid = int(input("Num of id: "))
    return nid


def input_select():
    string = int(input("1 = to one str\n"
                       "2 = to all str\n"
                       "Input:"))
    if string == 1:
        nid = int(input("Num of id: "))
        inp = [string, nid]
        return inp

    elif string == 2:
        inp = [string]
        return inp

    else:
        err()
        input_select()


def input_search(table):
    if table == 1:
        column = int(input("1 = to search name of the cashier\n"
                           "2 = to search number of tickets for sale\n"
                           "3 = to search id_cr\n"
                           "4 = to search id_rs\n"
                           "Input:"))
        if column == 2 or column == 3 or column == 4:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp

        elif column == 1:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp

        else:
            err()
            input_search(table)

    elif table == 2:
        column = int(input("1 = to search type\n"
                           "2 = to search number of seats\n"
                           "3 = to search id_rc\n"
                           "4 = to search train id\n"
                           "Input:"))
        if column == 2 or column == 3 or column == 4:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp

        elif column == 1:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp

        else:
            err()
            input_search(table)

    elif table == 3:
        column = int(input("1 = to search name \n"
                           "2 = to search address\n"
                           "3 = to search id_rs\n"
                           "Input:"))

        if column == 1 or column == 2:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp
        elif column == 3:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp
        else:
            err()
            input_search(table)

    elif table == 4:
        column = int(input("1 = to search time of departure\n"
                           "2 = to search place of departure and arrival\n"
                           "3 = to search id_ticket\n"
                           "4 = to search id rc\n"
                           "5 = to search id cr\n"

                           "Input:"))
        if column == 1:
            time_entry_a = input("New start time in HH:MM format: ")
            hour, minute = map(int, time_entry_a.split(':'))
            a = datetime.time(hour, minute)

            time_entry_b = input("New finish time in HH:MM format: ")
            hour, minute = map(int, time_entry_b.split(':'))
            b = datetime.time(hour, minute)

            inp = [column, a, b]
            return inp

        elif column == 3 or column == 4 or column == 5:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp

        elif column == 2:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp

        else:
            err()
            input_search(table)

    elif table == 5:
        column = int(input("1 = to search type of railway\n"
                           "2 = to search id_train\n"
                           "3 = to search id_rs\n"

                           "Input:"))
        if column == 2 or column == 3:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp

        elif column == 1:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp

        else:
            err()
            input_search(table)


def fetch(table, f_table, inp):
    if table == 1:
        if inp[0] == 1:
            print("\ncashier =", f_table[0])
            print("number of tickets for sale =", f_table[1])
            print("id_cr =", f_table[2])
            print("id_rs =", f_table[3], "\n")
        elif inp[0] == 2:
            for i in f_table:
                print("\ncashier =", i.cashier)
                print("number of tickets for sale =", i.number_of_tickets_for_sale)
                print("id_cr =", i.id_cr)
                print("id_rs =", i.id_rs, "\n")

    elif table == 2:
        if inp[0] == 1:
            print("\n""type =", f_table[0])
            print("number of seats =", f_table[1])
            print("id_rc =", f_table[2])
            print("id_train =", f_table[3], "\n")
        elif inp[0] == 2:
            for i in f_table:
                print("\n""type =", i.type)
                print("number of seats =", i.number_of_seats)
                print("id_rc =", i.id_rc)
                print("id_train =", i.id_train, "\n")

    elif table == 3:
        if inp[0] == 1:
            print("\n""name =", f_table[0])
            print("address =", f_table[1])
            print("id_rs =", f_table[2], "\n")
        elif inp[0] == 2:
            for i in f_table:
                print("\n""name =", i.name)
                print("address =", i.address)
                print("id_rs =", i.id_rs, "\n")

    elif table == 4:
        if inp[0] == 1:
            print("\n""time of departure =", f_table[0])
            print("place of departure and arrival =", f_table[1])
            print("id_ticket =", f_table[2])
            print("id_rc =", f_table[3])
            print("id_cr =", f_table[4], "\n")
        elif inp[0] == 2:
            for i in f_table:
                print("\n""time of departure =", i.time_of_departure)
                print("place of departure and arrival =", i.place_of_departure_and_arrival)
                print("id_ticket =", i.id_ticket)
                print("id_rc =", i.id_rc)
                print("id_cr =", i.id_cr, "\n")

    elif table == 5:
        if inp[0] == 1:
            print("\n""type of railway =", f_table[0])
            print("id_train =", f_table[1])
            print("id_rs =", f_table[2], "\n")
        elif inp[0] == 2:
            for i in f_table:
                print("\n""type of railway =", i.type_of_railway)
                print("id_train =", i.id_train)
                print("id_rs =", i.id_rs, "\n")


def data(task):
    if task == 1:
        print("\n[Data was successfully inserted]\n")
    elif task == 2:
        print("\n[Random Data was successfully inserted]\n")
    elif task == 3:
        print("\n[Data was successfully updated]\n")
    elif task == 4:
        print("\n[Data was successfully deleted]\n")


def search_time(t):
    print("\nSearch duration = ", t, "\n")


def err():
    print("\n[Error input, try again!]\n")


def print_close():
    print("\n[PostgreSQL connection closed]")


def err_except(_ex):
    print("\n[Error while working with PostgreSQL", _ex, "]\n")
