from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

if __name__ == '__main__':
  url = "http://127.0.0.1:5000"
  webbrowser.open(url, new=0, autoraise=True)
  app.run()

