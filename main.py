from sqlalchemy.orm import joinedload
from sqlalchemy import and_
from datetime import datetime
from hw.db import session
from hw.models import Contact
from faker import Faker


fake = Faker()

def get_contacts():
        students = session.query(Contact).all()
        for s in students:
            print(vars(s))

def add_contact():
    contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
        )
    session.add(contact)
    session.commit()


def update_contact(id, first_name, last_name, email, cell_phone, address):
    contact = session.query(Contact).filter(Contact.id == id)
    contact.update({'first_name': first_name, 'last_name': last_name, 'email': email, 'address': address, 'cell_phone': cell_phone})
    session.commit()


def remove_contact(id):
    contact = session.query(Contact).filter(Contact.id == id).delete()
    session.commit()


if __name__ == '__main__':
    first_name=fake.first_name()
    last_name=fake.last_name()
    email=fake.ascii_free_email()
    cell_phone=fake.phone_number()
    address=fake.address()

    remove_contact(10)
    
    
    