from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def get_name():
    return jsonify({'name': 'Georgiy Debrin'})

@app.route('/profession', methods=['GET'])
def get_profession():
    return jsonify({'Profession': 'QA Engineer', 'Experience': '2022 - present'})

@app.route('/social', methods=['GET'])
def get_social():
    return jsonify({'Telegram': 'gr_debrin', 'LinkedIn': 'georgiy-debrin', 'GitHub': 'grdebrin'})

@app.route('/salary', methods=['POST'])
def post_salary():
    name = request.form.get('name')
    salary = request.form.get('salary')
    return jsonify({'Name': name, 'Expected_salary': salary})

@app.route('/hobby', methods=['POST'])
def post_hobby():
    name = request.form.get('name')
    return jsonify({'Name': name, 'Hobby_1': 'Music', 'Hobby_2': 'Reading', 'Hobby_3': 'Investing'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
