from api import app


app.config['Testing'] = True

def test_get_success():
    result = app.test_client().get('/todos')
    assert result.status_code == 200

def test_get_fail():
    result = app.test_client().get('/todos')
    assert result.status_code == 405

def test_post_success():
    result = app.test_client().post('/todos')
    assert result.status_code == 201

def test_post_fail():
    result = app.test_client().post('/todos')
    assert result.status_code == 405

def test_put_success():
    result = app.test_client().put('/todos/todo1')
    assert result.status_code == 201

def test_put_fail():
    result = app.test_client().put('/todos/todo1')
    assert result.status_code == 405

def test_delete_success():
    result = app.test_client().delete('/todos/todo2')
    assert result.status_code == 204

def test_delete_fail():
    result = app.test_client().delete('/todos/todo2')
    assert result.status_code == 204