from flask import Flask , render_template ,request
import smtplib
import sqlite3
con=sqlite3.connect('pro.db',check_same_thread=False)
cur=con.cursor()
#cur.execute('CREATE TABLE Arduino(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
#cur.execute('CREATE TABLE Cloud(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
#cur.execute('CREATE TABLE Cyber(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
#cur.execute('CREATE TABLE Flutter(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
#cur.execute('CREATE TABLE IOT(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
#cur.execute('CREATE TABLE PCB(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
app=Flask(__name__)
@app.route('/')
@app.route('/home.html')
def index():
    return render_template('home.html')
@app.route('/arduino.html')
def arduino():
    return render_template('arduino.html')
@app.route('/iot.html')
def iot():
    return render_template('iot.html')
@app.route('/cloud_computing.html')
def cloud_computing():
    return render_template('cloud_computing.html')
@app.route('/cyber_security.html')
def cyber_security():
    return render_template('cyber_security.html')
@app.route('/flutter.html')
def flutter():
    return render_template('flutter.html')
@app.route('/pcb.html')
def pcb():
    return render_template('pcb.html')
@app.route('/reg.html',methods=['POST','GET'])
def reg():
    if request.method=='POST':
        try:
            d={}
            d['name']=request.form['name']
            d['gender']=request.form['gender']
            d['email']=request.form['email']
            d['num']=request.form['num']
            d['clg']=request.form['clg']
            d['year']=request.form['year']
            d['web']=request.form['web']
            if d['web']=="Arduino":
                cur.execute('INSERT INTO Arduino(NAME,GENDER,EMAIL,NUM,CLG,YEAR) VALUES(?,?,?,?,?,?)',(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="Cloud Computing":
                cur.execute('INSERT INTO Cloud(NAME,GENDER,EMAIL,NUM,CLG,YEAR) VALUES(?,?,?,?,?,?)',(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="Cyber Security":
                cur.execute('INSERT INTO Cyber(NAME,GENDER,EMAIL,NUM,CLG,YEAR) VALUES(?,?,?,?,?,?)',(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="Flutter":
                cur.execute('INSERT INTO Flutter(NAME,GENDER,EMAIL,NUM,CLG,YEAR) VALUES(?,?,?,?,?,?)',(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="IOT":
                cur.execute('INSERT INTO IOT(NAME,GENDER,EMAIL,NUM,CLG,YEAR) VALUES(?,?,?,?,?,?)',(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="PCB":
                cur.execute('INSERT INTO PCB(NAME,GENDER,EMAIL,NUM,CLG,YEAR) VALUES(?,?,?,?,?,?)',(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year'])) 
            con.commit()
            email_server=smtplib.SMTP("smtp.gmail.com",587)
            email_server.starttls()
            SUBJECT="Webinar registration"
            mail="rogopi42@gmail.com"
            
            TEXT="HI "+(d['name']).upper()+"\n           Greetings from RoGopi Software Solutions Webinar team! Thanks for your interest towards our webinar programme.Your registration for "+d['web']+" webinar is successful.The webinar link will be provided on the date of the webinar and the e-certificate will be provided at the end of the event.For any queries write to rogopi42@gmail.com"
            #msg='Subject: {}\n\n{}'.format(SUBJECT,TEXT)
            #msg="FROM : From RoGopi {} \n\n Subject : Webinar Registration \n\n {}".format('rogopi42@gmail.com',TEXT)
            msg=""" FROM : RoGopi %s\n"""%('Software Solution')
            ms0="""TO : %s\n"""%(d['email'])
            msg=msg+ms0
            ms1="""Subject : Webinar Registration


            %s"""%(TEXT)
            msg=msg+ms1
            password="virat@18"
            email_server.login(mail,password)
            email_server.sendmail(mail,d['email'],msg)
            email_server.quit()
            return render_template('end.html')
        except Exception as e:
            return render_template('error.html')
    else:
        return render_template('reg.html')
@app.route('/end.html')
def end():
    return render_template('end.html')
@app.route('/error.html')
def error():
    return render_template('error.html')
if __name__=="__main__":
    app.run(debug=True)