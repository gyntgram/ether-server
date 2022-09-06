from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://binplgqgsaqujo:98f906e6dd2c78a019e06fc9d1704773bd1eaec089b3c4b0a48b66b4b6fce891@ec2-34-233-115-14.compute-1.amazonaws.com:5432/de5h5s3rug5hkk"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
