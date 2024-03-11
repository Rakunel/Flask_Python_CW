from flask import Flask 
app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World Clarusway"

@app.route("/second")
def head2():
    return "Fenerin Maci Var"

@app.route("/third")
def head3():
    return "Sampiyon Fener"

@app.route("/forth/<string:id>")
def head4(id):
    return f'Fenerin total puani = {id}'




if __name__ == '__main__':

    # app.run(debug=True, port=30000)
    app.run(host= '0.0.0.0', port=8081)