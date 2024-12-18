from flask import Flask, render_template, request
import os

app = Flask(__name__)
# Define the route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Run the application on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5002)
