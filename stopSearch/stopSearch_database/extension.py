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
            QuestionReportQuestions(report_question='Please enter your email to start the report:'),
            QuestionReportQuestions(report_question='Please re-enter your email to complete the report:'),
            QuestionReportQuestions(report_question='Are you a witness or a victim?'),
            QuestionReportQuestions(report_question='Enter the date of the incident:'),
            QuestionReportQuestions(report_question='Where did this incident happen?'),
            QuestionReportQuestions(report_question='How many victim were involved in the incident?'),
            QuestionReportQuestions(report_question='Approximately how many police could you see?'),
            QuestionReportQuestions(report_question='What was the reason for the stop?'),
            QuestionReportQuestions(report_question='Was the search moderate or aggressive?'),
            QuestionReportQuestions(report_question='Did you get the police officer\'s name, badge number etc?'),
            QuestionReportQuestions(report_question='Enter the police officer\'s information where possible:'),
            QuestionReportQuestions(report_question='How old was the person or people involved?'),
            QuestionReportQuestions(report_question='What was the gender of the person or people involved?'),
            QuestionReportQuestions(report_question='What is the race of the person or people involved?'),
            QuestionReportQuestions(report_question='Please add any additional notes here:'),
            QuestionReportQuestions(report_question='Please upload any media you have here:'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionReportType).first():
        default_data = [
            QuestionReportType(report_type='witness'),
            QuestionReportType(report_type='victim'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionLocationType).first():
        default_data = [
            QuestionLocationType(location_type='Automatic Address'),
            QuestionLocationType(location_type='Manual Address'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionVictimsInvolved).first():
        default_data = [
            QuestionVictimsInvolved(victims_involved='Unknown'),
            QuestionVictimsInvolved(victims_involved='1'),
            QuestionVictimsInvolved(victims_involved='2'),
            QuestionVictimsInvolved(victims_involved='3'),
            QuestionVictimsInvolved(victims_involved='4'),
            QuestionVictimsInvolved(victims_involved='5'),
            QuestionVictimsInvolved(victims_involved='6'),
            QuestionVictimsInvolved(victims_involved='7'),
            QuestionVictimsInvolved(victims_involved='8'),
            QuestionVictimsInvolved(victims_involved='9'),
            QuestionVictimsInvolved(victims_involved='10'),
            QuestionVictimsInvolved(victims_involved='10+'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionNumberOfPolice).first():
        default_data = [
            QuestionNumberOfPolice(number_of_police='Unknown'),
            QuestionNumberOfPolice(number_of_police='1 - 2'),
            QuestionNumberOfPolice(number_of_police='3 - 4'),
            QuestionNumberOfPolice(number_of_police='5 - 6'),
            QuestionNumberOfPolice(number_of_police='6+'),
            QuestionNumberOfPolice(number_of_police='10+'),
            QuestionNumberOfPolice(number_of_police='15+'),
            QuestionNumberOfPolice(number_of_police='20+'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionSearchReason).first():
        default_data = [
            QuestionSearchReason(search_reason='Unknown'),
            QuestionSearchReason(search_reason='A police officer has the power to search someone if they have reasonable grounds of:'),
            QuestionSearchReason(search_reason='Suspicion of drugs'),
            QuestionSearchReason(search_reason='Carrying a weapon'),
            QuestionSearchReason(search_reason='Stolen goods'),
            QuestionSearchReason(search_reason='Suspicion of comitting a crime'),
            QuestionSearchReason(search_reason='A police officer has th epower to search without reasonable grounds if:'),
            QuestionSearchReason(search_reason='Suspicion of comitting a serious or violent crime'),
            QuestionSearchReason(search_reason='History of carrying or using a weapon in the past'),
            QuestionSearchReason(search_reason='In a location where crime is high'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionSearchType).first():
        default_data = [
            QuestionSearchType(search_type='Unknown'),
            QuestionSearchType(search_type='Moderate'),
            QuestionSearchType(search_type='Aggressive'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionVictimAge).first():
        default_data = [
            QuestionVictimAge(victim_age='Unknown'),
            QuestionVictimAge(victim_age='15 - 17'),
            QuestionVictimAge(victim_age='18 - 24'),
            QuestionVictimAge(victim_age='25 - 30'),
            QuestionVictimAge(victim_age='31 - 35'),
            QuestionVictimAge(victim_age='35+'),
            QuestionVictimAge(victim_age='40+'),
            QuestionVictimAge(victim_age='45+'),
            QuestionVictimAge(victim_age='50+'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionVictimGender).first():
        default_data = [
            QuestionVictimGender(victim_gender='Unknown'),
            QuestionVictimGender(victim_gender='Man'),
            QuestionVictimGender(victim_gender='Woman'),
            QuestionVictimGender(victim_gender='Non-Binary'),
            QuestionVictimGender(victim_gender='Trans'),
            QuestionVictimGender(victim_gender='Group of mixed genders'),
            QuestionVictimGender(victim_gender='Group of men'),
            QuestionVictimGender(victim_gender='Group of women'),
            QuestionVictimGender(victim_gender='Group from LGBT community'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    if not session.query(QuestionVictimRace).first():
        default_data = [
            QuestionVictimRace(victim_race='Unknown'),
            QuestionVictimRace(victim_race='Arab'),
            QuestionVictimRace(victim_race='Asian'),
            QuestionVictimRace(victim_race='Black'),
            QuestionVictimRace(victim_race='Mixed Race'),
            QuestionVictimRace(victim_race='Group of different races'),
            QuestionVictimRace(victim_race='Group of Arab people'),
            QuestionVictimRace(victim_race='Group of Asian people'),
            QuestionVictimRace(victim_race='Group of Black people'),
            QuestionVictimRace(victim_race='Group of White people'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()