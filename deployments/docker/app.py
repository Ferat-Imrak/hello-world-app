from flask import Flask,  jsonify 
import os 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return jsonify({
        'message': 'hello I am a developer my name is Ferhat',
        'environment': os.environ.get('ENVIRONMENT'),
        'ownner': 'jiro1',
        'namespace': os.environ.get('NAMESPACE')
    })
@app.route('/jiro1')
def comming_soon():
    return jsonify({
        'message': 'This is my page!!'
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)