import os
from sqlalchemy import create_engine, text

db_url = os.environ.get('DATABASE_URL')

if db_url is None:
    raise ValueError("DATABASE_URL não configurada nos Secrets!")

engine = create_engine(db_url)

with engine.connect() as conn:
    resultado = conn.execute(text("SELECT * FROM vagas"))
    print(resultado.all())
    