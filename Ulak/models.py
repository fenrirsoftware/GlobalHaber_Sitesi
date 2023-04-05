from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from json import loads


def readConfig():
    return loads(
        open(
            "config.json",
            mode="r",
            encoding="utf-8"
        ).read()
    )


app = Flask(__name__)

app.config['SECRET_KEY'] = '8963e76bfd5038857a3e7e2e42624e748f9f44b967ea56423445asdffg'

username = readConfig()["username"]
password = readConfig()["password"]
dbname = readConfig()["db_name"]

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"

db = SQLAlchemy(app)



class UlakNews(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1000))
    content = db.Column(db.String(1000))
    trtitle = db.Column(db.String(1000))
    trcontent = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
    domain_name = db.Column(db.String(1000))
    datetime = db.Column(db.String(1000))
    imageurl = db.Column(db.String(1000))

    def __init__(self, title, content, trtitle, trcontent, url, domain_name, datetime, imageurl) -> None:
        self.title = title
        self.content = content
        self.trtitle = trtitle
        self.trcontent = trcontent
        self.url = url
        self.domain_name = domain_name
        self.datetime = datetime
        self.imageurl = imageurl