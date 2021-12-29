import time
import psycopg2


def connect():
    connection = psycopg2.connect(
        database="Vlad",
        user="postgres",
        password="4214",
        host="127.0.0.1")
    connection.autocommit = True
    return connection


def close():
    connection = connect()
    connection.close()


def insert(table, inp):
    connection = connect()
    if table == 1:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Cash register"(cashier, number_of_tickets_for_sale, id_cr, id_rs) 
            VALUES(%s, %s, %s, %s);""", (inp[0], inp[1], inp[2], inp[3],))

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Railway carriage"(type, number_of_seats, id_rc, id_train) 
            VALUES(%s, %s, %s, %s);""", (inp[0], inp[1], inp[2], inp[3],))

    elif table == 3:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Railway station"(name, address, id_rs) 
                VALUES(%s, %s, %s);""", (inp[0], inp[1], inp[2],))

    elif table == 4:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Ticket"(time_of_departure, place_of_departure_and_arrival,
             id_ticket, id_rc, id_cr) VALUES(%s, %s, %s, %s, %s);""", (inp[0], inp[1], inp[2], inp[3], inp[4],))

    elif table == 5:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Train"(type_of_railway, id_train, id_rs) 
            VALUES(%s, %s, %s);""", (inp[0], inp[1], inp[2],))


def insert_rand(table, count):
    connection = connect()
    if table == 1:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Cash register"(cashier, number_of_tickets_for_sale, id_cr, id_rs)
                    VALUES( (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int))),
                    trunc(random()*100+200)::int,
                    (SELECT(select count(id_cr) from "Cash register")+1::int),
                    (SELECT id_rs FROM "Railway station" OFFSET floor(random()*(select count(id_rs) 
                    from "Railway station")) LIMIT 1));""")

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Railway carriage"(type, number_of_seats, id_rc, id_train)
                 VALUES( 
                 (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int))),
                trunc(random()*100+200)::int,
                (SELECT(select count(id_rc) from "Railway carriage")+1::int),
                (SELECT id_train FROM "Train" OFFSET floor(random()*(select count(id_train) 
                    from "Train")) LIMIT 1));""")

    elif table == 3:
        with connection.cursor() as cursor:
            for i in range(0, count):
                cursor.execute("""INSERT INTO "Railway station"(name, address, id_rs) 
                     VALUES(
                     (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int))),
                     (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            ' st.' || (trunc(random()*100)::int))),
                     (SELECT(select count(id_rs) from "Railway station")+1::int));""")

    elif table == 4:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Ticket"(time_of_departure, place_of_departure_and_arrival,
             id_ticket, id_rc, id_cr) VALUES( 
             (select (random() * (interval '21 hour')) + '2 hour'),
             (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        ' - ' || 
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int))),
             (SELECT(select count(id_ticket) from "Ticket")+1::int),
             (SELECT id_rc FROM "Railway carriage" OFFSET floor(random()*(select count(id_rc) 
                        from "Railway carriage")) LIMIT 1),
             (SELECT id_cr FROM "Cash register" OFFSET floor(random()*(select count(id_cr) 
                        from "Cash register")) LIMIT 1));""")

    elif table == 5:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Train"(type_of_railway, id_train, id_rs) 
             VALUES( 
             (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int))),
             (SELECT(select count(id_train) from "Train")+1::int),
             (SELECT id_rs FROM "Railway station" OFFSET floor(random()*(select count(id_rs) 
                    from "Railway station")) LIMIT 1));""")


def update(table, inp):
    connection = connect()

    n_id = inp[0]
    column = inp[1]
    new = inp[2]

    if table == 1:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set cashier = %s where id_cr = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set number_of_tickets_for_sale = %s where id_cr = %s;""",
                               (new, n_id,))

        elif column == 3:
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set id_rs = %s where id_cr = %s;""", (new, n_id,))

    elif table == 2:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Railway carriage" set type = %s where id_rc = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Railway carriage" set number_of_seats = %s where id_rc = %s;""", (new, n_id,))

        elif column == 3:
            with connection.cursor() as cursor:
                cursor.execute("""update "Railway carriage" set id_train = %s where id_rc = %s;""", (new, n_id,))

    elif table == 3:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Railway station" set name = %s where id_rs = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Railway station" set address = %s where id_rs = %s;""", (new, n_id,))

    elif table == 4:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set time_of_departure = %s where id_ticket = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set place_of_departure_and_arrival = %s where id_ticket = %s;""",
                               (new, n_id,))

        elif column == 3:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set id_rc = %s where id_ticket = %s;""", (new, n_id,))

        elif column == 4:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set id_cr = %s where id_ticket = %s;""", (new, n_id,))

    elif table == 5:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Train" set type_of_railway = %s where id_train = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Train" set id_rs = %s where id_train = %s;""", (new, n_id,))


def delete(table, nid):
    connection = connect()

    if table == 1:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Cash register" WHERE id_cr = %s;""", (nid,))

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Railway carriage" WHERE id_rc = %s;""", (nid,))

    elif table == 3:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Railway station" WHERE id_rs = %s;""", (nid,))

    elif table == 4:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Ticket" WHERE id_ticket = %s;""", (nid,))

    elif table == 5:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Train" WHERE id_train = %s;""", (nid,))


def select_table(table, inp):
    connection = connect()

    string = inp[0]

    if table == 1:
        if string == 1:
            n_id = inp[1]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cash register" where id_cr = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cash register";""")
                return cursor.fetchall()

    elif table == 2:
        if string == 1:
            n_id = inp[1]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Railway carriage" where id_rc = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Railway carriage";""")
                return cursor.fetchall()

    elif table == 3:
        if string == 1:
            n_id = inp[1]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Railway station" where id_rs = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Railway station";""")
                return cursor.fetchall()

    elif table == 4:
        if string == 1:
            n_id = inp[1]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Ticket" where id_ticket = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Ticket";""")
                return cursor.fetchall()

    elif table == 5:
        if string == 1:
            n_id = inp[1]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Train" where id_train = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Train";""")
                return cursor.fetchall()


def search(table, inp):
    connection = connect()

    column = inp[0]

    if table == 1:
        if column == 1:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE to_tsvector(cashier)
                                @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()
                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" 
                WHERE %s <= number_of_tickets_for_sale and number_of_tickets_for_sale <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE %s <= id_cr and id_cr <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE %s <= id_rs and id_rs <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 2:

        if column == 1:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Railway carriage" WHERE to_tsvector(type)
                                            @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()
                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Railway carriage" 
                WHERE %s <= number_of_seats and number_of_seats <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Railway carriage" WHERE %s <= id_rc and id_rc <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Railway carriage" WHERE %s <= id_train and id_train <= %s;""",
                               (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 3:
        if column == 2:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Railway station" WHERE %s <= id_rs and id_rs <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 1:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Railway station" WHERE to_tsvector(name) || to_tsvector(address)
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 4:
        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" 
                WHERE %s <= time_of_departure and time_of_departure <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE to_tsvector(place_of_departure_and_arrival)
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" 
                WHERE %s <= id_ticket and id_ticket <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" 
                WHERE %s <= id_rc and id_rc <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 5:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" 
                WHERE %s <= id_cr and id_cr <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 5:
        if column == 1:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Train" WHERE to_tsvector(type_of_railway)
                                @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Train" WHERE %s <= id_train and id_train <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Train" WHERE %s <= id_rs and id_rs <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret