from flask import Flask, request
import os

import parser

app = Flask(__name__)


@app.route("/parse-ingredients", methods=['POST'])
def parse_ingredients():
    data = request.json
    ingredients = data['ingredients']
    return parser.parse(ingredients)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
