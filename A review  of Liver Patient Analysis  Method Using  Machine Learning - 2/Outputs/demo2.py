from flask import Flask, render_template, request

app = Flask(__name__

  @app.route('/')
  def home():
    return render_template('home.html')

@app.route('/getdata', method=('post'))
def data():
    name1 = request.form['fname']
    name2 = request.form['lname']
    age = request.form['age']
    pritn(name1, name2,int(age))
    if int(age)> 18:
        text = str(name1)+str(name2)+'you are eligible for vote'
    else:
        text = str(name1)+str(name2)+'you are not eligible for vote'
  return render_template('output.html' , output=text)

if __name__ == '__main__' :
    app.run()