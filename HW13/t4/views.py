from flask import redirect, url_for, request, render_template, escape, render_template_string


def index():
    return render_template("index.html")


def login():
    return render_template("login.html")


def sign_up():
    return render_template("sign-up.html")
