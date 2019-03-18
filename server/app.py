from datetime import datetime
from flask import Flask, jsonify, request
import uuid
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

NOTES = [{
  "title": "Mumbai Hackathon",
  "id": uuid.uuid4().hex,
  "author": "Shivam Mishra",
  "created": datetime.now(),
  "note": {
  "type": "doc",
  "content": [
    {
      "type": "heading",
      "attrs": {
        "level": 1
      },
      "content": [
        {
          "type": "text",
          "text": "This is Mumbai Hackathon"
        }
      ]
    },
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "Mumbai Hackathon is Annual Open Source Hackathon organized by the ERPNext Foundation and Don Bosco Institute of Technology. Every year, we welcome students, developers and designers from across the country to create incredible open source projects at Mumbai's largest Open Source Hackathon."
        }
      ]
    },
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "Here's the "
        },
        {
          "type": "text",
          "marks": [
            {
              "type": "link",
              "attrs": {
                "href": "https://github.com/MumbaiHackathon"
              }
            }
          ],
          "text": "repositories"
        },
        {
          "type": "text",
          "text": " of the amazing projects built at Mumbai Hackathon."
        }
      ]
    },
    {
      "type": "heading",
      "attrs": {
        "level": 2
      },
      "content": [
        {
          "type": "text",
          "text": "Details for Mumbai Hackathon 2019"
        }
      ]
    },
    {
      "type": "bullet_list",
      "content": [
        {
          "type": "list_item",
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "Date: 16th & 17th March 2019"
                }
              ]
            }
          ]
        },
        {
          "type": "list_item",
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "Timings:"
                }
              ]
            },
            {
              "type": "bullet_list",
              "content": [
                {
                  "type": "list_item",
                  "content": [
                    {
                      "type": "paragraph",
                      "content": [
                        {
                          "type": "text",
                          "text": "9 AM - 6 PM on 16th March."
                        }
                      ]
                    }
                  ]
                },
                {
                  "type": "list_item",
                  "content": [
                    {
                      "type": "paragraph",
                      "content": [
                        {
                          "type": "text",
                          "text": "9 AM - 12 PM on 17th March."
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "type": "list_item",
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "Prize Amount: Rs. 50,000"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
},
{
  "title": "Some More Note",
  "id": uuid.uuid4().hex,
  "author": "Shivam Mishra",
  "created": datetime.now(),
  "note": {
  "type": "doc",
  "content": [
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "This is some text."
        }
      ]
    }
  ]
}}]

@app.route("/api/notes", methods=['GET', 'POST'])
def notes():
    response_object = {'status': 'success'}
    response_object['notes'] = NOTES
    return jsonify(response_object)

@app.route("/api/note/<note_id>", methods=['GET', 'POST'])
def single_note(note_id):
    response_object = {'status': 'success'}
    note = list(filter(lambda d: d['id'] == note_id, NOTES))
    response_object['note'] = note
    return jsonify(response_object)

@app.route("/api/ping", methods=['GET', 'POST'])
def ping():
    response_object = {'status': 'success'}
    response_object['message'] = "pong"
    return jsonify(response_object)

@app.route("/")
def index():
    return "Hello"

if __name__ == "__main__":
    app.run()