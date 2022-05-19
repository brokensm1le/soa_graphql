import graphene
import json

import model

class scoreboardType(graphene.ObjectType):
    who_win=graphene.String()

    def resolve_who_win(sroreboard, info):
        return sroreboard.who_win


class GameType(graphene.ObjectType):
    id=graphene.Int()
    scoreboard=graphene.Field(scoreboardType)
    status=graphene.String()
    comments=graphene.String()

    def resolve_id(Game, info):
        return Game.id

    def resolve_scoreboard(Game, info):
        return Game.scoreboard

    def resolve_status(Game, info):
        return Game.status

    def resolve_comments(Game, info):
        return Game.comments


class Query(graphene.ObjectType):
    all_games = graphene.List(GameType)
    game = graphene.Field(GameType, key=graphene.Int())

    def resolve_all_games(root, info):
        return model.data.values()

    def resolve_game(root, info, key):
        return model.data[key]



# schema = graphene.Schema(query=Query, mutation=Mutations)
# result = schema.execute(
#     '''
#     mutation {
#         mutateGame(id:1, comments:"cool game") {
#             game {
#                 id
#             }
#         }
#     }
#     '''
# )
# print(result)
# items = dict(result.data.items())
# print(json.dumps(items, indent=4))
