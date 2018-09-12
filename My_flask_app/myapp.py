from flask import  Flask,render_template

app=Flask(__name__)

@app.route('/')
def my_funt():
    return 'This is Myapp'

@app.route('/search4')
def do_search(phrase,letters='aeiou'):
    return set(letters).intersection((set(phrase)))


app.run()