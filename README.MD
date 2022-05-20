# Fridge face backend

A digital shopping cart mobile application for the company [Applifting](https://www.applifting.cz/). </br>
Bachelor thesis of Xuan Anh Nguyen, [CVUT FEL SIT](https://sit.fel.cvut.cz/) year 2022. <br/>

This project aims to improve the food and drink purchase experience in a company for its employees, using [Flask](https://flask.palletsprojects.com/en/2.1.x/) with [Tensorflow](https://www.tensorflow.org/).

## Resources

- **Frontent source code**: <br/>
  https://github.com/alexnguyen98/fridge-face-frontend
- **Keras FaceNet model**: <br/>
  https://github.com/nyoki-mtl/keras-facenet

## Getting Started

### Project structure

```sh
fridge-face-backend/
  └── app/
      ├── db/
           └── __init__py.py        # DB service representation
      ├── services/
      ├── __init__.py
      └── api.py                    # API Controller
  └── model/
      └── facenet_keras.h5.         # Keras FaceNet model
```

### Requirements

- Python 3.7.2
- pip3

### Usage

```bash
# Set development mode (FLASK_ENV=development/production)
nano .env

# Activate python venv
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Running dev mode
python3 run.py

# Running prod mode
gunicorn run:app -b 0.0.0.0:3000
```

## Notice

This app was created for the company Applifting, so without the access to the internal system you cannot fully test the functionality. Nevertheless you can host the backend locally and configure it to your own API that can mock the Products and Users entities.

## Contribution

In case you decide to contribute to this project, we will be very happy and we appreciate your help. Feel free to:

1. Check out [issues](https://github.com/alexnguyen98/fridge-face-backend/issues).
2. Create a new branch from `master` where work will be done
3. After work is done please create new pull request into `master`
4. Wait for review and PR approval (PR should be approved)
5. After merge work is DONE! Thank you! :heart:

If you have any questions about development or issue description, feel free to ask the author of the issue in comments.
