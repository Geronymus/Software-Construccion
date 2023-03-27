from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_users():   

    print('select * users')

    result = {'result': True, 'data':'userss ....' }
    return jsonify(result)


@app.route('/user', methods=['POST'])
def user():   
    name = request.json['name']
    lastname = request.json['lastname']
    age = request.json['age']
    height = request.json['height']
    weight = request.json['weight']

    print('inserting new user', name, lastname, age, height, weight)

    result = {'result': True, 'message':'OK' }
    return jsonify(result)


@app.route('/user', methods=['DELETE'])
def del_user():   
    user_id = request.json['id']

    print('deleting user', user_id)

    result = {'result': True, 'message':'OK' }
    return jsonify(result)


@app.route('/user', methods=['PATCH'])
def update_user():   
    user_id = request.json['id']
    name = request.json['name']
    lastname = request.json['lastname']
    age = request.json['age']
    height = request.json['height']
    weight = request.json['weight']

    print('updating user', user_id, name, lastname, age, height, weight)

    result = {'result': True, 'message':'OK' }
    return jsonify(result)



@app.route('/user/upload_photo', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']

        f.save("D:\\Upload\\" + f.filename)

    result = {'result': True, 'message':'OK' }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5002)


