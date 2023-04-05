import requests
from bs4 import BeautifulSoup as bs
from xmltodict import parse
from translate import translator
from database import addNews
from datetime import datetime
from functions import returnFormatDate


class ScrapingNews(object):
    def __init__(self) -> None:
        super().__init__()
        self.arstechnica = "https://feeds.arstechnica.com/arstechnica/technology-lab"
        self.computerWorld = "https://www.computerworld.com/news/index.rss"
        self.vox = "https://www.vox.com/rss/technology/index.xml"
        self.theVerge = "https://www.theverge.com/rss/index.xml"
        self.engadget = "https://www.engadget.com/rss.xml"
        self.toLinux = "https://9to5linux.com/feed"
        self.techSpot = "https://www.techspot.com/backend.xml"
        self.venturebeat = "https://feeds.feedburner.com/venturebeat/SZYF"
        self.gsmArena = "https://www.gsmarena.com/rss-news-reviews.php3"
        self.darkReading = "https://www.darkreading.com/rss.xml"

    def getRssContent(self, url: str):
        self.__requests = requests.get(url=url)
        if self.__requests.status_code == 200:
            self.__parse = parse(self.__requests.text)["rss"]["channel"]

            self.link = [x["link"] for x in self.__parse["item"]]
            self.title = [x["title"] for x in self.__parse["item"]]
            self.date = [x["pubDate"] for x in self.__parse["item"]]
            if self.title and self.link and self.date:
                return self.title, self.link, self.date

    def arstechnicaNewsScraping(self):
        self.title, self.link, self.date = self.getRssContent(
            url=self.arstechnica)
        for title, link, date in zip(self.title, self.link, self.date):
            self.__contReq = requests.get(url=link)
            if self.__contReq.status_code == 200:
                self.Cont = bs(self.__contReq.content, "lxml")
                self.image = self.Cont.find(
                    "figure", class_="intro-image intro-left").find("img").get("src")
                self.content = self.Cont.find(
                    "div", class_="article-content post-page").find_all("p")
                self.source = ("".join(x.getText() for x in self.content))
                contentTr, titleTr = translator(
                    content=self.source, title=title)
                addNews(
                    title=str(title),
                    content=self.source,
                    trtitle=titleTr,
                    trcontent=contentTr,
                    url=link,
                    domain_name="Arstechnica",
                    datetime=returnFormatDate(date),
                    imageurl=self.image,

                )

    def computerWorldRss(self):
        try:
            self.title, self.link, self.date = self.getRssContent(
                url=self.computerWorld)
            if self.title and self.link and self.date:
                for title, link, date in zip(self.title, self.link, self.date):

                    self.__contReq = requests.get(url=link)
                    if self.__contReq.status_code == 200:
                        self.Cont = bs(self.__contReq.content, "lxml")
                        self.image = self.Cont.find(
                            class_="lazy").get("data-original")
                        self.contentEng = self.Cont.find(
                            "div", attrs={"id": "drr-container"}).find_all("p")
                        self.source = ("".join([x.getText()
                                       for x in self.contentEng]))
                        contentTr, titleTr = translator(
                            content=self.source, title=title)
                        addNews(
                            title=str(title),
                            content=self.source,
                            trtitle=titleTr,
                            trcontent=contentTr,
                            url=link,
                            domain_name="Computerworld",
                            datetime=returnFormatDate(date),
                            imageurl=self.image,

                        )
        except:
            ...

    def voxGetRss(self):
        __req = requests.get(url=self.vox)
        if __req.status_code == 200:
            __parse = parse(__req.text)

            content = __parse["feed"]["entry"]
            title = [x["title"] for x in content]
            pubDate = [x["published"] for x in content]
            link = [x["id"] for x in content]
            if title and pubDate and link:
                return title, link, pubDate

    def voxParseContent(self):
        title, link, date = self.voxGetRss()
        for titleX, url, time in zip(title, link, date):
            self.__contReq = requests.get(url=url)
            if self.__contReq.status_code == 200:
                self.Cont = bs(self.__contReq.content, "lxml")
                self.content = self.Cont.find(
                    "div", class_="c-entry-content").find_all("p")
                self.title = self.Cont.find(
                    "h1", class_="c-page-title").getText()
                page = ' '.join(p.getText() for p in self.content if not p.findParent(
                    "div", class_="c-article-footer"))
                self.imageLink = self.Cont.find(
                    "span", class_="e-image__image")["data-original"]
                contentTr, titleTr = translator(content=page, title=titleX)
                addNews(
                    title=str(titleX),
                    content=page,
                    trtitle=titleTr,
                    trcontent=contentTr,
                    url=url,
                    domain_name="Vox",
                    datetime=returnFormatDate(time),
                    imageurl=self.imageLink,

                )

    def getRssTheVerge(self):
        __requestsRss = requests.get(url=self.theVerge)
        if __requestsRss.status_code == 200:
            __parse = parse(__requestsRss.text)["feed"]["entry"]
            link = [x["id"] for x in __parse]
            date = [x["published"] for x in __parse]
            title = [x["title"] for x in __parse]
            return title, link, date

    def theVergeParse(self):
        try:
            title, link, date = self.getRssTheVerge()
            for titleRss, url, datetime in zip(title, link, date):
                __requests = requests.get(url=url)
                if __requests.status_code == 200:
                    __parse = bs(__requests.content, "lxml")
                    p_tag = __parse.find(attrs={"id": "content"}).find_all(
                        "div", class_="duet--article--article-body-component")
                    page_text = ' '.join(
                        e.text for p in p_tag for e in p.findAll(text=True))
                    image = __parse.find(
                        "figure", class_="w-full").find("img").get("src")
                    contentTr, titleTr = translator(
                        content=page_text, title=titleRss)
                    addNews(
                        title=str(titleRss),
                        content=page_text,
                        trtitle=titleTr,
                        trcontent=contentTr,
                        url=url,
                        domain_name="TheVerge",
                        datetime=returnFormatDate(datetime),
                        imageurl=image,

                    )
        except Exception:
            ...

    def getEngadgetRss(self):
        __requestsRss = requests.get(url=self.engadget)
        if __requestsRss.status_code == 200:
            __parse = parse(__requestsRss.text)["rss"]["channel"]["item"]
            title = [x["title"] for x in __parse]
            link = [x["link"] for x in __parse]
            date = [x["pubDate"] for x in __parse]

            return title, link, date

    def engadgetParse(self):

        title, link, date = self.getEngadgetRss()
        for titleRss, url, dateTime in zip(title, link, date):
            try:
                __requests = requests.get(url=url)
                if __requests.status_code == 200:
                    self.parseContent = bs(__requests.content, "lxml")
                    self.__content = self.parseContent.find(
                        "div", class_="article-text").find_all("p")
                    page_text = ' '.join(
                        e.text for p in self.__content for e in p.findAll(text=True))
                    try:

                        image = self.parseContent.find(
                            "img", class_="W(100%) H(a)").get("src")
                    except AttributeError:
                        image = "https://png.pngtree.com/thumb_back/fh260/background/20210923/pngtree-news-red-and-blue-stripe-tv-background-image_902549.png"
                    contentTr, titleTr = translator(
                        content=page_text, title=titleRss)

                    addNews(
                        title=str(titleRss),
                        content=page_text,
                        trtitle=titleTr,
                        trcontent=contentTr,
                        url=url,
                        domain_name="Engadget",
                        datetime=returnFormatDate(dateTime),
                        imageurl=image,

                    )

            except AttributeError:
                continue

    def getToLinuxRss(self):
        __requestsRss = requests.get(url=self.toLinux)
        if __requestsRss.status_code == 200:
            __parse = parse(__requestsRss.text)["rss"]["channel"]["item"]
            title = [x["title"] for x in __parse]
            link = [x["link"] for x in __parse]
            date = [x["pubDate"] for x in __parse]
            return title, link, date

    def toLinuxParse(self):
        try:
            title, link, date = self.getToLinuxRss()
            for titleRss, url, dateTime in zip(title, link, date):
                self.__requests = requests.get(url=url)
                if self.__requests.status_code == 200:
                    __parseContent = bs(self.__requests.content, "lxml")
                    image = __parseContent.find(
                        "div", class_="post-thumbnail").find("img").get("src")
                    p_tag = __parseContent.find(
                        "div", class_="entry-content").find_all("p")
                    page_text = ' '.join(
                        e.text for p in p_tag for e in p.findAll(text=True))
                    contentTr, titleTr = translator(
                        content=page_text, title=titleRss)

                    addNews(
                        title=str(titleRss),
                        content=page_text,
                        trtitle=titleTr,
                        trcontent=contentTr,
                        url=url,
                        domain_name="TheVerge",
                        datetime=returnFormatDate(dateTime),
                        imageurl=image,

                    )

        except:
            ...

    def getTechSpot(self):
        try:
            self.title, self.link, self.date = self.getRssContent(
                url=self.techSpot)
            for titleRss, url, date in zip(self.title, self.link, self.date):
                __req = requests.get(url=url)
                if __req.status_code == 200:
                    __parseContent = bs(__req.content, "lxml")
                    self.content = __parseContent.find(
                        "div", class_="articleBody").find_all("p")
                    page_text = ' '.join(
                        e.text for p in self.content for e in p.findAll(text=True))
                    try:
                        image = __parseContent.find(
                            "picture", class_="intro-pic").find("img").get("src")
                    except AttributeError:
                        image = "https://png.pngtree.com/thumb_back/fh260/background/20210923/pngtree-news-red-and-blue-stripe-tv-background-image_902549.png"

                    contentTr, titleTr = translator(
                        content=page_text, title=titleRss)
                    addNews(
                        title=str(titleRss),
                        content=page_text,
                        trtitle=titleTr,
                        trcontent=contentTr,
                        url=url,
                        domain_name="Techspot",
                        datetime=returnFormatDate(date),
                        imageurl=image,

                    )

        except:
            ...

    def ventureBeat(self):
        try:
            self.title, self.link, self.date = self.getRssContent(
                url=self.venturebeat)
            for titleRss, url, date in zip(self.title, self.link, self.date):
                __req = requests.get(url=url)
                if __req.status_code == 200:
                    __parseContent = bs(__req.content, "lxml")
                    content = __parseContent.find(
                        "div", class_="article-content").find_all("p")[1:-1]
                    page_text = ' '.join(
                        e.text for p in content for e in p.findAll(text=True))
                    try:
                        image = __parseContent.find(
                            "img", class_="skip-lazy").get("src")
                    except AttributeError:
                        image = "https://png.pngtree.com/thumb_back/fh260/background/20210923/pngtree-news-red-and-blue-stripe-tv-background-image_902549.png"

                    contentTr, titleTr = translator(
                        content=page_text, title=titleRss)

                    addNews(
                        title=str(titleRss),
                        content=page_text,
                        trtitle=titleTr,
                        trcontent=contentTr,
                        url=url,
                        domain_name="Venturebeat",
                        datetime=returnFormatDate(date),
                        imageurl=image,

                    )

        except:
            ...

    def getRssGsmArena(self):
        try:

            self.title, self.link, self.date = self.getRssContent(
                url=self.gsmArena)
            for titleRss, url, date in zip(self.title, self.link, self.date):
                __req = requests.get(url=url)
                if __req.status_code == 200:
                    __parseContent = bs(__req.content, "lxml")
                    self.content = __parseContent.find(
                        "div", attrs={"id": "review-body"}).find_all("p")
                    page_text = ' '.join(
                        e.text for p in self.content for e in p.findAll(text=True))
                    try:
                        image = __parseContent.find(
                            "img", class_="center-stage-background").get("src")

                    except AttributeError:
                        image = "https://png.pngtree.com/thumb_back/fh260/background/20210923/pngtree-news-red-and-blue-stripe-tv-background-image_902549.png"

                    contentTr, titleTr = translator(
                        content=page_text, title=titleRss)
                    addNews(
                        title=str(titleRss),
                        content=page_text,
                        trtitle=titleTr,
                        trcontent=contentTr,
                        url=url,
                        domain_name="GsmArena",
                        datetime=returnFormatDate(date),
                        imageurl=image,

                    )
        except:
            ...

    def darkReadingRss(self):
        req = requests.get(url=self.darkReading)
        if req.status_code == 200:
            parserss = parse(req.text)["rss"]["channel"]["item"]
            title = [x["title"] for x in parserss]
            link = [x["link"] for x in parserss]
            date = [x["pubDate"] for x in parserss]
            return title, link, date

    def darkReadingParse(self):
        try:
            title, link, date = self.darkReadingRss()
            for titleRss, url, date in zip(title, link, date):
                __req = requests.get(url=url)
                if __req.status_code == 200:
                    __parseContent = bs(__req.content, "lxml")
                    try:
                        image = __parseContent.find(
                            "div", class_="featured-image").find("picture").find("source").get("srcset")
                    except AttributeError:
                        image = "https://png.pngtree.com/thumb_back/fh260/background/20210923/pngtree-news-red-and-blue-stripe-tv-background-image_902549.png"
                    content = __parseContent.find(
                        "div", class_="article-content").find_all("p")
                    page_text = ' '.join(
                        e.text for p in content for e in p.findAll(text=True))

                    contentTr, titleTr = translator(
                        content=page_text, title=titleRss)
                    if page_text and image and title and titleTr and date:
                        addNews(
                            title=str(titleRss),
                            content=page_text,
                            trtitle=titleTr,
                            trcontent=contentTr,
                            url=url,
                            domain_name="Darkreading",
                            datetime=returnFormatDate(date),
                            imageurl=image,

                        )
        except Exception:
            ...


def mainFunc():

    News = ScrapingNews()
    News.arstechnicaNewsScraping()
    News.computerWorldRss()
    News.voxParseContent()
    News.theVergeParse()
    News.engadgetParse()
    News.toLinuxParse()
    News.getTechSpot()
    News.ventureBeat()
    News.getRssGsmArena()
    News.darkReadingParse()


if __name__ == "__main__":
    mainFunc()
