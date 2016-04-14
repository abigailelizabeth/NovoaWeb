import flask
import os
import json

app = flask.Flask(__name__)


data = json.load(open('data/data.json', 'r', encoding='UTF8'))


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/calculate')
def calculate():
    return flask.render_template('calculate.html')


@app.route('/results')
def render_data():

    return flask.render_template('result.html')


@app.route('/generate', methods=['POST'])
def generate_grid():
    size = int(flask.request.form['usersize'])
    return flask.render_template('calculate.html', size=size)


@app.route('/demo', methods=['POST'])
def get_data():
    size = int(flask.request.form['size'])
    for i in range(1, size+1):
        data.append(flask.request.form.get('select'+ str(i)))
    print(data)
    return flask.render_template('result.html', size=size, data=data)


@app.route('/examples/<string:building>/')
def student_ex(building):
    facility = data[building]
    flows = data['flows'];
    distances = data['distances'];
    print(facility)
    return flask.render_template('example-foundation.html', facility=facility, flows=flows, distances=distances)

if __name__ == '__main__':
    app.run(debug=True)
