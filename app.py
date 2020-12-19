from flask import Flask , render_template ,request
from flask_mysqldb import MySQL
import smtplib
app=Flask(__name__)
app.config['MYSQL_USER']='sql12378478'
app.config['MYSQL_PASSWORD']='FHkjlJkAeP'
app.config['MYSQL_HOST']='sql12.freemysqlhosting.net'
app.config['MYSQL_DB']='sql12378478'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route('/')
def index():
    # cur = mysql.connection.cursor()
    # print("Database opened successfully")
    # cur.execute('CREATE TABLE Arduino(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT  ,CLG VARCHAR(20),YEAR VARCHAR(20))')
    # cur.execute('CREATE TABLE Cloud(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
    # cur.execute('CREATE TABLE Cyber(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
    # cur.execute('CREATE TABLE Flutter(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
    # cur.execute('CREATE TABLE IOT(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
    # cur.execute('CREATE TABLE PCB(NAME VARCHAR(20),GENDER VARCHAR(20),EMAIL VARCHAR(20) PRIMARY KEY,NUM INT ,CLG VARCHAR(20),YEAR VARCHAR(20))')
    # print("Table created successfully")
    # mysql.connection.commit()
    # cur.close()
    return render_template('home.html')
@app.route('/home.html')
def home():
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
        if 1:
            d={}
            d['name']=request.form['name']
            d['gender']=request.form['gender']
            d['email']=request.form['email']
            d['num']=request.form['num']
            d['clg']=request.form['clg']
            d['year']=request.form['year']
            d['web']=request.form['web']
            #cur = mysql.connection.cursor()
            if d['web']=="Arduino":
                cur.execute("INSERT into Arduino(NAME,GENDER,EMAIL,NUM,CLG,YEAR)values(%s,%s,%s,%s,%s,%s)",(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="Cloud Computing":
                cur.execute("INSERT INTO Cloud(NAME,GENDER,EMAIL,NUM,CLG,YEAR)VALUES(%s,%s,%s,%s,%s,%s)",(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="Cyber Security":
                cur.execute("INSERT INTO Cyber(NAME,GENDER,EMAIL,NUM,CLG,YEAR)VALUES(%s,%s,%s,%s,%s,%s)",(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="Flutter":
                print('hi')
                #cur.execute("INSERT INTO Flutter(NAME,GENDER,EMAIL,NUM,CLG,YEAR)VALUES(%s,%s,%s,%s,%s,%s)",(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="IOT":
                cur.execute("INSERT INTO IOT(NAME,GENDER,EMAIL,NUM,CLG,YEAR)VALUES(%s,%s,%s,%s,%s,%s)",(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            elif d['web']=="PCB":
                cur.execute("INSERT INTO PCB(NAME,GENDER,EMAIL,NUM,CLG,YEAR)VALUES(%s,%s,%s,%s,%s,%s)",(d['name'],d['gender'],d['email'],d['num'],d['clg'],d['year']))
            #mysql.connection.commit()
            email_server=smtplib.SMTP("smtp.gmail.com",587)
            email_server.starttls()
            SUBJECT="Webinar registration"
            mail="rogopi42@gmail.com"

            TEXT="HI "+(d['name']).upper()+"\n           Greetings from RoGopi Software Solutions Webinar team! Thanks for your interest towards our webinar programme.Your registration for "+d['web']+" webinar is successful.The webinar link will be provided on the date of the webinar and the e-certificate will be provided at the end of the event.For any queries write to rogopi42@gmail.com"
            #msg='Subject: {}\n\n{}'.format(SUBJECT,TEXT)
            #msg="FROM : From RoGopi {} \n\n Subject : Webinar Registration \n\n {}".format('rogopi42@gmail.com',TEXT)
            msg=""" FROM : RoGopi %s\n"""%('Software Solution')
            ms0="""TO : %s %s\n"""%(d['name'],d['email'])
            msg=msg+ms0
            ms1="""Subject : Webinar Registration


            %s"""%(TEXT)
            msg=msg+ms1
            password="virat@18"
            email_server.login(mail,password)
            email_server.sendmail(mail,d['email'],msg)
            email_server.quit()
            return render_template('end.html')
        '''except Exception as e:
            print("dd",e.args)
            return render_template('error.html')'''
    else:
        return render_template('reg.html')
@app.route('/end.html')
def end():
    return render_template('end.html')
@app.route('/error.html')
def error():
    return render_template('error.html')
if __name__=="__main__":
    app.run()
