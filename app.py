from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
# client = MongoClient('mongodb+srv://test:sparta@cluster0.ygtjgst.mongodb.net/Cluster0?retryWrites=true&w=majority')
# db = client.adopts

client = MongoClient('mongodb+srv://homesite:oBJqg6n3yp0IItHS@cluster0.gnq7ra8.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.miniproject

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/saveAdopt", methods=["POST"])
def animal_post():
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    address_receive = request.form['address_give']
    reason_receive = request.form['reason_give']
    id_receive = request.form['id_give']

    doc = {
        'name': name_receive,
        'age': age_receive,
        'address': address_receive,
        'reason': reason_receive,
        'id': id_receive,
    }
    # db.animal.insert_one(doc)
    db.miniproject.insert_one(doc)
    return jsonify({'msg':'입양신청 완료!'})


@app.route("/saveAdopt", methods=["GET"])
def animal_get():
    animals_list = list(db.animal.find({},{'_id':False}))
    return jsonify({'animal':animals_list})


@app.route("/saveAdoptView", methods=["POST"])
def saveAdoptView_post():
    index_receive = request.form['index_give']
    all_comments = list(db.miniproject.find({'id': index_receive}, {'_id': False}))
    print(index_receive)
    return jsonify({'msg': all_comments})


@app.route("/saveAdoptView")
def saveAdoptView_page():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)