from api import User
from flask import Flask
from flask_restful import Api, Resource, reqparse
import commands

app = Flask(__name__)
api = Api(app)
api.add_resource(User, "/users", "/users/", "/users/<int:id>")

# def run():
    
#     while True:
#         command = input("Choose a command to run:\n")
#         if not command:
#             break
            
#         if command not in commands:
#             print("I do not recognize this command.")
#             continue
            
#         commands[command]()
        

if __name__ == "__main__":
#     run()
    app.run(host='0.0.0.0', port=80, debug=True)

