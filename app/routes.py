from flask import render_template
from app import app
import os

basedir = os.path.abspath(os.path.dirname('data'))

attaque_page = '/pages/attaque.html'


@app.route('/')
@app.route('/index')
def index():
    urls = []
    title = 'Scam'
    urls_file = open(os.path.join(basedir, 'app/data/scam.txt'))
    urls_file_lines = urls_file.readlines()
    for line in urls_file_lines:
        urls.append(line.strip())

    return render_template('index.html', title=title, urls=urls)


@app.route('/phishing')
def phishing():
    title = 'Phising'
    urls = []
    urls_file = open(os.path.join(basedir, 'app/data/phishing.txt'))
    urls_file_lines = urls_file.readlines()
    for line in urls_file_lines:
        urls.append(line.strip())

    return render_template(attaque_page, title=title, urls=urls)


@app.route('/pharming')
def pharming():
    title = 'Pharming'
    urls = []
    urls_file = open(os.path.join(basedir, 'app/data/pharming.txt'))
    urls_file_lines = urls_file.readlines()
    for line in urls_file_lines:
        urls.append(line.strip())
    return render_template(attaque_page, title=title, urls=urls)


@app.route('/vishing')
def vishing():
    title = 'Vishing'
    urls = []
    urls_file = open(os.path.join(basedir, 'app/data/vishing.txt'))
    urls_file_lines = urls_file.readlines()
    for line in urls_file_lines:
        urls.append(line.strip())
    return render_template(attaque_page, title=title, urls=urls)


@app.route('/smishing')
def smishing():
    title = 'Smishing'
    urls = []
    urls_file = open(os.path.join(basedir, 'app/data/smishing.txt'))
    urls_file_lines = urls_file.readlines()
    for line in urls_file_lines:
        urls.append(line.strip())
    return render_template(attaque_page, title=title, urls=urls)
