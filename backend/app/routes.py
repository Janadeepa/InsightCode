from flask import Blueprint, jsonify, request
from .models.code_analysis import analyze_code
from .models.nlp_feedback import generate_feedback

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/analyze', methods=['POST'])
def analyze():
    code = request.json.get('code')
    analysis_result = analyze_code(code)
    feedback = generate_feedback(code)
    return jsonify({
        'analysis': analysis_result,
        'feedback': feedback
    })

@main_blueprint.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})
