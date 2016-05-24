import flask
import os
import json

app = flask.Flask(__name__)


data = json.load(open('data/data.json', 'r', encoding='UTF8'))


@app.route('/')
def index():
    return flask.render_template('index.html', objective=data['objective'])


@app.route('/examples/<string:building>/')
def student_ex(building):
    facility = data[building]
    flows = data['flows'];
    distances = data['distances'];
    print(facility)
    return flask.render_template('example-foundation.html', facility=facility, flows=flows, distances=distances)

if __name__ == '__main__':
    app.run(debug=True)
