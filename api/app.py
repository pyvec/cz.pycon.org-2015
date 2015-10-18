from flask import Flask
from flask.ext.restful import Api

from resources.spaces import Spaces

pycon_app = Flask(__name__)
api = Api(pycon_app)


# resources
api.add_resource(Spaces, '/spaces', '/spaces/<int:space_id>')

if __name__ == '__main__':
    pycon_app.run(debug=True)
