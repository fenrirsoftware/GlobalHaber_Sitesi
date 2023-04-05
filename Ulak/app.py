from flask import redirect, redirect, render_template
from functions import returnTrAndEngWorldCOunt
from models import *
from flask_paginate import Pagination, get_page_args
from database import getTotal

def get_users(offset=0, per_page=3):
    return getTotal()[offset: offset + per_page]


@app.route("/")
def index():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(getTotal())
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap3')
    
    return render_template("index.html",
            
            data = getTotal() ,
            users=pagination_users,
            page=page,
            per_page=per_page,
            pagination=pagination)

@app.route("/detay/<int:id>/")
def details(id: int):
    value = db.session.query(UlakNews).filter(UlakNews.id == id).first()
    tr, eng = returnTrAndEngWorldCOunt(value.trcontent, value.content)
    if value:
        return render_template(
            "details.html",
            türkceKelime = tr,
            ingilizceKelime = eng,
             value = value
        
    )
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
