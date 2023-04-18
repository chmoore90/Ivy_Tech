from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name} | {self.author} | {self.publisher}"



@app.route("/")
def index():
    return "Hello"


@app.get("/books")
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {"id": book.id, "book_name": book.book_name, "author": book.author, "publisher": book.publisher}
        output.append(book_data)

    return {"book": output}


@app.route("/books/<id>")
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}


@app.route("/books", methods=["POST"])
def add_book():
    book = Book(name=request.json["book_name"], author=request.json["author"], publisher=request.json["publisher"])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id}
