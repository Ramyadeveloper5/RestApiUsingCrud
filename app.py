# Package Importing
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# App Creation
app = Flask(__name__)


# Check the file is Main Module or Not
if __name__ == '__main__':
    app.run(debug=True)