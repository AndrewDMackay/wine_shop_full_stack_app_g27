
from flask import Flask, render_template

from controllers.wines_controller import wines_blueprint
from controllers.producers_controller import producers_blueprint

app = Flask(__name__)

app.register_blueprint(wines_blueprint)
app.register_blueprint(producers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

