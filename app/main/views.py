from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from datetime import datetime, timezone


@main.route('/')
def index():
    '''
    View root page function that returns the index page
    '''
    title = 'Home'
    return render_template('index.html', title=title)


@main.route('/speedtest', methods=['GET', 'POST'])
def speedtest():
    '''
    View function to speedtest
    '''
    title = "Test Your Speed"
    return render_template('speedtest.html',title=title)
