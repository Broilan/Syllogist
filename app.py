from flask import Flask, request, jsonify
from nlp.analyzer import analyze_syllogism

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_syllogism_route():
    data = request.get_json()
    statement = data.get('statement', '')
    
    if not statement:
        return jsonify({'error': 'No statement provided'}), 400
    
    result = analyze_syllogism(statement)
    
    if 'error' in result:
        return jsonify(result), 400
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)


