from application import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

gunicorn app:app
gunicorn --workers 4 app:app
gunicorn --bind=0.0.0.0:666 app:app