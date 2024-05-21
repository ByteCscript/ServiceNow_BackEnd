from sqlalchemy import create_engine, MetaData

   # Conexión a MySQL
   # Importante : La ruta debe estar muy bien escrita para su funcionamiento
url_db = "mysql+pymysql://root:admin@localhost:3306/helpdesk"
engine = create_engine(url_db)

meta = MetaData()

conn = engine.connect()

