from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://azdyzndhooeuma:a80beddd39d36c61c71f8676574b4e4aca7ed4f41c8d155a61396378c4a19d75@ec2-44-205-63-142.compute-1.amazonaws.com:5432/d22i1tna67qvni"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
