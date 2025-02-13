from flask import Flask

app=Flask(__name__)

# @app.route('/home')
# def home():
#     return "welcome to ML"

@app.route('/class')
def home():
    return "welcome to ML week6"



if __name__=='__main__':
    app.run(debug=True)