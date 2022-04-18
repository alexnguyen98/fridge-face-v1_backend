import os
import pickle # storing a python object into a serialized file
import numpy

users = ['ALN', 'KAJ', 'KOP', 'TEO', 'TRP', 'ROV', 'OMO', 'RAW', "DVO", "TON", "FKI", "DAF", "JPO", "RAF", "JAM", "VEK", "KNL", "JZE", "PRS", "ADH", "MAH", "PJC", "PEC", "ARY"]
threshold = 7;

def get_filename():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(base_dir, 'db', "user_db.pkl")
    return filename

def user_exist(user):
    return user in users

def registered_exist(user):
    db = get_db()
    return user in db

def get_db():
    global database # singleton model
    filename = get_filename()
    if (not 'database' in globals()):
        if (not os.path.isfile(filename)): 
            return {}
        try:
            print("* Loading DB...")
            file = open(filename, "rb")
            database = pickle.load(file)
            file.close()
            print("* DB loaded")
        except Exception as e:
            print(e)
    return database

def save_db(embedding, user):
    db = get_db()
    db[user] = embedding

    filename = get_filename()
    file = open(filename, "wb")
    pickle.dump(db, file)
    file.close()

    print("* User saved")

def find_user(embedding):
    db = get_db()
    min_dist = threshold
    user_id = "No user found"
    for key, value in db.items():
        dist = numpy.linalg.norm(value - embedding)
        if (dist < threshold):
            min_dist = min_dist
            user_id = str(key)
    return user_id

def get_avaiable_users():
    db = get_db()

    arr = []
    for i in users:
        if (i not in db):
            arr.append(i)
    
    return arr