
from flask import *

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def Home():
    return render_template('index.html')
	
@app.route("/add", methods = ['POST'])
def add():
	if request.method == 'POST':
		a = int(request.form['fn'])
		b = int(request.form['sn'])
		s = a+b
		
		return render_template('index.html', results = "The sum of two numbers are {}".format(s))
	else:
		return render_template('index.html')
		
		

if __name__ == "__main__":
	app.run(debug = True)