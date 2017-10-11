from flask import Flask
from flask import render_template
app = Flask(__name__)


# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
	return render_template('index.html')




if __name__ == "__main__":
        app.run(host='0.0.0.0', port='80') #Run the flask app at port 5000
