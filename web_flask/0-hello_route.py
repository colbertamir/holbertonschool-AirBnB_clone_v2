#!/usr/bin/python3
"""Starting up Flask & returning Hello HBNB!"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_there():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 (accessible from any IP) and port 5000
    app.run(host='0.0.0.0', port=5000)
