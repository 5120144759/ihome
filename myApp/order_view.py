from datetime import datetime

from flask import Blueprint, render_template, request, session, jsonify

from myApp.models import Order, House
from utils import status_code
from utils.func import is_login

order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('/booking/', methods=['get'])
@is_login
def booking():
    return render_template('booking.html')


@order_blueprint.route('/order/', methods=['post'])
@is_login
def order():
    order_dict = request.form
    house_id = order_dict.get('house_id')
    house = House.query.get(house_id)
    begin_data = datetime.strptime(order_dict.get('begin_data'), '%Y-%m-%d')
    end_data = datetime.strptime(order_dict.get('end_data'), '%Y-%m-%d')
    order = Order()
    order.user_id = session['user_id']
    order.house_id = house_id
    order.begin_date = begin_data
    order.end_date = end_data
    order.days = (end_data - begin_data).days + 1
    order.house_price = house.price
    order.amount = order.days * order.house_price
    order.add_update()
    return jsonify(code=status_code.SUCCESS)

@order_blueprint.route('/my_orders/', methods=['get'])
@is_login
def my_orders():
    orders = Order.query.filter(Order.user_id==session['user_id'])
    order_list = [order.to_dict() for order in orders]
    return jsonify(code=status_code.OK, order_list=order_list)

@order_blueprint.route('/orders/', methods=['get'])
@is_login
def orders():
    return render_template('orders.html')


@order_blueprint.route('/lorders/', methods=['get'])
@is_login
def lorders():
    return render_template('lorders.html')

@order_blueprint.route('/my_lorders/', methods=['get'])
def my_lorders():
    user_id = session['user_id']
    houses = House.query.filter(House.user_id==user_id)
    houses_id = [house.id for house in houses]
    orders = Order.query.filter(Order.house_id.in_(houses_id))
    order_list = [order.to_dict() for order in orders]
    return jsonify(code=status_code.OK, order_list = order_list)

@order_blueprint.route('/accept/', methods=['patch'])
@is_login
def accept():
    order_id = request.form.get('order_id')
    status = request.form.get('status')
    order = Order.query.get(order_id)
    order.status = status
    order.add_update()
    return jsonify(status_code.SUCCESS)

@order_blueprint.route('/fd/', methods=['get'])
@is_login
def fd():
    pass