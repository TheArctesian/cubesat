from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def get(self):
        return {
                "some data" : "0x00000"
        }

api.add_resource(Data, '/')

if __name__ == '__main__':
    app.run(debug=True)
