from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])
@cross_origin(origins="*")
def query():
    data = request.get_json()
    query = data['query']

    # Use langchain to process the query and retrieve the notes
    # result = langchain.process(query)

    # For now, just return the query as the result
    result = query

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)