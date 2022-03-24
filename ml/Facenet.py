from keras.models import load_model

def get_model():
    global model # singleton model
    if (not 'model' in globals()):
        # try:
        print("* Loading model...")
        model = load_model('./ml/facenet_keras.h5')
        print("* Model loaded")
        # except Exception as e:
        #     # print(e)

# import os.path

# file_name = "./ml/facenet_keras.h5"

# try:
#     my_file = open(file_name)
#     print("file exists")
# except IOError:
#     print("file doesnt exist")

# print("neco")