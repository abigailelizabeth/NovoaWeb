import flask
from flask import g
app = flask.Flask(__name__)

data=[]


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/calculate')
def calculate():
    return flask.render_template('calculate.html')


@app.route('/calculate', methods=['POST'])
def render_data():

    return flask.render_template('result.html')


@app.route('/generate', methods=['POST'])
def generate_grid():
    size = int(flask.request.form['usersize'])
    return flask.render_template('calculate.html', size=size)


@app.route('/demo', methods=['POST'])
def get_data():
    for i in range(1, int(flask.request.form['size'])+1):
        print('what about here')
        data.append(flask.request.form.get('select'+ str(i)))
    print(data)
    return flask.redirect('/', code=301)


if __name__ == '__main__':
    app.run(debug=True)
