from flask import render_template, request, redirect, url_for, abort, flash
from . import main



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


   return render_template('speedtest.html')

@main.route('/speeedtest', methods=['GET', 'POST'])
def refresh():
   '''
   View function to refresh
   '''


   return render_template('refresh.html')
