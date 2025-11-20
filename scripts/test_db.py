from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()
uri = os.getenv('DEV_DATABASE_URI')
print('Using DEV_DATABASE_URI:', uri)
try:
    engine = create_engine(uri, connect_args={'connect_timeout': 5})
    with engine.connect() as conn:
        print('PostgreSQL connection OK')
except Exception as ex:
    print('Error:', type(ex).__name__, ex)
