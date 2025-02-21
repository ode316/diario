#Import
from flask import Flask, render_template,request, redirect
#Connecting the database library
from flask_sqlalchemy import SQLAlchemy
from speech import capturar_audio,transcribir_audio_espaniol

app = Flask(__name__)
#Connecting SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Creating a db
db = SQLAlchemy(app)
#Creating a table

#Assignment #1. Create a db
class Card(db.Model):
    #Creating column fields
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Title
    title = db.Column(db.String(100), nullable=False)
    #Description
    subtitle = db.Column(db.String(300), nullable=False)
    #Text
    text = db.Column(db.Text, nullable=False)

    #Outputting the object and its
    def __repr__(self):
        return f'<Card {self.id}>'


#Running the page with the content
@app.route('/')
def index():
    #Outputting the objects from the DB
    #Assignment #2. Make it so that the DB objects are shown in index.html
    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html', cards=cards)

#Running the page with the card
@app.route('/card/<int:id>')
def card(id):
    #Assignment #2. Use the id to show the right card
    card = Card.query.get(id)

    return render_template('card.html', card=card)

#Running the page with card initialization
@app.route('/create')
def create():
    return render_template('create_card.html')
@app.route("/voice")
def voice():
    
    try:
        audio= capturar_audio()
        text= transcribir_audio_espaniol(audio)
    except:
        text="No se puede escuchar, vocaliza mejor"
    return render_template("create_card.html", text=text)


#The card's form
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Creating an object to pass to DB

        #Assignment #2. Create a way to store data in the DB
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)