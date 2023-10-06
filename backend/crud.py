from sqlalchemy.orm import Session

from . import models, schemas


def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(email=client.email, login=client.login, password=client.password, name=client.name,
                              phone_num=client.phone_num)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def create_table(db: Session, table: schemas.TableCreate):
    db_table = models.Table(num_of_ppl=table.num_of_ppl)
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def get_table(db: Session, table_id: int):
    return db.query(models.Table).filter(models.Table.id == table_id).first()


def get_reservation(db: Session, reservation_id: int):
    return db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()


def create_table_reservation(db: Session, reservation: schemas.ReservationCreate, table_id: int, client_id: int):
    db_reservation = models.Reservation(**reservation.model_dump(), table_id=table_id, client_id=client_id)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation