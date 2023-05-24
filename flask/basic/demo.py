from flask import Flask,request,redirect,url_for,render_template,session,flash
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "badru"
# app.permanent_session_lifetime=timedelta(days=5)
app.permanent_session_lifetime=timedelta(minutes=1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product/<int:id>')
def product(id):
    return "product id %s" % id

@app.route('/guest/<name>')
def guest(name):
    return "Guest  is %s" % name

@app.route('/search',methods=['GET'])
def search():
    args = request.args
    name = args.get('name')
    #location = args.get('location')
    return name

# @app.route('/user/<name>')
# def login(name):
#      if name=='admin':
#           return redirect(url_for('home'))
#      else:
#           return redirect(url_for('guest',name='arman'))
     
     

@app.route('/login',methods=["POST","GET"])
def login():
     if request.method == "POST":
        session.permanent = True
        user = request.form['username']
        session["user"] = user
        #return redirect(url_for("user",user=user))
        return redirect(url_for("user"))
     else:
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template('login.html')   
             

# @app.route('/<user>')
# def user(user):
#      return f"<h1>{user}<h2>"
@app.route('/user')
def user():
    if "user" in session:
        user = session['user']
        return f"<h1>{user}<h2>"
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    if "user" in session:
        user = session['user']
        flash(f"{user} logout","info")
    session.pop("user",None)
   
    return  redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)

