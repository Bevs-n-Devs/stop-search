import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(
    os.environ["STOPSEARCH_DB"],
    # connect_args={'check_same_thread': False},
    pool_pre_ping=True  # Optional: enable pool_pre_ping to prevent MySQL server has gone away error
)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)
LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine
)

Base: declarative_base = declarative_base()
Base.query = db_session.query_property()

# initialise database
def init_db():
    from stopSearch.stopSearch_database.models import Base
    Base.metadata.create_all(bind=engine)

    # Create default data if it doesn't exist
    from stopSearch.stopSearch_database.models import QuestionReportType
    session = db_session()
    if not session.query(QuestionReportType).first():
        default_data = [
            QuestionReportType(reportType='Type1'),
            QuestionReportType(reportType='Type2'),
            # Add more default data as needed
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
