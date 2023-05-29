from flask import Flask, jsonify, abort, request, json, render_template
import socket
app = Flask(__name__)

def hostdetails():
     hostname=socket.gethostname()
     ip=socket.gethostbyname(hostname)

     return  hostname, ip

@app.route("/")
def hello_world():
  return "<p> hello world </p>"

@app.route('/health')
def health():
      return jsonify(
        status= "OK"
    )

@app.route("/details")
def details():
    hostname,ip =hostdetails()
    return render_template('index.html', hostname=hostname,ip=ip) 


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',port=5000,use_reloader=False)