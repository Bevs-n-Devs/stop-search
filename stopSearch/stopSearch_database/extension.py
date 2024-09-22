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

    # TODO:   3. Write comments, what is going on? How do we populate the questions?
    
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
        QuestionVictimRace,
        QuestionBodyCamera,
        QuestionOfficerInteraction,
        QuestionSearchOutcome
    )

    session = db_session()

    # create the questions that will be asked in the report
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
            QuestionReportQuestions(question_name='Was the police officer wearing a body camera?'),
            QuestionReportQuestions(question_name='Do you know whart the outcome of the search was?'),
            QuestionReportQuestions(question_name='How did the officer engage with the victim or witness during the interaction?')
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
    
    # create the options for the user to select from the report.
    # The options are linked to the question index in QuestionReportQuestions

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
            QuestionVictimsInvolved(victims_involved_options='10 or more'),
            QuestionVictimsInvolved(victims_involved_options='15 or more'),
            QuestionVictimsInvolved(victims_involved_options='Over 20'),
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
            QuestionNumberOfPolice(number_of_police_options='7+'),
            QuestionNumberOfPolice(number_of_police_options='10 or more'),
            QuestionNumberOfPolice(number_of_police_options='15 or more'),
            QuestionNumberOfPolice(number_of_police_options='Over 20'),
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
            QuestionVictimAge(victim_age_options='14 or under'),
            QuestionVictimAge(victim_age_options='15 - 17'),
            QuestionVictimAge(victim_age_options='18 - 24'),
            QuestionVictimAge(victim_age_options='25 - 30'),
            QuestionVictimAge(victim_age_options='31 - 34'),
            QuestionVictimAge(victim_age_options='35+'),
            QuestionVictimAge(victim_age_options='40+'),
            QuestionVictimAge(victim_age_options='45+'),
            QuestionVictimAge(victim_age_options='50+'),
            QuestionVictimAge(victim_age_options='In their 60\'s'),
            QuestionVictimAge(victim_age_options='In their 70\'s'),
            QuestionVictimAge(victim_age_options='Over 80'),
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
            QuestionVictimRace(victim_race_options='Asian, Asian British or Asian Welsh:'),
            QuestionVictimRace(victim_race_options='Bangladeshi'),
            QuestionVictimRace(victim_race_options='Chinese'),
            QuestionVictimRace(victim_race_options='Indian'),
            QuestionVictimRace(victim_race_options='Pakistani'),
            QuestionVictimRace(victim_race_options='Other Asian'),
            QuestionVictimRace(victim_race_options='Black, Black British, Black Welsh, Caribbean or African:'),
            QuestionVictimRace(victim_race_options='African'),
            QuestionVictimRace(victim_race_options='Caribbean'),
            QuestionVictimRace(victim_race_options='Other Black'),
            QuestionVictimRace(victim_race_options='Mixed or Multiple ethnic groups:'),
            QuestionVictimRace(victim_race_options='White and Asian'),
            QuestionVictimRace(victim_race_options='White and Black African'),
            QuestionVictimRace(victim_race_options='White and Black Caribbean'),
            QuestionVictimRace(victim_race_options='Other Mixed or Multiple ethnic groups'),
            QuestionVictimRace(victim_race_options='White:'),
            QuestionVictimRace(victim_race_options='English, Welsh, Scottish, Northern Irish or British'),
            QuestionVictimRace(victim_race_options='Irish'),
            QuestionVictimRace(victim_race_options='Gypsy or Irish Traveller'),# 21
            QuestionVictimRace(victim_race_options='Roma'),
            QuestionVictimRace(victim_race_options='Other White'),
            QuestionVictimRace(victim_race_options='Other ethnic group:'), # 24
            QuestionVictimRace(victim_race_options='Arab'),
            QuestionVictimRace(victim_race_options='Any other ethnic group'),
            QuestionVictimRace(victim_race_options='Groups of people:'), # 27
            QuestionVictimRace(victim_race_options='Multiple racial groups'),
            QuestionVictimRace(victim_race_options='Group of Arab people'),
            QuestionVictimRace(victim_race_options='Group of Asian people'), # 30
            QuestionVictimRace(victim_race_options='Group of Black people'),
            QuestionVictimRace(victim_race_options='Group of Mixed Race people'),
            QuestionVictimRace(victim_race_options='Group of White people'), # 33
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionBodyCamera).first():
        default_data = [
            QuestionBodyCamera(body_camera_options='Unknown'),
            QuestionBodyCamera(body_camera_options='yes'),
            QuestionBodyCamera(body_camera_options='no')
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionSearchOutcome).first():
        default_data = [
            QuestionSearchOutcome(search_outcome_options='Unknown'),
            QuestionSearchOutcome(search_outcome_options='No Further Action (NFA)'),
            QuestionSearchOutcome(search_outcome_options='Item Seized'),
            QuestionSearchOutcome(search_outcome_options='Arrest'),
            QuestionSearchOutcome(search_outcome_options='Warning or Caution Issued'),
            QuestionSearchOutcome(search_outcome_options='Fixed Penalty Notice'),
            QuestionSearchOutcome(search_outcome_options='Summons to Court'),
            QuestionSearchOutcome(search_outcome_options='Community Resolution'),
            QuestionSearchOutcome(search_outcome_options='Referral to Other Agencies'),
        ]
        session.add_all(default_data)
        session.commit()
        session.close()

    if not session.query(QuestionOfficerInteraction).first():
        default_data = [
            QuestionOfficerInteraction(officer_interaction_options='Asked About Recent Activities'),
            QuestionOfficerInteraction(officer_interaction_options='Asked for Consent to Search'),
            QuestionOfficerInteraction(officer_interaction_options='Asked for Explanation of Presence'),
            QuestionOfficerInteraction(officer_interaction_options='Asked to Empty Pockets'),
            QuestionOfficerInteraction(officer_interaction_options='Asked to Open Bag'),
            QuestionOfficerInteraction(officer_interaction_options='Asked to Provide Contact Information'),
            QuestionOfficerInteraction(officer_interaction_options='Asked to Remove Outer Clothing'),
            QuestionOfficerInteraction(officer_interaction_options='Asked to Show ID'),
            QuestionOfficerInteraction(officer_interaction_options='Asked to Provide DNA Sample'),
            QuestionOfficerInteraction(officer_interaction_options='Detained for Further Investigation'),
            QuestionOfficerInteraction(officer_interaction_options='Escorted to a Police Vehicle'),
            QuestionOfficerInteraction(officer_interaction_options='Given a Fixed Penalty Notice'),
            QuestionOfficerInteraction(officer_interaction_options='Given a Stop and Search Reference Number'),
            QuestionOfficerInteraction(officer_interaction_options='Given a Verbal Caution'),
            QuestionOfficerInteraction(officer_interaction_options='Handcuffed'),
            QuestionOfficerInteraction(officer_interaction_options='Informed of Arrest'),
            QuestionOfficerInteraction(officer_interaction_options='Informed of Body Cam Recording'),
            QuestionOfficerInteraction(officer_interaction_options='Informed of Rights'),
            QuestionOfficerInteraction(officer_interaction_options='Informed of Rights to File a Complaint'),
            QuestionOfficerInteraction(officer_interaction_options='Informed of Search Grounds'),
            QuestionOfficerInteraction(officer_interaction_options='Issued a Stop and Search Receipt'),
            QuestionOfficerInteraction(officer_interaction_options='Issued Warning'),
            QuestionOfficerInteraction(officer_interaction_options='Offered a Community Resolution'),
            QuestionOfficerInteraction(officer_interaction_options='Provided First Aid'),
            QuestionOfficerInteraction(officer_interaction_options='Provided with Legal Advice'),
            QuestionOfficerInteraction(officer_interaction_options='Questioned About Possessions'),
            QuestionOfficerInteraction(officer_interaction_options='Requested to Provide Witness Information'),
            QuestionOfficerInteraction(officer_interaction_options='Requested to Sign a Statement'),
            QuestionOfficerInteraction(officer_interaction_options='Request for Assistance by Another Officer'),
            QuestionOfficerInteraction(officer_interaction_options='Searched for Drugs'),
            QuestionOfficerInteraction(officer_interaction_options='Searched for Stolen Property'),
            QuestionOfficerInteraction(officer_interaction_options='Searched for Weapons'),
            QuestionOfficerInteraction(officer_interaction_options='Searched Using Force'),
            QuestionOfficerInteraction(officer_interaction_options='Searched Without Force'),
            QuestionOfficerInteraction(officer_interaction_options='Taken to Police Station'),
            QuestionOfficerInteraction(officer_interaction_options='Told to Attend Police Station'),
            QuestionOfficerInteraction(officer_interaction_options='Told to Leave the Area'),
            QuestionOfficerInteraction(officer_interaction_options='Told to Wait for Further Instructions')
        ]
        session.add_all(default_data)
        session.commit()
        session.close()
