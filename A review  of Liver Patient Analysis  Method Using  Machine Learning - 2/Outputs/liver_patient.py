from flask import Flask #importing flask

app = Flask(__name__) #initializing flask

@app.route('/')
def hello():
    return 'Hello world'
if __name__ == '__main__': #Running application with condition
    app.run()


