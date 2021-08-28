# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:02:55 2021

@author: Pranav Viswanathan
"""

from flask import Flask, render_template
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

    @app.route('/game')
    @app.route('/gamepage')
    def game_page():
        return render_template('game.html')

    return app
app = create_app()