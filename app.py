from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 用一个简单的列表来存储图书信息，每本书是一个字典
books = [
    {"id": 1, "title": "Python", "author": "Ray", "year": 2021},
    {"id": 2, "title": "Java", "author": "Ray1", "year": 2020},
]

# 首页，展示图书列表
@app.route('/')
def index():
    return render_template('index.html', books=books)

# 添加图书
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = int(request.form['year'])
        book_id = len(books) + 1
        book = {"id": book_id, "title": title, "author": author, "year": year}
        books.append(book)
        return redirect(url_for('index'))
    return render_template('add_book.html')

# 删除图书
@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
