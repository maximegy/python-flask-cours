from flask import Flask

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Biatch !"

if __name__ == "__main__":
    app.run()