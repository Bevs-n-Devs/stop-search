from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float, JSON
from sqlalchemy.orm import relationship
from stopSearch.stopSearch_database.extension import Base

# questions
class QuestionReportQuestions(Base):
    __tablename__ = 'question_report_questions'
    question_id = Column(Integer, primary_key=True)
    question_name = Column(String(500))

class QuestionReportType(Base):
    __tablename__ = 'question_report_type'
    question_report_type_id = Column(Integer, primary_key=True)
    report_type_options = Column(String(8)) # witness / victim 

class QuestionLocationType(Base):
    __tablename__ = 'question_location_type'
    question_location_type_id = Column(Integer, primary_key=True)
    location_type_options = Column(String(20)) # automatic address / manual address

class QuestionVictimsInvolved(Base):
    __tablename__ = 'question_victims_involved'
    question_victims_involved_id = Column(Integer, primary_key=True)
    victims_involved_options = Column(String(20))

class QuestionNumberOfPolice(Base):
    __tablename__ = 'question_number_of_police'
    question_number_of_police_id = Column(Integer, primary_key=True)
    number_of_police_options = Column(String(20))

class QuestionSearchReason(Base):
    __tablename__ = 'question_search_reason'
    question_search_reason_id = Column(Integer, primary_key=True)
    search_reason_options = Column(String(85))

class QuestionSearchType(Base):
    __tablename__ = 'question_search_type'
    question_search_type_id = Column(Integer, primary_key=True)
    search_type_options = Column(String(10)) # moderate / aggressive

class QuestionVictimAge(Base):
    __tablename__ = 'question_victim_age'
    question_victim_age_id = Column(Integer, primary_key=True)
    victim_age_options = Column(String(20))

class QuestionVictimGender(Base):
    __tablename__ = 'question_victim_gender'
    question_victim_gender_id = Column(Integer, primary_key=True)
    victim_gender_options = Column(String(30))

class QuestionVictimRace(Base):
    __tablename__ = 'question_victim_race'
    question_victim_race_id = Column(Integer, primary_key=True)
    victim_race_options = Column(String(75))

# TODO: Add extra questions to database and update in answers tables
#       i.e.  QuestionBodyCamera            ->     PoliceInformation
#             QuestionSearchOutcome         ->     PublicRelations 
#             QuestionOfficerInteractions   ->     OfficerInformation
class QuestionBodyCamera(Base):
    __tablename__ = 'question_body_camera'
    question_body_cam_id = Column(Integer, primary_key=True)
    body_camera_options = Column(String(10)) # Unknown, yes, no

class QuestionSearchOutcome(Base):
    __tablename__= 'question_search_outcome'
    question_search_outcome_id = Column(Integer, primary_key=True)
    search_outcome_options = Column(String(30))  # Unknown, No Further Action (NFA), Item Seized, Arrest, Warning or Caution Issued, Fixed Penalty Notice, Summons to Court, Community Resolution, Referral to Other Agencies

class QuestionOfficerInteraction(Base):
    __tablename__ = 'question_officer_interaction'
    officer_interaction_id = Column(Integer, primary_key=True)
    officer_interaction_options = Column(String(45))

# answers
class ReportData(Base):
    __tablename__ = 'report_data'
    report_data_id = Column(Integer, primary_key=True)
    report_email = Column(String(255), nullable=False, unique=False)
    reported = relationship('ReportedBy', backref='reported_by_')
    victim_info = relationship('VictimInformation', backref='victim_information_')
    public = relationship('PublicRelations', backref='public_relations_')
    police = relationship('PoliceInformation', backref='police_information_')

class ReportedBy(Base):
    __tablename__ = 'reported_by'
    reported_by_id = Column(Integer, primary_key=True, autoincrement=True)
    confirm_email = Column(String(255), nullable=False, unique=False)
    f_type = relationship('FormType', backref='form_type_')
    f_date = relationship('ReportDate', backref='form_date_')
    report_data_id = Column(Integer, ForeignKey('report_data.report_data_id'))

class VictimInformation(Base):
    __tablename__ = 'victim_information'
    victim_information_id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_victims = Column(String(25), nullable=False)
    victim_age = Column(String(25), nullable=False)
    victim_gender = Column(String(25), nullable=False)
    victim_race = Column(String(60), nullable=False)
    report_data_id = Column(Integer, ForeignKey('report_data.report_data_id'))

class PublicRelations(Base):
    __tablename__ = 'public_relations'
    public_relations_id = Column(Integer, primary_key=True, autoincrement=True)
    search_reason = Column(String(55), nullable=False)
    search_type = Column(String(10), nullable=False)
    search_outcome = Column(String(30), nullable=False) # NEW Unknown, No Further Action (NFA), Item Seized, Arrest, Warning or Caution Issued, Fixed Penalty Notice, Summons to Court, Community Resolution, Referral to Other Agencies
    additional_notes = Column(Text, nullable=True)
    media = relationship('ReportMedia', backref='report_media_')
    address = relationship('IncidentAddress', backref='incident_address_')
    report_data_id = Column(Integer, ForeignKey('report_data.report_data_id'))

class PoliceInformation(Base):
    __tablename__ = 'police_information'
    police_information_id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_police = Column(String(25), nullable=False)
    obtain_police_info = Column(String(3), nullable=False)
    body_camera = Column(String(10), nullable=False) # NEW Unknown / yes / no
    # actions = relationship('PoliceActions', backref='police_actions_')
    officers = relationship('OfficerInformation', backref='officer_information_')
    report_data_id = Column(Integer, ForeignKey('report_data.report_data_id'))

class FormType(Base):
    __tablename__ = 'form_type'
    form_type_id = Column(Integer, primary_key=True, autoincrement=True)
    report_type = Column(String(9), nullable=False)
    reported_by_id = Column(Integer, ForeignKey('reported_by.reported_by_id'))

class ReportDate(Base):
    __tablename__ = 'report_date'
    report_date_id = Column(Integer, primary_key=True, autoincrement=True)
    report_date = Column(String(30), nullable=False)
    formatted_day = Column(String(30), nullable=False)
    formatted_week = Column(String(30), nullable=False)
    formatted_month = Column(String(30), nullable=False)
    formatted_year = Column(String(30), nullable=False)
    formatted_time = Column(String(30), nullable=False)
    time_stamp = Column(String(30), nullable=False)
    reported_by_id = Column(Integer, ForeignKey('reported_by.reported_by_id'))

class IncidentAddress(Base):
    __tablename__ = 'incident_address'
    incident_address_id = Column(Integer, primary_key=True, autoincrement=True)
    address_type = Column(String(20), nullable=False)  # automaticAddress or manualAddress
    street_name = Column(String(50), nullable=False)
    town_or_city = Column(String(100), nullable=False)
    country = Column(String(50), default='UK')
    coordinates = relationship('MapCoordinates', backref='map_coordinates_')
    public_relations_id = Column(Integer, ForeignKey('public_relations.public_relations_id'))
 

# class PoliceActions(Base):
#     __tablename__ = 'police_actions'
#     police_action_id = Column(Integer, primary_key=True, autoincrement=True)
#     police_interaction = Column(String(100), nullable=False)  # can be adujsted later
#     police_information_id = Column(Integer, ForeignKey('police_information.police_information_id'))
    
    
    
class OfficerInformation(Base):
    __tablename__ = 'officer_information'
    officer_information_id = Column(Integer, primary_key=True, autoincrement=True)
    # TODO: Create a limit for the characters and apply logic in the submit_report report to validate length of characters
    badge_number = Column(Text, nullable=True)
    officer_name = Column(Text, nullable=True)
    police_station = Column(Text, nullable=True)
    police_information_id = Column(Integer, ForeignKey('police_information.police_information_id'))
    

class MapCoordinates(Base):
    __tablename__ = 'map_coordinates'
    map_coordinates_id = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(String(30), nullable=False)
    lattitude = Column(String(30), nullable=False)
    incident_address_id = Column(Integer, ForeignKey('incident_address.incident_address_id'))

class ReportMedia(Base):
    __tablename__ = 'report_media'
    report_media_id = Column(Integer, primary_key=True, autoincrement=True)
    media_file_path = Column(String(150), nullable=True, unique=False)
    public_relations_id = Column(Integer, ForeignKey('public_relations.public_relations_id'))
