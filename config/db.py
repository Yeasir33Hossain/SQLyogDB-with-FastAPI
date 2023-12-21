from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:admin@localhost/fast_api")
meta = MetaData()
conn = engine.connect()