import json

def choice (data):
    health = data["snakes"]["data"][0]["health"]
    
    if health > 45:
        # chase your own fucking tail
        direction = "up" # make this it's astar tail
    else:
        # locate food!!!!!
        direction = "up" # make the direction right

    return direction

# this is all for testing
if __name__=="__main__":
    with open('move.json') as json_data:
        d = json.load(json_data)
        choice(d)
