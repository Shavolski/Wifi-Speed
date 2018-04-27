from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from datetime import datetime, timezone
import pyspeedtest

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
    st = pyspeedtest.SpeedTest()
    ping = st.ping()
    downloaded = st.download()
    upload = st.upload()

    return render_template('speedtest.html', ping=ping, downloaded=downloaded, upload=upload)
@main.route('/refresh',methods=['GET', 'POST'])
def refresh():
    return render_template('refresh.html')