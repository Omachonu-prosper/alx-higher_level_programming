#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy import select
from model_state import Base, State

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(
        f'mysql://{user}:{passwd}@{host}:{port}/{db}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    state = engine.execute(select(State)).first()
    if state:
        print(f'{state.id}: {state.name}')
