# Author: Fallon Skeens
# Project: Module 4 Lab
# Description:

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

# Book database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

# Read books
@app.route('/books', methods=['POST'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': b.id, 'book_name': b.book_name,
                     'author': b.author, 'publisher': b.publisher}
                    for b in books])


# Update books
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    db.session.commit()
    return jsonify({'message': "Book updated"})

# Delete books
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)