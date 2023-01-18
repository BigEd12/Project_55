from flask import Flask
import random

app = Flask(__name__)

generated_num = random.randint(0, 9)

@app.route('/')
def index():
    return "<center><h1>Guess a number between 0 and 9</h1>" \
           "<img src= 'https://media.giphy.com/media/5ZKrnu6JEOIak/giphy.gif'></center>"

@app.route('/<int:guess>')
def user_guess(guess):
    if generated_num == guess:
        return f"<center><h1>Well done!</h1>" \
               f"<img src= 'https://media.giphy.com/media/BYhoMtJMQsYVy/giphy.gif'></center>"
    elif guess < generated_num:
        return f"<center><h1>Your guess of {guess} is too low!</h1>" \
               "<img src= 'https://media.giphy.com/media/AckmGL4e1i7M4/giphy.gif'></center>"
    elif guess > generated_num:
        return f"<center><h1>Your guess of {guess} is too high!</h1>" \
               "<img src= 'https://media.giphy.com/media/AckmGL4e1i7M4/giphy.gif'></center>"



if __name__ == "__main__":
    app.run(debug=True)