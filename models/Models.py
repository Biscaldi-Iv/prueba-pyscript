from enum import unique
from typing import Dict
from sqlalchemy import Integer, String, Column, Sequence
from database import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, Sequence('user_seq_id'), primary_key=True)
    username = Column(String, unique=True)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self) -> str:
        return f'{self.id},{self.username},{self.fullname};'


class Client(Base):
    __tablename__ = 'Clients'
    id = Column(Integer, Sequence('cli_seq_id'), primary_key=True)
    bs_name = Column(String, unique=True)

    def rep(self) -> Dict:
        return {'id': self.id, 'bs_name': self.bs_name}
