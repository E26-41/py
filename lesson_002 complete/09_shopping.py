#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tokenize import cookie_re

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99},
    ],
    'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99},
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ]
}
# Указать надо только по 2 магазина с минимальными ценами

cookie = sweets['печенье']
cost = shops[cookie[0]['shop']][0]
print(cookie[0]['shop'],cost['name'], cost['price'])

cost = shops[cookie[1]['shop']][0]
print(cookie[1]['shop'],cost['name'], cost['price'], '\n')


candy = sweets['конфеты']
cost = shops[candy[1]['shop']][1]
print(candy[1]['shop'],cost['name'], cost['price'])

cost = shops[candy[2]['shop']][1]
print(candy[2]['shop'],cost['name'], cost['price'],'\n')


caramel = sweets['карамель']
cost = shops[caramel[0]['shop']][2]
print(caramel[0]['shop'], cost['name'], cost['price'])

caramel = sweets['карамель']
cost = shops[caramel[2]['shop']][2]
print(caramel[2]['shop'], cost['name'], cost['price'],'\n')


cake = sweets['пирожное']
cost = shops[cake[1]['shop']][3]
print(cake[1]['shop'], cost['name'], cost['price'])

cake = sweets['пирожное']
cost = shops[cake[2]['shop']][3]
print(cake[2]['shop'], cost['name'], cost['price'])
