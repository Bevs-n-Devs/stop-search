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

    # Create default questions if it doesn't exist
    
    from stopSearch.stopSearch_database.models import (
        QuestionReportQuestions,
        QuestionReportType,
        QuestionLocationType,
        QuestionVictimsInvolved,
        QuestionNumberOfPolice,
        QuestionSearchReason,
        QuestionSearchType,
        QuestionVictimAge,
        QuestionVictimGender,
        QuestionVictimRace
    )

    session = db_session()

    if not session.query(QuestionReportQuestions).first():
        default_data = [
            QuestionReportQuestions(question_name='Please enter your email to start the report:'),
            QuestionReportQuestions(question_name='Please re-enter your email to complete the report:'),
            QuestionReportQuestions(question_name='Are you a witness or a victim?'),
            QuestionReportQuestions(question_name='Enter the date of the incident:'),
            QuestionReportQuestions(question_name='Where did this incident happen?'),
            QuestionReportQuestions(question_name='How many victim were involved in the incident?'),
            QuestionReportQuestions(question_name='Approximately how many police could you see?'),
            QuestionReportQuestions(question_name='What was the reason for the stop?'),
            QuestionReportQuestions(question_name='Was the search moderate or aggressive?'),
            QuestionReportQuestions(question_name='Did you get the police officer\'s name, badge number etc?'),
            QuestionReportQuestions(question_name='Enter the police officer\'s information where possible:'),
            QuestionReportQuestions(question_name='How old was the person or people involved?'),
            QuestionReportQuestions(question_name='What was the gender of the person or people involved?'),
            QuestionReportQuestions(question_name='What is the race of the person or people involved?'),
            QuestionReportQuestions(question_name='Please add any additional notes here:'),
            QuestionReportQuestions(question_name='Please upload any media you have here:'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionReportType).first():
        default_data = [
            QuestionReportType(report_type_options='witness'),
            QuestionReportType(report_type_options='victim'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionLocationType).first():
        default_data = [
            QuestionLocationType(location_type_options='Automatic Address'),
            QuestionLocationType(location_type_options='Manual Address'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionVictimsInvolved).first():
        default_data = [
            QuestionVictimsInvolved(victims_involved_options='Unknown'),
            QuestionVictimsInvolved(victims_involved_options='1'),
            QuestionVictimsInvolved(victims_involved_options='2'),
            QuestionVictimsInvolved(victims_involved_options='3'),
            QuestionVictimsInvolved(victims_involved_options='4'),
            QuestionVictimsInvolved(victims_involved_options='5'),
            QuestionVictimsInvolved(victims_involved_options='6'),
            QuestionVictimsInvolved(victims_involved_options='7'),
            QuestionVictimsInvolved(victims_involved_options='8'),
            QuestionVictimsInvolved(victims_involved_options='9'),
            QuestionVictimsInvolved(victims_involved_options='10'),
            QuestionVictimsInvolved(victims_involved_options='10+'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionNumberOfPolice).first():
        default_data = [
            QuestionNumberOfPolice(number_of_police_options='Unknown'),
            QuestionNumberOfPolice(number_of_police_options='1 - 2'),
            QuestionNumberOfPolice(number_of_police_options='3 - 4'),
            QuestionNumberOfPolice(number_of_police_options='5 - 6'),
            QuestionNumberOfPolice(number_of_police_options='6+'),
            QuestionNumberOfPolice(number_of_police_options='10+'),
            QuestionNumberOfPolice(number_of_police_options='15+'),
            QuestionNumberOfPolice(number_of_police_options='20+'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionSearchReason).first():
        default_data = [
            QuestionSearchReason(search_reason_options='Unknown'),
            QuestionSearchReason(search_reason_options='A police officer has the power to search someone if they have reasonable grounds of:'),
            QuestionSearchReason(search_reason_options='Suspicion of drugs'),
            QuestionSearchReason(search_reason_options='Carrying a weapon'),
            QuestionSearchReason(search_reason_options='Stolen goods'),
            QuestionSearchReason(search_reason_options='Suspicion of comitting a crime'),
            QuestionSearchReason(search_reason_options='A police officer has th epower to search without reasonable grounds if:'),
            QuestionSearchReason(search_reason_options='Suspicion of comitting a serious or violent crime'),
            QuestionSearchReason(search_reason_options='History of carrying or using a weapon in the past'),
            QuestionSearchReason(search_reason_options='In a location where crime is high'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionSearchType).first():
        default_data = [
            QuestionSearchType(search_type_options='Unknown'),
            QuestionSearchType(search_type_options='Moderate'),
            QuestionSearchType(search_type_options='Aggressive'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionVictimAge).first():
        default_data = [
            QuestionVictimAge(victim_age_options='Unknown'),
            QuestionVictimAge(victim_age_options='15 - 17'),
            QuestionVictimAge(victim_age_options='18 - 24'),
            QuestionVictimAge(victim_age_options='25 - 30'),
            QuestionVictimAge(victim_age_options='31 - 35'),
            QuestionVictimAge(victim_age_options='35+'),
            QuestionVictimAge(victim_age_options='40+'),
            QuestionVictimAge(victim_age_options='45+'),
            QuestionVictimAge(victim_age_options='50+'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionVictimGender).first():
        default_data = [
            QuestionVictimGender(victim_gender_options='Unknown'),
            QuestionVictimGender(victim_gender_options='Man'),
            QuestionVictimGender(victim_gender_options='Woman'),
            QuestionVictimGender(victim_gender_options='Non-Binary'),
            QuestionVictimGender(victim_gender_options='Trans'),
            QuestionVictimGender(victim_gender_options='Group of mixed genders'),
            QuestionVictimGender(victim_gender_options='Group of men'),
            QuestionVictimGender(victim_gender_options='Group of women'),
            QuestionVictimGender(victim_gender_options='Group from LGBT community'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionVictimRace).first():
        default_data = [
            QuestionVictimRace(victim_race_options='Unknown'),
            QuestionVictimRace(victim_race_options='Arab'),
            QuestionVictimRace(victim_race_options='Asian'),
            QuestionVictimRace(victim_race_options='Black'),
            QuestionVictimRace(victim_race_options='Mixed Race'),
            QuestionVictimRace(victim_race_options='Group of different races'),
            QuestionVictimRace(victim_race_options='Group of Arab people'),
            QuestionVictimRace(victim_race_options='Group of Asian people'),
            QuestionVictimRace(victim_race_options='Group of Black people'),
            QuestionVictimRace(victim_race_options='Group of White people'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()