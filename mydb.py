
import MySQLdb
from flask import session

import os




def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="cloud")
    c = _conn.cursor()

    return c, _conn
    
    
#-------------------------------------Reg------------------------------------------
def reg(username, password, email, ):
    try:
        c, conn = db_connect()
        print(id,username, password, email)
        j = c.execute("insert into user (username,email,password) values ('"+username +
                      "','"+email+"','"+password+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

# -------------------------------------Login --------------------------------------
def user_login(email, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from user where email='"+email+"' and password='"+password+"'")
        data = c.fetchall()
        print(data)
        for a in data:
           session['email'] = a[0]
       
        c.fetchall()
        conn.close()
        return data
    except Exception as e:
        return(str(e))

# ================================================================
def user_upload(file,filename):
    try:
        c, conn = db_connect()
        print(file)
        username = session['username']  
        print(username)      
        print(filename)      
        
        data = file.read()
        print(data.decode('utf-8'),'----------------------')
        upload=data.decode('utf-8')
        c.execute("select name from user_data where  name='"+data.decode('utf-8') +"' ")
        result = c.fetchall()
        print(result ,'result')
        print(len(result))
        if len(result)==0:
            print('hiiiiiiii')
            j = c.execute("insert into user_data (filename,name,username) values ('"+filename+"','"+data.decode('utf-8')+"','"+username+"')")
            conn.commit()
            conn.close()
            print(j,"fog cloud")
            return j
        else:
            j = c.execute("insert into fog (filename,name,username) values ('"+filename+"','"+data.decode('utf-8')+"','"+username+"')")
            conn.commit()
            conn.close()
            print(j,'cloud')
            return j
    except Exception as e:
        print(e)
        return(str(e))


# ==============================================================================================
def user_viewimages(username):
    c, conn = db_connect()
    c.execute("select * from user_data where  username='"+username +"'")
    result = c.fetchall()
    conn.close()
    print(result)
    return result
# ==================================================================================================
def fog_viewimages(username):
    c, conn = db_connect()
    c.execute("select * from fog; ")
    result = c.fetchall()
    conn.close()
    print(result,'database')
    return result
    
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fog_reg(username, password, email, ):
    try:
        c, conn = db_connect()
        print(id,username, password, email)
        j = c.execute("insert into foguser (username,email,password) values ('"+username +
                      "','"+email+"','"+password+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

# ===============================================================================================================
def fog_user_login(email, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from foguser where email='"+email+"' and password='"+password+"'")
        data = c.fetchall()
        print(data)
        for a in data:
           session['email'] = a[0]
       
        c.fetchall()
        conn.close()
        return data
    except Exception as e:
        return(str(e))
# ===========================================SEARCH================================================
def user_search(username,search):
    c, conn = db_connect()
    c.execute("SELECT * FROM user_data WHERE BINARY name LIKE '%"+ search + "%'")
  
    result = c.fetchall()
    conn.close()
    print(result)
    return result


def cl_viewimages(username):
    c, conn = db_connect()
    c.execute("select * from user_data; ")
    result = c.fetchall()
    conn.close()
    print(result,'database')
    return result

#-------------------------------------cloud Reg------------------------------------------
def cl_reg(username, password, email, ):
    try:
        c, conn = db_connect()
        print(id,username, password, email)
        j = c.execute("insert into coluduser (username,email,password) values ('"+username +
                      "','"+email+"','"+password+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

# ------------------------------------cloud -Login --------------------------------------
def cloudlogin(email, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from coluduser where email='"+email+"' and password='"+password+"'")
        data = c.fetchall()
        print(data)
        for a in data:
           session['email'] = a[0]
       
        c.fetchall()
        conn.close()
        return data
    except Exception as e:
        return(str(e))

# =============