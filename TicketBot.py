from flask import Flask, request,jsonify,make_response
from flask_assistant import Assistant
from flask_ngrok import run_with_ngrok
import dialogflow_v2

app = Flask(__name__)
run_with_ngrok(app)
assist = Assistant(app,project_id="apt-classes")
app.debug = True
@app.route('/')

def book_ticket():
    req = request.get_json(force=True)


    action = req.get('queryResult').get('action')
    if action == 'Name':
    #     fullfillmentText = 'A sample response from webhoon'

          return {'fulfillmentText': 'Okay now please tell me your fathers occupation',

            }
    if action == 'father-occupation':
    #     fullfillmentText = 'A sample response from webhoon'

          return {'fulfillmentText': 'Okay thankyou so much how can I help you ?',

            }




    if action == 'book_ticket':
    #     fullfillmentText = 'A sample response from webhoon'

          return {'fulfillmentText': 'Yeah sure please tell me your origin of flight.',

            }
    if action == 'origin':
          return{'fulfillmentText': 'Okay I got your origin now please tell me what will be your destination.'}

    if action == 'Destination':
          return{'fulfillmentText': 'Okay I got your data your ticket is booked'}

@app.route('/webhook',methods=['GET','POST'])

def webhook():
    return make_response(jsonify(book_ticket()))

if __name__ == '__main__':
    app.run()
