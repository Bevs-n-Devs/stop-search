from stopSearch import app
from stopSearch.stopSearch_api import index_route, questions_route, submit_report, search_engine
from stopSearch.stopSearch_endpoint import report_endpoint, map_endpoint

# BE
app.route("/")(index_route)
app.route("/questions")(questions_route)
app.route("/submit_report")(submit_report)
app.route("/search")(search_engine)

# FE
app.route("/report")(report_endpoint)
app.route("/map")(map_endpoint)