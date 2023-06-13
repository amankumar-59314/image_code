from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return "<h1>Hello,World</h1>"

if __name__=="__main__": 
    app.run(host="0.0.0.0")                                                       

