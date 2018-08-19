from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)

    data = {'name': 'Surajit', 'greet': 'Guten Tag'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b"Surajit", rv.data)
    assert_in(b"Guten Tag", rv.data)
