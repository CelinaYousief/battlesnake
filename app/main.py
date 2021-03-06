import bottle
import os
import random
import snakechoice
import parsesnakes
import parsefood
import astar
import gametocode

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

    head_url = '%s://%s/static/mariah.jpg' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#FFAE00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'Mariah Scarey',
        'head_type': 'tongue',
        'tail_type': 'fat-rattle'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    board_width = data.get('width')
    board_height = data.get('height')
    snakes = parsesnakes.parsesnakes(data)
    #print(snakes)
    omnom = parsefood.parsefood(data)
    #print(omnom)
    board,goal,head = gametocode.tonumpy(snakes,omnom,board_width,board_height)
    #print(board)
    #print(goal)
    #print(head)
    direction = astar.astar(board,head,goal)
    print(direction)

    # up, down, left, right
    #directions = ['up', 'down', 'left', 'right']
    #direction = random.choice(directions)
    return {
        'move': direction,
        'taunt': 'All I want for Christmas is your snake'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)
