from flask import Flask, render_template, json, request
from flask:ext.mysql import MySQL

app = Flask(__name__)

mysql = MysQL()

#MySQL configuraton
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'fourir96akbar'
app.config['MYSQL_DATABASE_DB'] = 'kuncir'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
	# return "Welcome!"
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signUp():
	#create user code will be here

	#read the posted values from the UI
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']

	#validate the received values
	if _name and _email and _password:
		return json.dumps({'html':'<span>All fields good!!</span>'})
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
	app.run()