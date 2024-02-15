from sqlalchemy.engine import create_engine
from db import session
from faker import Faker

from models import Contact

fake = Faker()
def create_contacts():
    for _ in range(10):
        teacher = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
        )
        session.add(teacher)
    session.commit()

if __name__ == '__main__':
    create_contacts()