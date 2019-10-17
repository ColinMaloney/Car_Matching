import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Time to Match your Car</h1>    <p>This site is a prototype API.</p>"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(debug=True)


# # A route to return all of the available entries in our catalog.
# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)

# {
#   "embeddings": [
#     {
#       "tensorName": "My tensor",
#       "tensorShape": [
#         1000,
#         50
#       ],
#       "tensorPath": "https://raw.githubusercontent.com/.../tensors.tsv",
#       "metadataPath": "https://raw.githubusercontent.com/.../optional.metadata.tsv"
#     }
#   ]
# }
