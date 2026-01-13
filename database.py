import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

# No Supabase, a URL geralmente termina com ?sslmode=require 
# ou você configura via código como abaixo
db_url = os.getenv('DATABASE_URL')

if not db_url:
    raise ValueError("DATABASE_URL não encontrada!")

# Para PostgreSQL, geralmente não precisamos do ssl:{} vazio do MySQL
# Se der erro de certificado, use: connect_args={"sslmode": "require"}
engine = create_engine(db_url)

try:
    with engine.connect() as conn:
        # O text() é obrigatório no SQLAlchemy 2.0+
        resultado = conn.execute(text("SELECT * FROM vagas"))
        print(resultado.all())
except Exception as e:
    print(f"Erro na conexão: {e}")