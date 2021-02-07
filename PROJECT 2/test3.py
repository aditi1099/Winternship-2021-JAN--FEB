from flask import Flask 
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app, prefix="api/v1")
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'aditi':
        return 'patel'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})



if __name__ == '__main__':
    app.run(debug=True) 