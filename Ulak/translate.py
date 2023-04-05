from deep_translator import GoogleTranslator

def getTextFormat(s, maxlength):
        start = 0
        end = 0
        while start + maxlength  < len(s) and end != -1:
            end = s.rfind(" ", start, start + maxlength + 1)
            yield s[start:end]
            start = end +1
        yield s[start:]


def translator(content: str, title: str) -> str:
    contentTr = "".join([
        GoogleTranslator(source="auto", target="tr").translate(x)
        for x in getTextFormat(content, 4999)
    ])
    
    titleTr = "".join([
        GoogleTranslator(source="auto", target="tr").translate(x)
        for x in getTextFormat(title, 4999)
    ])

    return contentTr, titleTr
