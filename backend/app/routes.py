from flask import jsonify, request
from . import app, db
from .models import CodeAnalysis, NLPFeedback

@app.route("/code-analysis", methods=["POST"])
def code_analysis():
    code = request.get_json()["code"]
    analysis = CodeAnalysis(code)
    db.session.add(analysis)
    db.session.commit()
    return jsonify({"message": "Code analysis completed"})

@app.route("/nlp-feedback", methods=["POST"])
def nlp_feedback():
    code = request.get_json()["code"]
    feedback = NLPFeedback(code)
    db.session.add(feedback)
    db.session.commit()
    return jsonify({"message": "NLP feedback generated"})
