import os
import csv
from model import app, db, Person

persons=[]
base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, 'persons.csv'), 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        person = Person(
            name=row['name'],
            phone_number=row['phone_number'],
            age=row['age'],
        )
        persons.append(person)

with app.app_context():
    db.session.add_all(persons)
    db.session.commit()

