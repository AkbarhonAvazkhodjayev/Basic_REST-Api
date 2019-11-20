from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
	def get(self, name):
		item = next(filter(lambda x: x['name'] == name, items), None)
		return {'item': None}, 404

	def post(self, name):
		data = request.get_json() 
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item, 201


class ItemList(Resource):
	def get(self):
		return{"items":items}


api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')

app.run(debug=True)