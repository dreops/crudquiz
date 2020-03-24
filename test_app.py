from app import __name__

def test_name():
    assert __name__== '__main__'

def test_run():
    assert run == app.run(debug=True, host='0.0.0.0')