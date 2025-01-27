import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase

base_dir = os.path.dirname(__file__)

app=Flask(__name__)

database_path=os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{database_path}'

class Base(DeclarativeBase):
  pass
db = SQLAlchemy(app,model_class=Base)

class Person(Base):
    __tablename__ = 'person'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String)
    phone_number: Mapped[str] = mapped_column(db.String)
    age: Mapped[int] = mapped_column(db.Integer)
    def __str__(self):
       return f"id={self.id}, name={self.name}, phone_number={self.phone_number}, age={self.age}"

    print(db)
    print(db.metadata.tables)
       

