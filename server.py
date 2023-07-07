from flask import Flask, render_template, request, redirect, session

app = Flask(__name__) 
app.secret_key = "Vollstin"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def gatherInfo():
    session['firstname'] = request.form['first_name']
    session['lastname'] = request.form['last_name']
    session['dojolocation'] = request.form['location']
    session['language'] = request.form['favorite_language']
    session['yourcomment'] = request.form['comment']
    return redirect('/show')

@app.route('/show')
def showInfo():
    return render_template('info.html')




if __name__=="__main__":    
    app.run(debug=True)  