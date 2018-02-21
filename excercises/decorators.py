def make_italic(fn):
    print fn()
    print "---"
    def wrapped():
        return "<i>"+fn()+"</i>"
    return wrapped


def make_bold(fn):
    print fn()
    print "++++"
    def wrapped():
        return "<b>"+fn()+"</b>"
    return wrapped



def make_underline(fn):
    print fn()
    print "****"
    def wrapped():
        return "<u>"+fn()+"</u>"
    return wrapped

@make_underline
@make_italic
@make_bold

def hello():
    return "hello world"

print hello()
