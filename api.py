from flask import Flask, request, render_template, flash, redirect, url_for
import requests
from flask_restful import reqparse, Resource, Api
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from alerts import sendAlert

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
api = Api(app)

dataParser = reqparse.RequestParser()
dataParser.add_argument('timestamp')
dataParser.add_argument('CO')

data = {"timestamp":"02-22-2020 08:38", "CO":"100"}

# format of contactInfo list is a list of dictionaries
# [{"firstName":"Griffin", "lastName":"Jeanette", "emailAddress": "jeanet_g1@denison.edu",
#   "phoneNum":"1630-362-8142"}]
contactInfo = []

threshold = 100

class Data(Resource):
    def get(self, data_id):
        return data[data_id]

    def put(self, data_id):
        args = dataParser.parse_args()
        reading = args[data_id]
        data[data_id] = reading

        print(reading)

        if int(reading) > threshold:
            sendAlert(contactInfo)

        return data, 201

class ContactInfoForm(FlaskForm):
    firstName = StringField("First Name", validators=[DataRequired()])
    lastName = StringField("Last Name", validators=[DataRequired()])
    emailAddress = StringField("Email Address", validators=[DataRequired()])
    phoneNum = StringField("Phone Number (XXXX-XXX-XXXX)", validators=[DataRequired()])
    submitField = SubmitField("Submit")

@app.route("/")
def displayLevel():
    time = data["timestamp"]
    COLevel = data["CO"]

    return render_template("index.html", timestamp=time, colevel=COLevel)

@app.route("/subscribe", methods=['GET', 'POST'])
def contactInfoPage():
    form = ContactInfoForm(request.form)

    print("HEREEE")

    if request.method == 'POST':
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        emailAddress = request.form["emailAddress"]
        phoneNum = request.form["phoneNum"]

        newEntry = {}
        newEntry["firstName"] = firstName
        newEntry["lastName"] = lastName
        newEntry["emailAddress"] = emailAddress
        newEntry["phoneNum"] = phoneNum

        contactInfo.append(newEntry)

        print("name: " + firstName + " " + lastName)
        print("email: " + emailAddress)
        print("phoneNum: " + phoneNum)

        return redirect(url_for('contactInfoPage'))

    return render_template("subscribe.html", form=form)

api.add_resource(Data, "/data/<data_id>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
