
from datetime import datetime


def returnFormatDate(time):
    try:
        date_obj = (datetime.strptime(time, "%a, %d %b %Y %H:%M:%S %z"))

        return (date_obj.strftime("%Y-%m-%d %H:%M:%S"))
    except:
        return time



def returnTrAndEngWorldCOunt(tr_word, eng_world):
    tr = (list(tr_word.split(" ")))
    eng = (list(eng_world.split(" ")))
    return len(tr), len(eng)




