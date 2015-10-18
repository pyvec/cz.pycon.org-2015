from flask.ext.restful import Resource, reqparse
from models.space_model import SpaceModel

space = SpaceModel()


class Spaces(Resource):
    def __get_args(self):
        parser = reqparse.RequestParser()
        parser.add_argument('space', type=str)
        parser.add_argument('description', type=str)
        args = parser.parse_args()
        return args

    def __format_space_response(self, response):
        return {
            "id": response.get('id'),
            "space": response.get('space'),
            "description": response.get('description'),
            "href": "/spaces/{}".format(response.get('id')),
            "upvote": {
                "href": "/spaces/upvote/{}".format(response.get('id')),
            }
        }

    def get(self):
        return map(self.__format_space_response, space.get_all_spaces())


    def post(self):
        args = self.__get_args()

        if not args.get('space') or not args.get('description'):
            return {'msg': 'Missing mandatory (space, description) fields.'}, 500

        return self.__format_space_response(space.add_space(args)), 201

    def put(self, space_id):
        args = self.__get_args()
        args['id'] = space_id

        if not args.get('space') or not args.get('description'):
            return {'msg': 'Missing mandatory (space, description) fields.'}, 500

        return self.__format_space_response(space.edit_space(args)), 201

    def delete(self, space_id):
        space.delete_space(space_id)
        return None, 204
