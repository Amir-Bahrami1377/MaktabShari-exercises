from models import User
from flask import redirect, url_for, request, render_template, escape, render_template_string


def index():
    return render_template("index.html")
