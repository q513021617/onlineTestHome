from flask import Flask
from flask import render_template
from model.News import News, session
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/news')
def news():
    news = session.query(News).all()
    headsnews=session.query(News).limit(4).all()
    print(news)
    return render_template("news.html", news=news,headsnews=headsnews)


@app.route('/news/<id>')
def newsdetail(id):
    new = session.query(News).filter(News.id == id).one()

    print(new)
    return render_template("newsdetail.html", new=new)


if __name__ == '__main__':
    app.run(Debug=True)
