from flask_restful import Api, Resource, reqparse
import random

users = [
    {
        "id": 0,
        "author": "Kevin Kelly",
        "user": "The business plans of the next 10,000 startups are easy to forecast: " +
                 "Take X and add AI." 
    },
    {
        "id": 1,
        "author": "Stephen Hawking",
        "user": "The development of full artificial intelligence could " +
                 "spell the end of the human race…. " +
                 "It would take off on its own, and re-design " +
                 "itself at an ever increasing rate. " +
                 "Humans, who are limited by slow biological evolution, " + 
                 "couldn't compete, and would be superseded."
    },
    {
        "id": 2,
        "author": "Claude Shannon",
        "user": "I visualize a time when we will be to robots what " +
                 "dogs are to humans, " + 
                 "and I’m rooting for the machines."
    }
]

class User(Resource):

	def get(self, id=0):
		"""
		Return a user based on the given id. 

			If such user does not exist, return a 404 Status Code. 
			If no `id` given, return a user randomly.
		"""
		if id == 0:
			return random.choice(users), 200

		for user in users:
			if(user["id"] == id):
				return user, 200
		
		return "User not found", 404


	def post(self, id):
		"""
		Takes a new user `id` as the input, and parses the parameters that will
		go to the body of the request (e.g., name or products) using `regparse`.
		Finally, store this user in the database.

			If a user with given `id` exists, return a 400 Status Code.

			If a user with given `id` has not yet been created, do it and returns 
			this new record along with a 201 Status Code.
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("author")
		parser.add_argument("user")
		params = parser.parse_args()

		for user in users:
			if(id == user["id"]):
				return f"user with id {id} already exists", 400

		user = {
			"id": int(id),
			"author": params["author"],
			"user": params["user"]
		}

		users.append(user)
		return user, 201


	def put(self, id):
		"""
		Takes an `id` as input and parses the user parameters using `regparse`.

			If a user with the specified id exists, update with the parsed parameters and 
			return along with a 200 Status Code.

			If there is no user with the specified `id` yet, create a new record and return
			it along with a 201 Status Code.
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("author")
		parser.add_argument("user")
		params = parser.parse_args()
		for user in users:
			if(id == user["id"]):
				user["author"] = params["author"]
				user["user"] = params["user"]
				return user, 200

		user = {
			"id": id,
			"author": params["author"],
			"user": params["user"]
		}

		users.append(user)
		return user, 201


	def delete(self, id):
		"""
		Take a user `id` as input and updates the database via global 
		scope using list comprehension.
		"""
		global users
		users = [u for u in users if u["id"] != id]
		return f"user with id {id} is deleted.", 200