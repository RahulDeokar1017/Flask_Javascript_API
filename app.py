from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Abhi117093@localhost/sample_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    Mobile_number = db.Column(db.Integer, primary_key=True)

    def __init__(self, username, mobile_number):
        self.name = username
        self.Mobile_number = mobile_number

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    mobile = data.get('mobile')

    new_user = User(name, mobile)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    # Here, you can process the received data as needed
    print(f"Received Data - Name: {name}, Mobile: {mobile}")

    return jsonify({"status": "success", "message": "Data submitted successfully"})

if __name__ == '__main__':
    with app.app_context():
        # Create the database tables before running the app
        db.create_all()
    app.run(debug=True)
