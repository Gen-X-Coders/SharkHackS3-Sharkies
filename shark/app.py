# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:02:55 2021

@author: Pranav Viswanathan
"""
from flask import Flask, render_template, request
import pickle
import numpy as np

def format_data(data):
    # Country Activity Age Sex_F Sex_M Time_Afternoon Time_Evening Time_Morning Time_Night

    country_encoding = {'USA' : 0.04010025,'BRAZIL': 0.36,'AUSTRALIA': 0.27272727, 'SOUTH AFRICA': 0.20465116, 'BAHAMAS' : 0.07692308, 'MEXICO' :0.49999999, 
        'REUNION' : 0.46153846,'EGYPT' :  0.24990115,'NEW ZEALAND' :  0.18749999,'NEW CALEDONIA' :  0.3999681 , 'MOZAMBIQUE' : 0.18181635,
        'FIJI' : 0.29998044,'PAPUA NEW GUINEA':  0.49995576}

    activity_encoding = {'Standing':0.08474576, 'Surfing':0.05641026, 'Swimming': 0.27574751, 'Walking': 0.07692347, 'Wading':0.07142857,
        'Spearfishing': 0.15740741, 'Snorkeling': 0.19565217, 'Fishing': 0.02272727, 'Kayaking': 0.2826087 ,
        'Body boarding': 0.10000512 , 'Free diving': 0.05, 'Boogie boarding': 0.26666656, 'Diving': 0.16216216,
        'Body surfing': 0.27272132, 'Windsurfing': 0.0833343, 'Boogie Boarding': 0.3 , 'Scuba diving': 0.23076923,
        'Treading water': 0.55, 'Bathing': 0.14149755}
    
    country = country_encoding[data[2]]
    activity= activity_encoding[data[6]]
    X = [country, activity, int(data[1]), 0, 1]
    # if( data[3] == 'M' ):
    #     X.append([0, 1])
    # else:
    #     X.append([1, 0])
    
    if( data[5] == 'Afternoon' ):
        X.append([1, 0, 0, 0])
    elif( data[5] == 'Evening' ):
        X.append([0, 1, 0, 0])
    elif( data[5] == 'Morning' ):
        X.append([0, 0, 1, 0])
    else:
        X.append([0, 0, 0, 1])

    X = np.array(X)
    
    return X

def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/home')
    def welcome_page():
        return render_template('main.html')

    @app.route('/about')
    def about_page():
        return render_template('about.html')
   

    @app.route('/inf')
    @app.route('/infomation')
    def devinf_page():
        return render_template('devinf.html')

    @app.route('/game_page', methods=['GET' , 'POST'])
    def game_page():
        if request.method == 'POST':
            #getting input:
            name = request.form.get('name')
            age = request.form.get('age')
            location = request.form.get('location')
            location_inner = request.form.get('location_inner')
            beach = request.form.get('beach')
            time = request.form.get('time')
            activity = request.form.get('activity')

            data = [name, age, location, location_inner, beach, time, activity]
            print(data)
            pickle_in = open("classifierShark.pickle", "rb")
            classifier = pickle.load(pickle_in)
            pickle_in.close()
            #data = session.get("data",None)
            #X = format_data(data)
            #print(X)
            #prediction = classifier.fit(X)
            prediction = 1
            return render_template('mlmodel.html', data=prediction)
            
        return render_template('game.html')

    @app.route('/mlmodel_page')
    def mlmodel_page():
        pickle_in = open("classifierShark.pickle", "rb")
        classifier = pickle.load(pickle_in)
        pickle_in.close()
        #data = session.get("data",None)
        #X = format_data(data)
        #print(X)
        #prediction = classifier.fit(X)
        prediction = 1
        return render_template('mlmodel.html')

    return app
app = create_app()