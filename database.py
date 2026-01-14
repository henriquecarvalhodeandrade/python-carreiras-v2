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
            return vagas

    except Exception as e:
        return(f"Erro na conexão: {e}")

def carrega_vaga_db(id):
    try:
        with engine.connect() as conn:
            resultado = conn.execute(text(
                f"SELECT * FROM vagas WHERE id = :val"
            ), 
                {"val": id}
            )
            
            registro = resultado.mappings().all()
            
            if len(registro) == 0:
                return None
                
            else:
                return dict(registro[0])
            
    except Exception as e:
        return(f"Erro na conexão: {e}")