#!/usr/bin/env python

__author__ = 'Mauricio w/ help watching ERICAWENTWEST www.youtube.com'

import requests
import turtle
from time import ctime


def api_data():
    astro_req = requests.get('http://api.open-notify.org/astros.json')
    astro_data = astro_req.json()
    people = astro_data["people"]

    print('There are currently {} people in space.'.format(
        str(astro_data["number"])))
    for person in people:
        print('{} is on board {}.'.format(person["name"], person["craft"]))


def location_data():
    req = requests.get('http://api.open-notify.org/iss-now.json')
    location_data = req.json()
    location = location_data['iss_position']
    lat = location['latitude']
    long = location['longitude']
    return (float(lat), float(long))


def turtle_iss():
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')

    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(45)
    iss.penup()
    (lat, long) = location_data()
    iss.goto(long, lat)
    indy_loc()
    screen.exitonclick()


def indy_loc():
    turtle.Turtle()
    turtle.color('yellow')
    turtle.shape('circle')
    turtle.shapesize(0.5, 0.5)
    turtle.penup()
    turtle.goto(-86.1, 39.8)
    passovers = find_passover_times()
    next_passover = ctime(passovers[0]['risetime'])
    turtle.write(next_passover)


def find_passover_times():
    passing = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=39.8&lon=86.1")
    passing_data = passing.json()
    return passing_data['response']


def main():
    api_data()
    location_data()
    turtle_iss()
    find_passover_times()


if __name__ == '__main__':
    main()
