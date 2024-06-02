from stopSearch import app
from stopSearch.stopSearch_api import index_route, questions_route

app.route("/")(index_route)
app.route("/questions")(questions_route)
