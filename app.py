from flask import Flask
from flask import jsonify
import json
import numpy as np
import openai

openai.api_key = "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"
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
  return "Hello, World!"


@app.route('/slot/<test>')
def getslot(test):
    
    YOUR_PROMPT = test

    model_name = "davinci:ft-nagoya-institute-of-technology-2022-01-27-03-19-44"
    response = openai.Completion.create(
        model= model_name,
        prompt=YOUR_PROMPT,
        max_tokens = 200,
        stop = ["END"],
    )

    slot_extraction = response['choices'][0]['text']

    ###########################################################################################################
    stamp_extraction = slot_extraction[slot_extraction.find("stamp:") + 6:]
    whom_extraction = slot_extraction[slot_extraction.find("whom:") + 5:slot_extraction.find("\nstamp:")]
    target_extraction = slot_extraction[slot_extraction.find("target:") + 7:slot_extraction.find("\npolarity_term:")]
    polarityTerm_extraction = slot_extraction[slot_extraction.find("polarity_term:") + 14:slot_extraction.find("\naspect:")]
    aspect_extraction = slot_extraction[slot_extraction.find("aspect:") + 7:slot_extraction.find("\nexperiencer:")]
    experiencer_extraction = slot_extraction[slot_extraction.find("experiencer:") + 12:slot_extraction.find("\nwhen:")]
    when_extraction = slot_extraction[slot_extraction.find("when:") + 5:slot_extraction.find("\nwhere:")]
    where_extraction = slot_extraction[slot_extraction.find("where:") + 6:slot_extraction.find("\nwhom:")]

    info = {"target":target_extraction, "polarityTerm":polarityTerm_extraction, "aspect":aspect_extraction, 
            "experiencer":experiencer_extraction,  "when":when_extraction, "where":where_extraction, "whom":whom_extraction, "stamp":stamp_extraction}
    
    return jsonify(info)

@app.route('/polarity/<test>')
def getpolarity(test):
    
    YOUR_PROMPT = test

    model_name = "curie:ft-nagoya-institute-of-technology-2022-01-24-05-33-47"
    response = openai.Completion.create(
        model= model_name,
        prompt=YOUR_PROMPT,
        max_tokens = 200,
        stop = ["END"],
    )

    slot_extraction = response['choices'][0]['text']

    ###########################################################################################################
    polarity_extraction = slot_extraction[slot_extraction.find("polarity:") + 9:]
    
    info = {"polarity":polarity_extraction}
    return jsonify(info)

@app.route('/question/<test>')
def getquestion(test):
    
    YOUR_PROMPT = test

    model_name = "davinci:ft-nagoya-institute-of-technology-2022-01-28-17-22-21"
    response = openai.Completion.create(
        model= model_name,
        prompt=YOUR_PROMPT,
        max_tokens = 200,
        stop = ["END"],
    )
    slot_extraction = response['choices'][0]['text']

    ###########################################################################################################
    question_extraction = slot_extraction[slot_extraction.find("Bot:") + 4:]
    
    info = {"question":question_extraction}
    return jsonify(info)

@app.route('/aizuti/<test>')
def getaizuti(test):
    
    YOUR_PROMPT = test

    model_name = "davinci:ft-nagoya-institute-of-technology-2022-01-27-05-44-27"
    response = openai.Completion.create(
        model= model_name,
        prompt=YOUR_PROMPT,
        max_tokens = 200,
        stop = ["END"],
    )
    slot_extraction = response['choices'][0]['text']

    ###########################################################################################################
    question_extraction = slot_extraction[slot_extraction.find("Bot:") + 4:]
    
    info = {"aizuti":question_extraction}
    return jsonify(info)