# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:02:55 2021

@author: Pranav Viswanathan
"""

from flask import Flask, render_template, request
import pickle

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

    @app.route('/game', methods=['GET', 'POST'])
    def game_page():
        if request.method == 'POST':
            #getting input:
            name = request.form.get('name')
            age = request.form.get('age')
            location = request.form.get('location')
            location_inner = request.form.get('location_inner')
            beach = request.form.get('beach')
            owl = request.form.get('owl')
            bird = request.form.get('bird')
            recoveryMethod = request.form.get('recoveryMethod')
            pickle_in = open("classiferShark.pickle", "rb")
            classifier = pickle.load(pickle_in)
            pickle_in.close()
            prediction = classifier.fit()
        return render_template('game.html')

    @app.route('/mlmodel')
    @app.route('/mlmodelpage')
    def mlmodel_page():
        pickle_in = open("classiferShark.pickle", "rb")
        classifier = pickle.load(pickle_in)
        pickle_in.close()
        prediction = classifier.fit()
        return render_template('mlmodel.html')

    return app
app = create_app()