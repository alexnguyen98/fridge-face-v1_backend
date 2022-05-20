from app import app
import os
import pickle # storing a python object into a serialized file
import numpy

threshold = 7

def get_filename():
    filename = os.path.join(app.root_path, "db/user_db.pkl")
    return filename

class DB():
    db = {}

    def __init__(self):
        filename = get_filename()
        if (os.path.isfile(filename)):
            try:
                print("* Loading DB...")
                file = open(filename, "rb")
                self.db = pickle.load(file)
                file.close()
                print("* DB loaded")
            except Exception as e:
                print(e)

    def registered_exist(self, user):
        return user in self.db

    def save_db(self, embedding, user):
        self.db[user] = embedding

        filename = get_filename()
        file = open(filename, "wb")
        pickle.dump(self.db, file)
        file.close()

        print("* User saved")

    def find_user(self, embedding):
        min_dist = threshold
        user_id = ""
        for key, value in self.db.items():
            dist = numpy.linalg.norm(value - embedding)
            print("* dist: " + str(dist))
            if (dist < threshold):
                min_dist = min_dist
                user_id = str(key)

        return user_id

    # NOTICE: For testing!
    def reset_db(self):
        self.db = {}

        filename = get_filename()
        file = open(filename, "wb")
        pickle.dump(self.db, file)
        file.close()

        print("* DB reseted")
