from flask import Flask,render_template
import pickle
import sklearn

app = Flask(__name__)

model = pickle.load(open('Direct_Bilirubin_rf.pk1','rb'))

@app.route('/')
def about():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')


if __name__ == '__main__':
    app.run()


