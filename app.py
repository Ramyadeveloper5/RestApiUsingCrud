# Package Importing
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# App Creation
app = Flask(__name__)

# Route: Home Page
@app.route('/')
def home():
    return jsonify({
        'Name': "Ramya",
        'Role': "Developer"
    })

# Database Configuration
BASEDIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Object Creation for SQLAlchemy and Marshmallow
database = SQLAlchemy(app)
marshmallow = Marshmallow(app)

# User Model
class UserModel(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(100))
    email = database.Column(database.String(100))
    mobile = database.Column(database.String(100))

    def __init__(self, username, email, mobile):
        self.username = username
        self.email = email
        self.mobile = mobile

# Schema Creation
class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'mobile')

# Single User Schema
single_user_schema = UserSchema()
# Many Users Schema
multi_user_schema = UserSchema(many=True)

# Creating tables within the application context
with app.app_context():
    database.create_all()


# User Creation : Create Method

@app.route('/usercreate',methods=['POST'])
def userCreation():
    username = request.json['username']
    email = request.json['email']
    mobile = request.json['mobile']
    # User Creation
    user_create = UserModel(username,email,mobile)
    # Session Add
    database.session.add(user_create)
    # Session Commit
    database.session.commit()
    return single_user_schema.jsonify(user_create)

# User Get : Read Method








# Check if the file is the main module
if __name__ == '__main__':
    app.run(debug=True)
