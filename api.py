from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'title': 'do something cool',
              'created': '4/23/2019',
              'last-updated': '4/23/2019',
              'due-date': None,
              'completed': False,
              'completion-date': None
              },

    'todo2': {'title': 'learn to surf',
              'created': '4/23/2019',
              'last-updated': '4/23/2019',
              'due-date': None,
              'completed': False,
              'completion-date': None
              },

}


def abort_if_todo_doesnt_exist(todo_id):
    """throws an error if the todo specified does not exist"""
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class Todo(Resource):
    """shows a single todo item and lets you delete a todo item"""
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        if args['completed']:
            TODOS[todo_id].update({
                'completed': args['completed']
            })
        if args['due-date']:
            TODOS[todo_id].update({
                'due-date': args['due-date']
            })
        if args['title']:
            TODOS[todo_id].update({
                'title': args['title']
            })
        TODOS[todo_id].update({'last-updated': str(datetime.now())})
        return "Received PUT request for ID {}".format(todo_id), 201


class TodoList(Resource):
    """shows a list of all todos, and lets you POST to add new tasks"""
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'title': args['title'],
                          'due-date': args['due-date'],
                          'completed': args['completed'],
                          'completion-date': args['completion-date'],
                          'created': str(datetime.now()),
                          'last-updated': str(datetime.now())}
        return "Created new post with ID {}".format(todo_id), 201


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('due-date')
parser.add_argument('completion-date')
parser.add_argument('completed', type="bool", default=False)


if __name__ == '__main__':
    app.run(debug=True)