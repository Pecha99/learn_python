from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/news/')
def news():
    return 'Новости'


@app.route('/news/detail/<int:id>')
def news1(id):
    news = [{'title': 'Удивительное событиие в школе',
             'text': 'Какой-то текст новости'},
            {'title': 'Случай в зоопарке',
             'text': 'Текст новости про зоопарк'}]

    title = news[id]['title']
    text = news[id]['text']

    return render_template('news_detail.html', title=title, text=text)

@app.route('/category/<string:name>')
def category(name):
    return f'Новость {name}'

if __name__ == '__main__':
    app.run(debug=True)