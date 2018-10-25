# encoding:utf-8
import sys
from flask import Flask,render_template,request
from flask_socketio import SocketIO
import flask_restful
from transform import willingnessCalculation,capacityCalculation

app = Flask(__name__)
api = flask_restful.Api(app)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform',methods=['POST','GET'])
def transform():
    q2a = request.args.get('q2a')
    q3a = request.args.get('q3a')
    q4a = request.args.get('q4a')
    q6a = request.args.get('q6a')
    q7a = request.args.get('q7a')
    q8a = request.args.get('q8a')
    willingness = willingnessCalculation(q2a,q3a,q8a)
    capacity = capacityCalculation(q4a,q6a,q7a)
    print capacity
    return render_template('index.html',willingness=willingness,capacity=capacity)

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    socketio.run(app,debug=True,port=5001)