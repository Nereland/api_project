from src.app import app
from src.config import PORT
import src.controllers.users
import src.controllers.chat


app.run("localhost", PORT, debug=True)