from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from stopSearch.stopSearch_database.extension import Base

class QuestionReportType(Base):
    __tablename__ = 'questionReportType'
    questionReportTypeID = Column(Integer, primary_key=True)
    reportType = Column(String(8))
