import flask
from flask import request, jsonify
from flask_restful import Resource, Api

app = flask.Flask(__name__)
api = Api(app)

class IntroToWebsite(Resource):
    def get(self):
        return "<h1>Time to Match your Car</h1>    <p>This site is a prototype API.</p>"
class CarSelection(Resource):
    def get(self):
        return "<h1>Pick your car from the drop down list</h1>"
# @app.route('/', methods=['GET'])
# def drop_down_list():
#     return "{% for each in listStatus %} <option value="{{each}}" {% if each == "list_status" %} selected {% endif %}>{{each}}</option> {% endfor %}"
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

api.add_resource(IntroToWebsite,'/')
api.add_resource(CarSelection,'/car_matching')

if __name__ == "__main__":
    app.run(debug=True)


# # A route to return all of the available entries in our catalog.
# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)

# {
#   "embeddings": [
#     {
#       "tensorName": "Car Nodes",
#       "tensorShape": [
#         1000,
#         50
#       ],
#       "tensorPath": "https://raw.githubusercontent.com/.../tensors.tsv",
#       "metadataPath": "https://raw.githubusercontent.com/.../optional.metadata.tsv"
#     }
#   ]
# }
