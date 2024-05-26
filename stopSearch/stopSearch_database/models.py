from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from stopSearch.stopSearch_database.extension import Base

# questions
class QuestionReportType(Base):
    __tablename__ = 'question_report_type'
    question_report_type_id = Column(Integer, primary_key=True)
    report_type = Column(String(8)) # witness / victim 

class QuestionLocationType(Base):
    __tablename__ = 'question_location_type'
    question_location_type_id = Column(Integer, primary_key=True)
    location_type = Column(String(20)) # automatic address / manual address

class QuestionVictimsInvolved(Base):
    __tablename__ = 'question_victims_involved'
    question_victims_involved_id = Column(Integer, primary_key=True)
    victims_involved = Column(String(8))

class QuestionNumberOfPolice(Base):
    __tablename__ = 'question_number_of_police'
    question_number_of_police_id = Column(Integer, primary_key=True)
    number_of_police = Column(String(8))

class QuestionSearchReason(Base):
    __tablename__ = 'question_serarch_type'
    question_serarch_type_id = Column(Integer, primary_key=True)
    search_reason = Column(String(85))

class QuestionSearchType(Base):
    __tablename__ = 'question_search_type'
    question_search_type_id = Column(Integer, primary_key=True)
    search_type = Column(String(10)) # moderate / aggressive

class QuestionVictimAge(Base):
    __tablename__ = 'question_victim_age'
    question_victim_age_id = Column(Integer, primary_key=True)
    victim_age = Column(String(8))

class QuestionVictimGender(Base):
    __tablename__ = 'question_victim_gender'
    question_victim_gender_id = Column(Integer, primary_key=True)
    victim_gender = Column(String(30))

class QuestionVictimRace(Base):
    __tablename__ = 'question_victim_race'
    question_victim_race_id = Column(Integer, primary_key=True)
    victim_race = Column(String(30))

# answers
class ReportData(Base):
    __tablename__ = 'report_data'
    report_data_id = Column(Integer, primary_key=True)
    report_email = Column(String(255), nullable=False, unique=False)
    reported_by = relationship('ReportedBy', backref='reported_by_')
    victim_information = relationship('VictimInformation', backref='victim_info_')
    public_relations = relationship('PublicRelations', backref='public_relations_')
    police_information = relationship('PoliceInformation', backref='police_info_')

class ReportedBy(Base):
    __tablename__ = 'reported_by'
    reported_by_id = Column(Integer, primary_key=True, autoincrement=True)
    confirm_email = Column(String(255), nullable=False, unique=False)
    report_type = relationship('ReportType', backref='report_type_')
    report_date = relationship('ReportDate', backref='report_date_')
    report_data_id = Column(Integer, ForeignKey('report_data.report_data_id'))

class VictimInformation(Base):
    __tablename__ = 'victim_information'
    victim_information_id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_victims = Column(String(8), nullable=False)
    victim_age = Column(String(8), nullable=False)
    victim_gender = Column(String(25), nullable=False)
    victim_race = Column(String(10), nullable=False)
    report_data_id = Column(Integer, ForeignKey('report_data.report_data_id'))

class PublicRelations(Base):
    __tablename__ = 'public_relations'
    public_relations_id = Column(Integer, primary_key=True, autoincrement=True)
    search_reason = Column(String(55), nullable=False)
    search_type = Column(String(10), nullable=False)
    additional_notes = Column(Text, nullable=True)
    incident_address = relationship('IncidentAddress', backref='incident_address_')
    report_data_id = Column(Integer, ForeignKey('report_data.report_data_id'))

class PoliceInformation(Base):
    __tablename__ = 'police_information'
    police_information_id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_police = Column(String(8), nullable=False)
    obtain_police_info = Column(Integer, nullable=False) # 0 = False, 1 = True
    officer_information = relationship('OfficerInformation', backref='officer_information_')
    report_data_id = Column(Integer, ForeignKey('report_data.report_data_id'))

class ReportType(Base):
    __tablename__ = 'report_type'
    report_type_id = Column(Integer, primary_key=True, autoincrement=True)
    report_type = Column(String(9), nullable=False)
    reported_by_id = Column(Integer, ForeignKey('reported_by.reported_by_id'))

class ReportDate(Base):
    __tablename__ = 'report_date'
    report_date_id = Column(Integer, primary_key=True, autoincrement=True)
    report_date = Column(String(20), nullable=False)
    formatted_day = Column(String(4), nullable=False)
    formatted_weekday = Column(String(9), nullable=False)
    formatted_month = Column(String(9), nullable=False)
    formatted_year = Column(String(4), nullable=False)
    formatted_time = Column(String(8), nullable=False)
    reported_by_id = Column(Integer, ForeignKey('reported_by.reported_by_id'))

class IncidentAddress(Base):
    __tablename__ = 'incident_address'
    incident_address_id = Column(Integer, primary_key=True, autoincrement=True)
    addressType = Column(String(16), nullable=False)  # automaticAddress or manualAddress
    street_name = Column(String(50), nullable=False)
    town_or_city = Column(String(50), nullable=False)
    country = Column(String(50), default='UK')
    map_coordinates = relationship('MapCoordinates', backref='map_coordinates_')
    public_relations_id = Column(Integer, ForeignKey('public_relations.public_relations_id'))

class OfficerInformation(Base):
    __tablename__ = 'officer_information'
    officer_information_id = Column(Integer, primary_key=True, autoincrement=True)
    badge_number =  Column(String(10), nullable=True)
    officer_name =  Column(String(50), nullable=True)
    police_station =  Column(String(50), nullable=True)
    police_information_id = Column(Integer, ForeignKey('police_information.police_information_id'))
    
class MapCoordinates(Base):
    __tablename__ = 'map_coordinates'
    map_coordinates_id = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    incident_address_id = Column(Integer, ForeignKey('incident_address.incident_address_id'))
