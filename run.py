from shop import app

app.config.from_object('config')
app.config.from_pyfile('config.py')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])