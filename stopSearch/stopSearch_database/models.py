from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from stopSearch.stopSearch_database.extension import Base

# questions
class QuestionReportType(Base):
    __tablename__ = 'questionReportType'
    questionReportTypeID = Column(Integer, primary_key=True)
    reportType = Column(String(8)) # witness / victim 

class QuestionLocationType(Base):
    __tablename__ = 'questionLocationType'
    questionLocationTypeID = Column(Integer, primary_key=True)
    locationType = Column(String(20)) # automatic address / manual address

class QuestionVictimsInvolved(Base):
    __tablename__ = 'questionVictimsInvolved'
    questionVictimsInvolvedID = Column(Integer, primary_key=True)
    victimsInvolved = Column(String(8))

class QuestionNumberOfPolice(Base):
    __tablename__ = 'questionNumberOfPolice'
    questionNumberOfPoliceID = Column(Integer, primary_key=True)
    numberOfPolice = Column(String(8))

class QuestionSearchReason(Base):
    __tablename__ = 'questionSearchReason'
    questionsearchTypeID = Column(Integer, primary_key=True)
    searchReason = Column(String(50))

class QuestionSearchType(Base):
    __tablename__ = 'questionSearchType'
    questionSearchTypeID = Column(Integer, primary_key=True)
    searchType = Column(String(10)) # moderate / aggressive

class QuestionVictimAge(Base):
    __tablename__ = 'questionVictimAge'
    questionVictimAgeID = Column(Integer, primary_key=True)
    victimAge = Column(String(8))

class QuestionVictimGender(Base):
    __tablename__ = 'questionVictimGender'
    questionVictimGenderID = Column(Integer, primary_key=True)
    victimGender = Column(String(30))

class QuestionVictimRace(Base):
    __tablename__ = 'questionVictimRace'
    questionVictimRaceID = Column(Integer, primary_key=True)
    victimRace = Column(String(30))

# answers
class ReportData(Base):
    __tablename__ = 'reportData'
    reportDataID = Column(Integer, primary_key=True)
    reportEmail = Column(String(255), nullable=False, unique=False)
    reportedBy = relationship('ReportedBy', backref='reported_by')
    victimInformation = relationship('VictimInformation', backref='victim_info')
    publicRelations = relationship('PublicRelations', backref='public_relations')
    policeInformation = relationship('PoliceInformation', backref='police_info')

class ReportedBy(Base):
    __tablename__ = 'reportedBy'
    reportedByID = Column(Integer, primary_key=True, autoincrement=True)
    confirmEmail = Column(String(255), nullable=False, unique=False)
    reportType = relationship('ReportType', backref='report_type')
    reportDate = relationship('ReportDate', backref='report_date')
    reportDataID = Column(Integer, ForeignKey('reportData.reportDataID'))

class VictimInformation(Base):
    __tablename__ = 'victimInformation'
    victimInformationID = Column(Integer, primary_key=True, autoincrement=True)
    numberOfVictims = Column(String(8), nullable=False)
    victimAge = Column(String(8), nullable=False)
    victimGender = Column(String(25), nullable=False)
    victimRace = Column(String(10), nullable=False)
    reportDataID = Column(Integer, ForeignKey('reportData.reportDataID'))

class PublicRelations(Base):
    __tablename__ = 'publicRelations'
    publicRelationsID = Column(Integer, primary_key=True, autoincrement=True)
    searchReason = Column(String(55), nullable=False)
    searchType = Column(String(10), nullable=False)
    additionalNotes = Column(Text, nullable=True)
    incidentAddress = relationship('IncidentAddress', backref='incident_address')
    reportDataID = Column(Integer, ForeignKey('reportData.reportDataID'))

class PoliceInformation(Base):
    __tablename__ = 'policeInformation'
    policeInformationID = Column(Integer, primary_key=True, autoincrement=True)
    numberOfPolice = Column(String(8), nullable=False)
    obtainPoliceInfo = Column(Integer, nullable=False) # 0 = False, 1 = True
    officerInformation = relationship('OfficerInformation', backref='officer_information')
    reportDataID = Column(Integer, ForeignKey('reportData.reportDataID'))

class ReportType(Base):
    __tablename__ = 'reportType'
    reportTypeID = Column(Integer, primary_key=True, autoincrement=True)
    reportType = Column(String(9), nullable=False)
    reportedByID = Column(Integer, ForeignKey('reportedBy.reportedByID'))

class ReportDate(Base):
    __tablename__ = 'reportDate'
    reportDateID = Column(Integer, primary_key=True, autoincrement=True)
    reportDate = Column(String(20), nullable=False)
    formattedDay = Column(String(4), nullable=False)
    formattedWeekday = Column(String(9), nullable=False)
    formattedMonth = Column(String(9), nullable=False)
    formattedYear = Column(String(4), nullable=False)
    formattedTime = Column(String(8), nullable=False)
    reportedByID = Column(Integer, ForeignKey('reportedBy.reportedByID'))

class IncidentAddress(Base):
    __tablename__ = 'incidentAddress'
    incidentAddressID = Column(Integer, primary_key=True, autoincrement=True)
    addressType = Column(String(16), nullable=False)  # automaticAddress or manualAddress
    streetName = Column(String(50), nullable=False)
    townOrCity = Column(String(50), nullable=False)
    country = Column(String(50), default='UK')
    mapCoordinates = relationship('MapCoordinates', backref='map_coordinates')
    publicRelationsID = Column(Integer, ForeignKey('publicRelations.publicRelationsID'))



class OfficerInformation(Base):
    __tablename__ = 'officerInformation'
    officerInformationID = Column(Integer, primary_key=True, autoincrement=True)
    badgeNumber =  Column(String(10), nullable=True)
    officerName =  Column(String(50), nullable=True)
    policeStation =  Column(String(50), nullable=True)
    policeInformationID = Column(Integer, ForeignKey('policeInformation.policeInformationID'))
    
class MapCoordinates(Base):
    __tablename__ = 'mapCoordinates'
    mapCoordinatesID = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    incidentAddressID = Column(Integer, ForeignKey('incidentAddress.incidentAddressID'))
