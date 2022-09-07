from flask import Flask
import os
import socketapp = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/>"

return html.format(name=os.getenv("NAME", "world", hostname=socket.gethostname())

if __name__ == '__main__': 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port=80)
