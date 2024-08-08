from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime

app = Flask(__name__)
db_path = 'library.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books 
                      (id INTEGER PRIMARY KEY, title TEXT, author TEXT, 
                       published_date TEXT, added_date TEXT)''')
    conn.commit()
    conn.close()

def get_books():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'title': row[1], 'author': row[2], 
             'published_date': row[3], 'added_date': row[4]} 
            for row in rows]

def get_book(book_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    row = cursor.fetchone()
    conn.close()
    return {'id': row[0], 'title': row[1], 'author': row[2], 
            'published_date': row[3], 'added_date': row[4]} if row else None

def add_book(data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, published_date, added_date) VALUES (?, ?, ?, ?)',
                   (data['title'], data['author'], data['published_date'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()
    return cursor.lastrowid

def update_book(book_id, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title = ?, author = ?, published_date = ? WHERE id = ?',
                   (data['title'], data['author'], data['published_date'], book_id))
    conn.commit()
    conn.close()
    return cursor.rowcount

def delete_book(book_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount

@app.route('/books', methods=['GET'])
def list_books():
    books = get_books()
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_details(book_id):
    book = get_book(book_id)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    if not all(key in data for key in ('title', 'author', 'published_date')):
        return jsonify({'error': 'Invalid data'}), 400
    book_id = add_book(data)
    return jsonify({'id': book_id}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book_details(book_id):
    data = request.json
    if not all(key in data for key in ('title', 'author', 'published_date')):
        return jsonify({'error': 'Invalid data'}), 400
    if update_book(book_id, data):
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book_details(book_id):
    if delete_book(book_id):
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
