import json
from flask import jsonify, request
from sqlalchemy import func, not_
from app import app
from app.models import swtable
from . import db  # Import the db object that is initialized in __init__.py

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route('/list')
def returnList():
    all_sw = swtable.query.order_by(swtable.elo.desc())
    sw_data = []
    for sw in all_sw:
        sw_data.append({
            "id": sw.id,
            "content": sw.content,
            "explanation": sw.explanation,
            "icon": sw.icon,
            "elo": sw.elo,
            "matchesplayed": sw.matchesplayed
        })
    return jsonify(sw_data)

@app.route('/match')
def match():
    results = ( swtable.query.order_by(swtable.matchesplayed.asc(), func.random()).limit(10).first())


    match1 = {"id":results.id, "content":results.content, "explanation":results.explanation, "icon":results.icon, "elo":results.elo, "matchesplayed":results.matchesplayed}
    match2 = findEloEnemy(match1['elo'], match1['id'])
    
    return jsonify([match1, match2])

def findEloEnemy(elo_of_1, id_of_1):
    results = swtable.query.order_by(func.abs(swtable.elo - elo_of_1).asc()).filter(swtable.id != id_of_1).limit(10)
    match2 = {"id":results[0].id, "content":results[0].content, "explanation":results[0].explanation, "icon":results[0].icon, "elo":results[0].elo, "matchesplayed":results[0].matchesplayed}
    return match2


@app.route('/processvote', methods=['POST'])
def processVote():
    data = request.get_json()
    id_of_winner = data['idOfWinner']
    id_of_loser = data['idOfLoser']
    winner = swtable.query.filter(swtable.id == id_of_winner).first()
    loser = swtable.query.filter(swtable.id == id_of_loser).first()

    elo_prediction_winner = 1/(1+10**((loser.elo-winner.elo)/400))
    elo_prediction_loser = 1/(1+10**((winner.elo-loser.elo)/400))


    new_elo_winner = winner.elo + (32*(1-elo_prediction_winner))
    new_elo_loser = loser.elo + 32*(0-elo_prediction_loser)

    
    winner.elo = new_elo_winner
    loser.elo = new_elo_loser
    winner.matchesplayed = winner.matchesplayed + 1
    loser.matchesplayed = loser.matchesplayed + 1
    
    db.session.commit()

    return jsonify({"message": "Votes processed!"})



@app.route('/addsw', methods=['POST'])
def addSprichwort():
    data = request.get_json()  # Parse JSON payload
    content = data['content']
    explanation = data['explanation']
    icon = data['icon']
    matchesplayed = data['matchesplayed']
    elo = data['elo']
    sw = swtable(content=content, explanation=explanation, icon=icon, matchesplayed=matchesplayed, elo=elo)
    db.session.add(sw)
    db.session.commit()
    return jsonify({"message": "Sprichwort added!"})

""" @app.route('/addsw', methods=['POST'])
def addSprichwort():
    content = request.form['content'] 
    explanation = request.form['explanation']
    icon = request.form['icon']
    matchesplayed = request.form['matchesplayed']
    elo = request.form['elo']
    sw = swtable(content=content, explanation=explanation, icon=icon, matchesplayed=matchesplayed, elo=elo)
    return jsonify({"message": "Sprichwort added!"}) """

""" @app.route('/addall')
def addAll():
    with open('sprichwort_liste_neu.json', 'r') as file:
        sprichworter = json.load(file)
    
    for i in sprichworter:
        addSprichwort(i['sprichwort'], i['erklaerung'], i['icon'], 0, 1200)
    return jsonify({"message": "All Sprichw\u00f6rter added!"}) """