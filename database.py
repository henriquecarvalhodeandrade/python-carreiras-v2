from sqlalchemy import create_engine, text
import os

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
  with engine.connect() as conn:
    resultado = conn.execute(text("SELECT * FROM vagas"))
    vagas = []
    for vaga in resultado.all():
      vagas.append(vaga._asdict())
    return vagas

def carrega_vaga_db(id):
  with engine.connect() as conn:
    resultado = conn.execute(text(f"SELECT * FROM vagas WHERE id = :val"),
                             {"val": id})
    registro = resultado.mappings().all()
    if len(registro) == 0:
      return None
    else:
      return dict(registro[0])

def adiciona_inscricao(id_vaga, dados):
  with engine.connect() as conn:
    query = text(
      f"INSERT INTO inscricoes(vaga_id, nome, email, linkedin, experiencia) VALUES(:vaga_id, :nome, :email, :linkedin, :experiencia)"
    )
    conn.execute(
      query, {
        'vaga_id': id_vaga,
        'nome': dados['nome'],
        'email': dados['email'],
        'linkedin': dados['linkedin'],
        'experiencia': dados['experiencia']
      })
