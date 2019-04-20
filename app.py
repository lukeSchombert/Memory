from bottle import route, run, template, static_file, get, post, request
from Tile import cards


@route('/static/index.html')
def server_static(filename):
    return static_file(filename, root="./static")


@get('/')
def index():
    return template('index.html', allCards=cards)


@get('/clickedCard')
def clickedCard():
    index = request.query.selectedButton
    index = int(index)
    cards[index].faceUp = True
    return template('index.html', allCards=cards)


run(host='localhost', port=8080, debug=True, reloader=True)


