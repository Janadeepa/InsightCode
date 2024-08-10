from flask import Blueprint, request, jsonify
from app import app, db
from app.models import CodeAnalysis, NLPFeedback

routes_blueprint = Blueprint("routes", __name__)

@routes_blueprint.route("/code_analysis", methods=["POST"])
def code_analysis():
    code = request.get_json()["code"]
    analysis = CodeAnalysis(code)
    result = analysis.run()
    return jsonify({"result": result})

@routes_blueprint.route("/nlp_feedback", methods=["POST"])
def nlp_feedback():
    code = request.get_json()["code"]
    feedback = NLPFeedback(code)
    result = feedback.generate()
    return jsonify({"result": result})

app.register_blueprint(routes_blueprint)
