from flask import Flask,render_template,request, session, redirect, url_for
import os
import pprint
from pymongo import MongoClient as mc
app=Flask(__name__)
app.secret_key = os.urandom(24)

connection = mc('localhost')
database = connection.studentdb
collection = database.studentinfo


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/AdminLogin")
def AdminLogin():
	return render_template("adminlogin.html")

@app.route("/AdminPage")
def AdminPage():
	return render_template("MainAdminPage.html")


@app.route("/StaffLogin")
def StaffLogin():
	return render_template("stafflogin.html")

@app.route("/StaffPage")
def StaffPage():
	return render_template("staffpage.html")

@app.route("/StudentRegister", methods=['POST','GET'])
def StudentRegister():
	if request.method == 'POST':
		existing_user = collection.find_one({'Admission_number': request.form['Admission_number']})
		if existing_user is None:
			sname = request.form['Student_name']
			admno = request.form['Admission_number']
			fname = request.form['Father_name']
			mname = request.form['Mother_name']
			doj   = request.form['doj']
			doc   = request.form['coursecomplete']
			dept  = request.form['department']
			pwd   = request.form['password']
			sex   = request.form['gender']
			dob   = request.form['dob']
			rel   = request.form['relegion']
			caste = request.form['caste']
			s_caste= request.form['sub_caste']
			course= request.form['course']
			phno  = request.form['contact_no']
			email = request.form['email']
			adno  = request.form['aadhar_no']
			age   = request.form['Age']
			bgp   = request.form['bloodgroup']
			addr  = request.form['address']
			city  = request.form['city']
			s_data={'Student_name' : sname,'Admission_number' : admno, 'Father_name' : fname, 'Mother_name' : mname, 'doj' : doj,
			'coursecomplete' : doc, 'department' : dept, 'password' : pwd, 'gender' : sex, 'dob' : dob, 'relegion' : rel, 'caste' : caste,
			'sub_caste' : s_caste, 'course' : course, 'contact_no' : phno, 'email' : email, 'aadhar_no' : adno, 'Age' : age,
			'bloodgroup' :bgp, 'address' : addr, 'city' : city}
			collection.insert_one(s_data)
			session['Admission_number'] = request.form['Admission_number']
			print("data posted Successfully")
			return render_template("submitted.html",sname = sname)
		return render_template("errors.html")
	return render_template("studentreg2.html")



@app.route('/StudentLogin', methods=['POST','GET'])
def Studentlogin():
	if request.method == 'POST':
		login_user = collection.find_one(dict(Admission_number=request.form['Admission_number']))
		pprint.pprint(login_user)
		if login_user:
			if request.form['pass'] == login_user['password']:
				session['Admission_number'] = request.form['Admission_number']
				return redirect(url_for('loggedin'))
		return 'Invalid username/password combination'
	return render_template("studentlogin.html")

@app.route('/LoggedIn')
def loggedin():
    if 'Admission_number' in session:
        return 'You are logged in as ' + session['Admission_number']

    return render_template('logged.html')



@app.route("/addition")
def add(a=10,b=20):
	d = a+b
	return render_template("first.html",display=d)

@app.route("/webform")
def display():
	show = "flask jinji webform"
	return render_template("first.html", display=show)


@app.route("/fileinput")
def input():
	return render_template("fileinput.html")


'''
@app.route('/filewriting', methods=['POST','GET'])
def filewrite():
    a = request.form["i1"]
    b = request.form["i2"]
    c = request.form["i3"]
    print(a)
    print(b)
    print(c)
    x = open("index.txt", "a")
    x.write("My Name is:"+a+"\nMy Number is:"+b+"\nMy Email is:"+c+"\n")
    x.close()
    return render_template('success.html')
'''



@app.route('/filewriting', methods=['POST','GET'])
def insert():
	a = request.form["i1"]
	b = request.form["i2"]
	c = request.form["i3"]
	data = {'Name' : a, 'Sid' : b, 'email' :c }
	collection.insert_one(data)
	print("data posted Successfully")
	return render_template('success.html')


@app.route("/loggeduser")
def display2():
	
	for record in collection.find({'Name':'Raviteja'}):
		name = record["Name"]
		scno = record['Scno']
	return render_template('logged.html',name = name, scno = scno)
			


'''return record['Name']
	return render_template('logged.html',a=record['Name'])'''

 
	
	



if __name__ == '__main__':
	app.secret_key = os.urandom(24)
	app.run(debug="True")