from flask_restful import Resource, reqparse
from models import items, Item

class ItemResource(Resource):
    def get(self, item_id):
        item = items.get(item_id)
        if item:
            return item.to_dict(), 200
        return {'message': 'Item not found'}, 404

    def post(self, item_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='Name of the item')
        parser.add_argument('quantity', type=int, required=True, help='Quantity of the item')
        parser.add_argument('price', type=float, required=True, help='Price of the item')
        data = parser.parse_args()

        if item_id in items:
            return {'message': 'Item already exists'}, 400

        item = Item(item_id, data['name'], data['quantity'], data['price'])
        items[item_id] = item
        return item.to_dict(), 201

    def put(self, item_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='Name of the item')
        parser.add_argument('quantity', type=int, required=True, help='Quantity of the item')
        parser.add_argument('price', type=float, required=True, help='Price of the item')
        data = parser.parse_args()

        if item_id not in items:
            return {'message': 'Item not found'}, 404

        item = items[item_id]
        item.name = data['name']
        item.quantity = data['quantity']
        item.price = data['price']
        return item.to_dict(), 200

    def delete(self, item_id):
        if item_id in items:
            del items[item_id]
            return {'message': 'Item deleted'}, 200
        return {'message': 'Item not found'}, 404

class ItemListResource(Resource):
    def get(self):
        return [item.to_dict() for item in items.values()], 200
