from flask import Flask, render_template


membership_app = Flask(__name__)

@membership_app.route("/")
def home():
    """Render index.html"""
    return render_template('index.html')

if __name__ == '__main__':
    membership_app.run(debug=True)
