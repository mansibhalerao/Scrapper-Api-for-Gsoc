import os
import time
from flask import Flask, flash, request, redirect, url_for, render_template, make_response,current_app,send_from_directory,session,escape
import re
from selenium import webdriver
import time
import bs4
import scrape4


UPLOAD_FOLDER = 'uploads'
###################################################################################################
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    x = int(time.time())
    filex = open("GDG.txt","r")
    k = filex.read()
    timstamp = x-int(k.split('<br>')[0])
    filex.close()
    print(timstamp)
    if(timstamp>43200):
        pass
        scrape4.GetList()
    return str(k)


##############################################################################
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#################################################################################
if __name__ == '__main__':
	app.run(debug=True)

