from stopSearch import app
from stopSearch.stopSearch_api import index_route, questions_route, submit_report
from stopSearch.stopSearch_endpoint import report_endpoint

# BE
app.route("/")(index_route)
app.route("/questions")(questions_route)
app.route("/submit_report")(submit_report)

# FE
app.route("/report")(report_endpoint)