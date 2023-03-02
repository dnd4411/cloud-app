
import os
import MySQLdb
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from mydb import db_connect,reg,user_login,user_upload,user_viewimages,fog_viewimages,fog_reg,fog_user_login,user_search,cl_viewimages,cl_reg,cloudlogin

from werkzeug.utils import secure_filename



 

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def FUN_root():
    return render_template("image.html")



# ==================================== sign up ==============================
@app.route("/signup", methods = ['GET','POST'])
def registeract():
    if request.method == 'POST':    
        id="0"
        status = reg(request.form['username'],request.form['password'],request.form['email'])
        if status == 1:
            return render_template("log.html",m1="sucess")
        else:
            return render_template("signup.html")   
    else:
        return render_template("signup.html")






@app.route("/login_user", methods=['GET', 'POST'])
def user_log():
    if request.method == 'POST':
        print(request.form['email'],"============")
        status = user_login(request.form['email'], request.form['password'])
        print(status,"---------")
        for a,b,c in status:
            session['username'] = a
            session['email'] = b

        if status:            
            print(session["username"],"------------session")                       
            return render_template("home.html", m1="sucess",uname=session['username'])   ###,uname=session['username']
        else:
            print('m2')
            return render_template("log.html", m2="Login Failed")

    else:
        return render_template("log.html")

@app.route('/logout')
def logout():
	session.pop('email', None)
    
	return render_template('image.html')

# =================================================================
@app.route("/upload.html",methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        id=0
        file = request.files['fname']        
        filename = request.form['recordname']        
        print( request.form['recordname'],'post')
        
        status = user_upload(file,filename)
        print(status)
        if status == 1:
            return render_template("upload.html",m1="your record is uploaded successfully")
        else:
            return render_template('upload.html',m1="Enter valid input")



    else:
        print('hii')
        return render_template('upload.html')
# =================================  view all  ============================================
@app.route("/viewall.html")
def viewimages():
    data = user_viewimages(session['username'])
    print(data)
    print
    result = []
    for i in data:
        result.append(i[1])

    
    
    # print(read)
  
    # reading the file
    
    
    return render_template("viewall.html",user = data)

# ==================================== sign up ==============================
@app.route("/fog_signup", methods = ['GET','POST'])
def fog_rege():
    if request.method == 'POST':    
        id="0"
        status = fog_reg(request.form['username'],request.form['password'],request.form['email'])
        if status == 1:
            return render_template("fog_login.html",m1="sucess")
        else:
            return render_template("fog_signup.html")   
    else:
        return render_template("fog_signup.html")






@app.route("/fog_login_user", methods=['GET', 'POST'])
def fog_log():
    if request.method == 'POST':
        print(request.form['email'],"============")
        status = fog_user_login(request.form['email'], request.form['password'])
        print(status,"---------")
        for a,b,c in status:
            session['username'] = a
            session['email'] = b

        if status:            
            print(session["username"],"------------session")                       
            return render_template("/fog.html", m1="sucess",uname=session['username'])   ###,uname=session['username']
        else:
            print('m2')
            return render_template("fog_login.html", m2="Login Failed")

    else:
        return render_template("fog_login.html")



# ====================================================================



@app.route("/fog_data",methods=['GET', 'POST'])
def fog_show():
    
    data = fog_viewimages(session['username'])
	 
    print(type(data))
    return render_template("fog.html",user = data)



    # else:
    #     print('hii')
    #     return render_template('fog.html')
# ==========================search===================================================
@app.route("/search.html",methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        find = request.form['filesearch'] 
        print(find )
        data = user_search(session['username'],request.form['filesearch'] )
    
        print(data)
        return render_template("search.html",user = data)

    else:
        return render_template("search.html")



#==================================  cloud  ==============================================================
# ==================================== sign up ==============================
@app.route("/cl_signup", methods = ['GET','POST'])
def cl_rege():
    if request.method == 'POST':    
        id="0"
        status = cl_reg(request.form['username'],request.form['password'],request.form['email'])
        if status == 1:
            return render_template("cl_login.html",m1="sucess")
        else:
            return render_template("cl_signup.html")   
    else:
        return render_template("cl_signup.html")






@app.route("/cl_login_user", methods=['GET', 'POST'])
def cloud_login():
    if request.method == 'POST':
        print(request.form['email'],"============")
        status = cloudlogin(request.form['email'], request.form['password'])
        print(status,"---------")
        for a,b,c in status:
            session['username'] = a
            session['email'] = b

        if status:            
            print(session["username"],"------------session")                       
            return render_template("/cl_home.html", m1="sucess",uname=session['username'])   ###,uname=session['username']
        else:
            print('m2')
            return render_template("cl_login.html", m2="Login Failed")

    else:
        return render_template("cl_login.html")


#===============================================================================================
@app.route("/cl_data",methods=['GET', 'POST'])
def cl_show():
    
    data = cl_viewimages(session['username'])
	 
    print(type(data))
    return render_template("cl_home.html",user = data)




# =============================================================================



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5500,use_reloader=False)




