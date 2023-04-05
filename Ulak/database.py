from models import *


def addNews(title, content, trtitle, trcontent, url, domain_name, datetime, imageurl):
    with app.app_context():
        db.create_all()
        if not db.session.query(UlakNews).filter(UlakNews.url == url).count():
            news = UlakNews(
                title=title,
                content=content,
                trtitle=trtitle,
                trcontent=trcontent,
                url=url,
                domain_name=domain_name,
                datetime=datetime,
                imageurl=imageurl


            )
            db.session.add(news)
            db.session.commit()
            print(url, " Eklendi")

        else:
            print(url, " Url veritabanında bulunuyor")

def getTotal():
    with app.app_context():
        db.create_all()
        return UlakNews.query.all()