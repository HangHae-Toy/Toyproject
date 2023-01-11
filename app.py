from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:starta@cluster0.ygtjgst.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.animals

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('index2.html')

@app.route("/animal", methods=["POST"])
def animal_post():
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    gender_receive = request.form['gender_give']

    doc = {
        'name': name_receive,
        'age': age_receive,
        'gender': gender_receive,
    }
    db.animal.insert_one(doc)

    return jsonify({'msg':'입양신청 완료!'})

@app.route("/animal", methods=["GET"])
def animal_get():
    animals_list = list(db.animal.find({},{'_id':False}))
    return jsonify({'animal':animals_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)