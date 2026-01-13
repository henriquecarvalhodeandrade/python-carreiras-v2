import os
from sqlalchemy import create_engine, text
# No Replit, você não precisa do load_dotenv() se estiver usando os Secrets do painel lateral, 
# mas mantê-lo não faz mal.

db_url = os.environ.get('DATABASE_URL')

if not db_url:
    raise ValueError("DATABASE_URL não configurada nos Secrets!")

# Adicionamos o connect_args para garantir o SSL exigido pelo Supabase
engine = create_engine(
    db_url,
    connect_args={
        "sslmode": "require"
    }
)

try:
    with engine.connect() as conn:
        print("Conexão estabelecida com sucesso!")
        resultado = conn.execute(text("SELECT * FROM vagas"))
        # Usar mappings().all() transforma cada linha em um dicionário, facilitando a leitura
        print(resultado.mappings().all())
except Exception as e:
    print(f"Erro na conexão: {e}")