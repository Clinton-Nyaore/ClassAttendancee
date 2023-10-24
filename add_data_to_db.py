import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from connect import *

ref = db.reference('Students')

unit_code = "BICT 411"
course = "BICT"

data = {
    "Bernard-Kemboi":
        {
            "name": "Bernard Kemboi",
            "course": course,
            "starting_year": 2017,
            "total_attendance": 0,
            "unit_code": unit_code,
            "year": 4,
            "last_attendance_time": "2023-12-08 00:54:34"
        },
    "Branon-Kipngeno":
        {
            "name": "Branon Kipngeno",
            "major": course,
            "starting_year": 2020,
            "total_attendance": 0,
            "unit_code": unit_code,
            "year": 4,
            "last_attendance_time": "2023-12-08 00:54:34"
        },
    "Cosmas-Bett":
        {
            "name": "Cosmas Bett",
            "major": course,
            "starting_year": 2020,
            "total_attendance": 0,
            "unit_code": unit_code,
            "year": 4,
            "last_attendance_time": "2023-12-08 00:54:34"
        },
        "David-Gikonyo":
        {
            "name": "David Gikonyo",
            "major": course,
            "starting_year": 2020,
            "total_attendance": 0,
            "unit_code": unit_code,
            "year": 4,
            "last_attendance_time": "2023-12-08 00:54:34"
        },
        "Joyce-Gatura":
        {
            "name": "Joyce Gatura",
            "major": course,
            "starting_year": 2020,
            "total_attendance": 0,
            "unit_code": unit_code,
            "year": 4,
            "last_attendance_time": "2023-12-08 00:54:34"
        },
         "Josephat-Mwai":
        {
            "name": "Josephat Mwai",
            "major": course,
            "starting_year": 2019,
            "total_attendance": 0,
            "unit_code": unit_code,
            "year": 4,
            "last_attendance_time": "2023-12-08 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)