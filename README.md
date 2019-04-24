# flask_restful_api

Usage
```
python api.py
```

GET the list of todos
```
curl http://localhost:5000/todos
```

GET a single task
```
curl http://localhost:5000/todos/todo2
```

DELETE a task
```
curl http://localhost:5000/todos/todo2 -X DELETE -v
```

Add a new task
```
curl http://localhost:5000/todos -d "title=new task" -X POST -v
```

Update a task
```
curl http://localhost:5000/todos/todo2 -d "completed=True" -X PUT -v
```
