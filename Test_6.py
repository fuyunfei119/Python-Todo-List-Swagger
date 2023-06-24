from flask import Flask, request, jsonify
import json
app = Flask(__name__)


TodoLists = []
TodoLists.append(
    {'id': '1a5eebec-410d-4904-8599-71244fbb25cb',
     'name': 'Milch einkaufen',
     'description': '',
     'list_id': 'c819997b-9b75-44a6-95e1-79da9ed36170'
     }
)
TodoLists.append(
    {'id': 'cab25b4e-0b60-4df4-9da3-82ecc2315241',
     'name': 'Kaffee einkaufen',
     'description': '',
     'list_id': 'd161cf01-a756-4e44-b3a9-3a6773d35826'
     }
)


# add some headers to allow cross origin access to the API on this server, necessary for using preview in Swagger Editor!


@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PATCH'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/todo-list/<string:list_id>', methods=['GET', 'DELETE', 'PATCH'])
def todo_list(list_id):
    if request.method == 'GET':
        # Get all entries of a Todo List
        # ...
        result = []

        for todolist in TodoLists:
            if todolist['id'] == list_id:
                result.append(todolist)
        return jsonify(result)

    elif request.method == 'DELETE':
        # Delete a complete Todo List with all entries
        # ...

        for todolist in TodoLists:
            if todolist['id'] == list_id:
                return jsonify({'message': 'List was deleted'})

    elif request.method == 'PATCH':
        # Update the name of an existing Todo List
        # ...
        for todolist in TodoLists:
            if todolist['id'] == list_id:
                return jsonify({'message': 'List was updated'})


@app.route('/todo-list', methods=['GET', 'POST'])
def todo_lists():
    if request.method == 'GET':
        # Get a list of all Todo Lists
        # ...
        new_entry = {'id': '1a5eebec-410d-4904-8599-71244fbb25cb',
                     'name': 'Milch einkaufen',
                     'description': '',
                     'list_id': 'c819997b-9b75-44a6-95e1-79da9ed36170'
                     }

        TodoLists.append(new_entry)
        return jsonify(TodoLists)

    elif request.method == 'POST':
        # Add a new Todo List
        # ...
        print(request.json)
        TodoLists.append(request.json)
        return jsonify(TodoLists)


@app.route('/todo-list/<string:list_id>/entry', methods=['POST'])
def todo_list_entry(list_id):
    # Add an entry to an existing Todo List
    # ...

    return jsonify({'message': 'Entry was added'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
