from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("temp.html",name='Swati',lang=False,language='Python',frame='Flask')

if __name__=='__main__':
    app.run(debug=True)