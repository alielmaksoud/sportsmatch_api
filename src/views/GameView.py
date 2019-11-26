from flask import request, g, Blueprint, json, Response
# from ..shared.Authentication import Auth
from ..models.GameModel import GameModel, GameSchema

game_api = Blueprint('game_api', __name__)
game_schema = GameSchema()

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

@game_api.route('/<int:game_id>', methods=['GET'])
def get_one(game_id):
  """
  Get A Blogpost
  """
  game = GameModel.get_one_game(game_id)
  if not game:
    return custom_response({'error': 'game not found'}, 404)
  data = game_schema.dump(game)
  return custom_response(data, 200)

@game_api.route('/', methods=['GET'])
def get_all():
  game = GameModel.get_all_games()
  data = game_schema.dump(game, many=True)
  return custom_response(data, 200)



@game_api.route('/', methods=['POST'])
def create():
  """
  Create Blogpost Function
  """
  req_data = request.get_json()
  data = game_schema.load(req_data)
  game = GameModel(data)
  game.save()
  data = game_schema.dump(game)
  return custom_response(data, 201)
