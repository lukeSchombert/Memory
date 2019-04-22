from bottle import route, run, template, static_file, get, post, request
from Tile import tiles



@route('/static/index.html')
def server_static(filename):
    return static_file(filename, root="./static")


@get('/')
def index():
    return template('index.html', allTiles=tiles)


@get('/clickedTile')
def clickedTile():
    index = request.query.selectedButton
    index = int(index)
    tiles[index].faceUp = True
    return template('index.html', allTiles=tiles)


run(host='localhost', port=8080, debug=True, reloader=True)
