from sqlalchemy import *
from stopSearch import app
from stopSearch.stopSearch_database.extension import LocalSession, init_db
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

def get_all_report_questions() -> list[QuestionReportQuestions]:
    """
    Returns list of QuestionReportQuestions objects.

    SELECT * 
    FROM stop_search_dev_db.question_report_questions;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionReportQuestions.question_id,
            QuestionReportQuestions.question_name
        )

        try:
            report_questions = session.execute(sql_query).all()
            return report_questions
        except Exception as e:
            return {"SQL Error": e}

def get_report_type_options() -> list[QuestionReportType]:
    """
    Returns all report type options.

    SELECT *
    FROM stop_search_dev_db.question_report_type;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionReportType.question_report_type_id,
            QuestionReportType.report_type_options,
        )

        try:
            report_type_options = session.execute(sql_query).all()
            return report_type_options
        except Exception as e:
            return {"SQL Error": e}

def get_location_type_options() -> list[QuestionLocationType]:
    """
    Returns list of location type options.

    SELECT *
    FROM stop_search_dev_db.question_location_type;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionLocationType.question_location_type_id,
            QuestionLocationType.location_type_options
        )

        try:
            location_type_options = session.execute(sql_query).all()
            return location_type_options
        except Exception as e:
            return {"SQL Error": e}
        
def get_victims_involved_options() -> list[QuestionVictimsInvolved]:
    """
    Returns list of victim options.

    SELECT *
    FROM stop_search_dev_db.question_victims_involved;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionVictimsInvolved.question_victims_involved_id,
            QuestionVictimsInvolved.victims_involved_options,
        )

        try:
            victim_involved_options = session.execute(sql_query).all()
            return victim_involved_options
        except Exception as e:
            return {"SQL Error": e}
        
def get_number_of_police_options() -> list[QuestionNumberOfPolice]:
    """
    Returns a list of police quantity options.

    SELECT *
    FROM stop_search_dev_db.question_number_of_police
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionNumberOfPolice.question_number_of_police_id,
            QuestionNumberOfPolice.number_of_police_options,
        )

        try:
            number_of_police_options = session.execute(sql_query).all()
            return number_of_police_options
        except Exception as e:
            return {"SQL Error": e}

def get_search_reason_options() -> list[QuestionSearchReason]:
    """
    Returns a list of search reasons.

    SELECT * 
    FROM stop_search_dev_db.question_search_reason;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionSearchReason.question_search_reason_id,
            QuestionSearchReason.search_reason_options,
        )

        try:
            search_reason_options = session.execute(sql_query).all()
            return search_reason_options
        except Exception as e:
            return {"SQL Error": e}
        
def get_search_type_options() -> list[QuestionSearchType]:
    """
    Returns a list of search types.

    SELECT *
    FROM stop_search_dev_db.question_search_type;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionSearchType.question_search_type_id,
            QuestionSearchType.search_type_options,
        )

        try:
            search_type_options_ = session.execute(sql_query).all()
            return search_type_options_
        except Exception as e:
            return {"SQL Error": e}

def get_victim_age_options() -> list[QuestionVictimAge]:
    """
    Returns a list of ages.

    SELECT *
    FROM stop_search_dev_db.question_victim_age;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionVictimAge.question_victim_age_id,
            QuestionVictimAge.victim_age_options,
        )

        try:
            victim_options = session.execute(sql_query).all()
            return victim_options
        except Exception as e:
            return {"SQL Error": e}
        
def get_victim_race_options() -> list[QuestionVictimRace]:
    """
    Returns a list of races.

    SELECT *
    FROM stop_search_dev_db.question_victim_race;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionVictimRace.question_victim_race_id,
            QuestionVictimRace.victim_race_options
        )

        try:
            victim_race = session.execute(sql_query).all()
            return victim_race
        except Exception as e:
            return {"SQL Error": e}
        
def get_victim_gender_options() -> list[QuestionVictimGender]:
    """
    Returns a list of genders.

    SELECT *
    FROM stop_search_dev_db.question_victim_gender;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            QuestionVictimGender.question_victim_gender_id,
            QuestionVictimGender.victim_gender_options
        )

        try:
            victim_gender = session.execute(sql_query).all()
            return victim_gender
        except Exception as e:
            return {"SQL Error": e}
        
