# Payloads

# Create Booking
# Update Booking
# Auth - Token

from dotenv import load_dotenv
import os


def payload_create_booking():
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_booking_with_invalid_data():
    payload = {
        "firstname": "Abc",
        "lastname": "Xyz",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
    }


def payload_update_booking():
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_token():
    load_dotenv()
    payload = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }
    return payload

def payload_create_token_with_invalid_data():
    payload = {
        "username": "abc",
        "password": "xyz"
    }
