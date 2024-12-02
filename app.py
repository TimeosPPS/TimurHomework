from flask import Flask, render_template
from app.routes import app, admin
from app.db.models import base

if __name__ == '__main__':
    app.run(port=5000, debug=True)
