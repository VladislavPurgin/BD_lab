import time
import datetime
from faker import Faker
from random import *
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Interval, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:v2l7a0d9@localhost:5432/Vlad', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

fake = Faker()


class Cash_register(Base):
    __tablename__ = 'Cash_register'
    cashier = Column(String)
    number_of_tickets_for_sale = Column(Integer)
    id_cr = Column(Integer, primary_key=True)
    id_rs = Column(Integer, ForeignKey('Railway_station.id_rs'))

    tickets = relationship('Ticket')

    def __init__(self, cashier: str, number_of_tickets_for_sale: int, id_cr: int, id_rs: int):
        self.cashier = cashier
        self.number_of_tickets_for_sale = number_of_tickets_for_sale
        self.id_cr = id_cr
        self.id_rs = id_rs


class Railway_carriage(Base):
    __tablename__ = 'Railway_carriage'
    type = Column(String)
    number_of_seats = Column(Integer)
    id_rc = Column(Integer, primary_key=True)
    id_train = Column(Integer, ForeignKey('Train.id_train'))

    tickets = relationship('Ticket')

    def __init__(self, type_: str, number_of_seats: int, id_rc: int, id_train: int):
        self.type = type_
        self.number_of_seats = number_of_seats
        self.id_rc = id_rc
        self.id_train = id_train


class Railway_station(Base):
    __tablename__ = 'Railway_station'
    name = Column(String)
    address = Column(String)
    id_rs = Column(Integer, primary_key=True)

    crs = relationship('Cash_register')
    trains = relationship('Train')

    def __init__(self, name: str, address: str, id_rs: int):
        self.name = name
        self.address = address
        self.id_rs = id_rs


class Ticket(Base):
    __tablename__ = 'Ticket'
    time_of_departure = Column(Interval)
    place_of_departure_and_arrival = Column(String)
    id_ticket = Column(Integer, primary_key=True)
    id_rc = Column(Integer, ForeignKey('Railway_carriage.id_rc'))
    id_cr = Column(Integer, ForeignKey('Cash_register.id_cr'))

    def __init__(self, time_of_departure: datetime.time, place_of_departure_and_arrival: str, id_ticket: int,
                 id_rc: int, id_cr: int):
        self.time_of_departure = time_of_departure
        self.place_of_departure_and_arrival = place_of_departure_and_arrival
        self.id_ticket = id_ticket
        self.id_rc = id_rc
        self.id_cr = id_cr


class Train(Base):
    __tablename__ = 'Train'
    type_of_railway = Column(String)
    id_train = Column(Integer, primary_key=True)
    id_rs = Column(Integer, ForeignKey('Railway_station.id_rs'))

    rcs = relationship('Railway_carriage')

    def __init__(self, type_of_railway: str, id_train: int, id_rs: int):
        self.type_of_railway = type_of_railway
        self.id_train = id_train
        self.id_rs = id_rs


def connect():
    Base.metadata.create_all(engine)


def insert(table, inp):
    if table == 1:
        tr = Cash_register(inp[0], inp[1], inp[2], inp[3])
        session.add(tr)
        session.commit()

    elif table == 2:
        tr = Railway_carriage(inp[0], inp[1], inp[2], inp[3])
        session.add(tr)
        session.commit()

    elif table == 3:
        tr = Railway_station(inp[0], inp[1], inp[2])
        session.add(tr)
        session.commit()

    elif table == 4:
        tr = Ticket(inp[0], inp[1], inp[2], inp[3], inp[4])
        session.add(tr)
        session.commit()

    elif table == 5:
        tr = Train(inp[0], inp[1], inp[2])
        session.add(tr)
        session.commit()


def insert_rand(table, count):
    if table == 1:
        tr = Cash_register(fake.name(),
                           randint(150, 400),
                           (session.query(Cash_register.id_cr).count() + 1),
                           randrange(1, session.query(Railway_station.id_rs).count()))
        session.add(tr)
        session.commit()

    elif table == 2:
        tr = Railway_carriage(fake.word(), randint(100, 1000),
                              (session.query(Railway_carriage.id_rc).count() + 1),
                              randrange(1, session.query(Train.id_train).count()))
        session.add(tr)
        session.commit()

    elif table == 3:
        for i in range(0, count):
            tr = Railway_station(fake.word(), fake.address(),
                                 (session.query(Railway_station.id_rs).count() + 1))
            session.add(tr)
            session.commit()

    elif table == 4:
        t = datetime.time(randrange(1, 3), randrange(1, 59))
        place = fake.country() + " - " + fake.country()
        tr = Ticket(t, place,
                    (session.query(Ticket.id_ticket).count() + 1),
                    randrange(1, session.query(Railway_carriage.id_rc).count()),
                    randrange(1, session.query(Cash_register.id_cr).count()))
        session.add(tr)
        session.commit()

    elif table == 5:
        tr = Train(fake.word(), (session.query(Train.id_train).count() + 1),
                   randrange(1, session.query(Railway_station.id_rs).count()), )
        session.add(tr)
        session.commit()


def update(table, inp):

    n_id = inp[0]
    column = inp[1]
    new = inp[2]

    if table == 1:
        if column == 1:
            tr = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
            tr.cashier = new
            session.commit()

        elif column == 2:
            tr = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
            tr.number_of_tickets_for_sale = new
            session.commit()

        elif column == 3:
            tr = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
            tr.id_rs = new
            session.commit()

    elif table == 2:
        if column == 1:
            tr = session.query(Railway_carriage).filter(Railway_carriage.id_rc == int(n_id)).first()
            tr.type = new
            session.commit()

        elif column == 2:
            tr = session.query(Railway_carriage).filter(Railway_carriage.id_rc == int(n_id)).first()
            tr.number_of_seats = new
            session.commit()

        elif column == 3:
            tr = session.query(Railway_carriage).filter(Railway_carriage.id_rc == int(n_id)).first()
            tr.id_train = new
            session.commit()

    elif table == 3:
        if column == 1:
            tr = session.query(Railway_station).filter(Railway_station.id_rs == int(n_id)).first()
            tr.name = new
            session.commit()

        elif column == 2:
            tr = session.query(Railway_station).filter(Railway_station.id_rs == int(n_id)).first()
            tr.address = new
            session.commit()

    elif table == 4:
        if column == 1:
            tr = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            tr.time_of_departure = new
            session.commit()

        elif column == 2:
            tr = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            tr.place_of_departure_and_arrival = new
            session.commit()

        elif column == 3:
            tr = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            tr.id_rc = new
            session.commit()

        elif column == 4:
            tr = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            tr.id_cr = new
            session.commit()

    elif table == 5:
        if column == 1:
            tr = session.query(Train).filter(Train.id_train == int(n_id)).first()
            tr.type_of_railway = new
            session.commit()

        elif column == 2:
            tr = session.query(Train).filter(Train.id_train == int(n_id)).first()
            tr.id_rs = new
            session.commit()


def delete(table, n_id):

    if table == 1:
        tr = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
        session.delete(tr)
        session.commit()

    elif table == 2:
        tr = session.query(Railway_carriage).filter(Railway_carriage.id_rc == int(n_id)).first()
        session.delete(tr)
        session.commit()

    elif table == 3:
        tr = session.query(Railway_station).filter(Railway_station.id_rs == int(n_id)).first()
        session.delete(tr)
        session.commit()

    elif table == 4:
        tr = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
        session.delete(tr)
        session.commit()

    elif table == 5:
        tr = session.query(Train).filter(Train.id_train == int(n_id)).first()
        session.delete(tr)
        session.commit()


def select_table(table, inp):

    string = inp[0]

    if table == 1:
        if string == 1:
            n_id = inp[1]
            tr = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
            returning = [tr.cashier, tr.number_of_tickets_for_sale, n_id, tr.id_rs]
            return returning

        elif string == 2:
            tr = session.query(Cash_register)
            return tr

    elif table == 2:
        if string == 1:
            n_id = inp[1]
            tr = session.query(Railway_carriage).filter(Railway_carriage.id_rc == int(n_id)).first()
            returning = [tr.type, tr.number_of_seats, n_id, tr.id_train]
            return returning

        elif string == 2:
            tr = session.query(Railway_carriage)
            return tr

    elif table == 3:
        if string == 1:
            n_id = inp[1]
            tr = session.query(Railway_station).filter(Railway_station.id_rs == int(n_id)).first()
            returning = [tr.name, tr.address, n_id]
            return returning

        elif string == 2:
            tr = session.query(Railway_station)
            return tr

    elif table == 4:
        if string == 1:
            n_id = inp[1]
            tr = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            returning = [tr.time_of_departure, tr.place_of_departure_and_arrival, n_id, tr.id_rc, tr.id_cr]
            return returning

        elif string == 2:
            tr = session.query(Ticket)
            return tr

    elif table == 5:
        if string == 1:
            n_id = inp[1]
            tr = session.query(Train).filter(Train.id_train == int(n_id)).first()
            returning = [tr.type_of_railway, n_id, tr.id_rs]
            return returning

        elif string == 2:
            tr = session.query(Train)
            return tr


def search(table, inp):

    column = inp[0]

    if table == 1:
        if column == 1:
            txt = inp[1]
            start_t = time.time()

            tr = session.query(Cash_register).filter(Cash_register.cashier == txt).all()

            finish = time.time()
            search_duration = finish - start_t
            ret = [tr, search_duration]
            return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Cash_register).filter(
                and_(Cash_register.number_of_tickets_for_sale >= int(a)),
                Cash_register.number_of_tickets_for_sale <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Cash_register).filter(
                and_(Cash_register.id_cr >= int(a)), Cash_register.id_cr <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Cash_register).filter(
                and_(Cash_register.id_rs >= int(a)), Cash_register.id_rs <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

    elif table == 2:

        if column == 1:
            txt = inp[1]
            start_t = time.time()

            tr = session.query(Railway_carriage).filter(Railway_carriage.type == txt).all()

            finish = time.time()
            search_duration = finish - start_t
            ret = [tr, search_duration]
            return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Railway_carriage).filter(
                and_(Railway_carriage.number_of_seats >= int(a)), Railway_carriage.number_of_seats <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Railway_carriage).filter(
                and_(Railway_carriage.id_rc >= int(a)), Railway_carriage.id_rc <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Railway_carriage).filter(
                and_(Railway_carriage.id_train >= int(a)), Railway_carriage.id_train <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

    elif table == 3:

        if column == 1:
            txt = inp[1]
            start_t = time.time()

            tr = session.query(Railway_station).filter(Railway_station.name == txt).all()

            finish = time.time()
            search_duration = finish - start_t
            ret = [tr, search_duration]
            return ret

        elif column == 2:
            txt = inp[1]
            start_t = time.time()

            tr = session.query(Railway_station).filter(Railway_station.address == txt).all()

            finish = time.time()
            search_duration = finish - start_t
            ret = [tr, search_duration]
            return ret
        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Railway_station).filter(
                and_(Railway_station.id_rs >= int(a)), Railway_station.id_rs <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

    elif table == 4:
        if column == 1:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Ticket).filter(
                and_(Ticket.time_of_departure >= a), Ticket.time_of_departure <= b
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

        elif column == 2:
            txt = inp[1]
            start_t = time.time()

            tr = session.query(Ticket).filter(Ticket.place_of_departure_and_arrival == txt).all()

            finish = time.time()
            search_duration = finish - start_t
            ret = [tr, search_duration]
            return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Ticket).filter(
                and_(Ticket.id_ticket >= int(a)), Ticket.id_ticket <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Ticket).filter(
                and_(Ticket.id_rc >= int(a)), Ticket.id_rc <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

        elif column == 5:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Ticket).filter(
                and_(Ticket.id_cr >= int(a)), Ticket.id_cr <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

    elif table == 5:
        if column == 1:
            txt = inp[1]
            start_t = time.time()

            tr = session.query(Train).filter(Train.type_of_railway == txt).all()

            finish = time.time()
            search_duration = finish - start_t
            ret = [tr, search_duration]
            return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Train).filter(
                and_(Train.id_train >= int(a)), Train.id_train <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            tr = session.query(Train).filter(
                and_(Train.id_rs >= int(a)), Train.id_rs <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [tr, search_duration]
            return ret
