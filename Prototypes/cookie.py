from flask import Flask, request, make_response, render_template 
from datetime import datetime, timedelta

app = Flask(__name__) 

@app.route('/') 
def vistors_count(): 
    # Converting str to int 
    count = int(request.cookies.get('visitors count', 0)) 
    # Getting the key-visitors count value as 0 
    count = count+1
    output = 'You visited this page for '+str(count) + ' times'
    resp = make_response(output) 
    resp.set_cookie('visitors count', str(count), secure=True, expires=datetime.now()+timedelta(seconds=15)) 
    return resp 
  
  
@app.route('/get') 
def get_vistors_count(): 
    count = request.cookies.get('visitors count') 
    return count 
  
@app.route('/details', methods = ['GET','POST']) 
def login(): 
	if request.method == 'POST': 
		name = request.form['username'] 
		output = 'Hi, Welcome '+name+ '' 
		resp = make_response(output) 
		resp.set_cookie('username', name) 
	return resp 

app.run(debug=True) 
