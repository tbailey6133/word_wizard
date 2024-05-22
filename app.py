from flask import Flask

from routes.home import home_view
from routes.wordcounter import wordcounter_view

app = Flask(__name__)
app.static_folder = "static"

app.register_blueprint(home_view)
app.register_blueprint(wordcounter_view)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
