# working with api's --> json

from flask import Flask, jsonify, request

app = Flask(__name__)


# Intial Data in my todo list

items = [
    {"id":1,"name":"Item 1","description":"This is item 1"},
    {"id":2,"name":"Item 2","description":"This is item 2"},
]

@app.route('/')
def home():
    return "Welcome to the sample to do list app"


# Get: Retrieve all the items 

@app.route('/items',methods=['GET'])

def get_items():
    return jsonify(items)

# Get : Retrieve a specific item by Id
@app.route('/items/<int:item_id>',method=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error: Item is not found"})
    

#Post : Create a new task

@app.route('/items'.methods['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "description":request.json["descriptio"]
    }
    items.append(new_item)
    return jsonify(new_item)


# PUT: for updating a task 
@app.route('/items/<int:item_id>',methods=['PUT'])
def update(item_id):
    






if __name__=="__main__":
    app.run(debug=True)

