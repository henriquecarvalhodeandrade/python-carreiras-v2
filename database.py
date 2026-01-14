import os
from sqlalchemy import create_engine, text

# O Replit já injeta os Secrets no environment
db_url = os.environ.get('DATABASE_URL')

if not db_url:
    raise ValueError("DATABASE_URL não configurada nos Secrets!")

# Criando a engine com configurações de robustez
engine = create_engine(
    db_url,
    connect_args={
        "sslmode": "require",
    }
)

def carrega_vagas_db():
    try:
        with engine.connect() as conn:
            resultado = conn.execute(text("SELECT * FROM vagas"))

            vagas = []
            for vaga in resultado.all():
                vagas.append(vaga._asdict())
            print(vagas)

    except Exception as e:
        print(f"Erro na conexão: {e}")