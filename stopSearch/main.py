from stopSearch import app
from stopSearch.stopSearch_api import index_route

app.route("/")(index_route)