# Leaf Logistics

A simple REST api for transposing matrices.

## Dependencies

- Python
- Pip
- Flask

## Setup

- clone repo
- python3 -m venv venv
- source venv/bin/activate
- pip3 install -r requirements.txt
- flask run

## Test API

`curl -d '[[1,2,3],[4,5,6],[7,8,9]] ' -H 'Content-Type: application/json' http://127.0.0.1:5000/`

![Demo](https://s3.gifyu.com/images/demo5f1f1cd826433648.gif)

## Run Tests

`pytest -rA`

![Demo](https://s9.gifyu.com/images/demoe96277f697214958.gif)

## Thoughts

I did see the following requirements in the email.

- Software engineering principles, e.g. SOLID
- Architectural principles, e.g. decoupling
- Computer science principles, e.g. complexity

However I was unsure on how to do this correctly given it was such a small project/only one API requested.

Would be more than happen to discuss how I'd do it in a bigger project if requested.
