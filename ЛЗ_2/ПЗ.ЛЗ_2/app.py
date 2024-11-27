from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    contact_no = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Contact('{self.name}', '{self.email}')"

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    success_message = None 

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact_no = request.form['contact_no']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, contact_no=contact_no, message=message)
        db.session.add(new_contact)
        db.session.commit()

        success_message = "Your message has been sent successfully!"  # Устанавливаем сообщение об успехе

    recent_contacts = Contact.query.order_by(Contact.id.desc()).limit(5).all()

    return render_template('index.html', success_message=success_message, recent_contacts=recent_contacts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
