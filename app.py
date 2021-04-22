from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
db = SQLAlchemy(app)

class Bookings(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username= db.Column(db.String, nullable=False)
   email= db.Column(db.String, nullable=False)
   phone= db.Column(db.Integer, nullable=False)
   guests = db.Column(db.Integer, nullable=False)
   rooms = db.Column(db.Integer, nullable=False)
   view = db.Column(db.String, nullable=False)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/bookRoom', methods=['POST', 'GET'])
def bookRoom():
    if request.method == 'POST':
        booking = Bookings(username=request.form['name'], email=request.form['email'], phone=request.form['phone'], guests=request.form['numofguests'], rooms=request.form['rooms'], view=request.form['view'])
        try:
            db.session.add(booking)
            db.session.commit()
            return 'successsful'#redirect('/getRooms')
        except Exception as e:
            print(e.message)

    else:
        return render_template('bookRoom.html')

if __name__ == '__main__':
    app.run(debug=True)