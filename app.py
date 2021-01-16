from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # Rerpites to original website if /____ doesnt exist
def index():
    return render_template("website.html")
    
if __name__ == "__main__":
    app.run(debug=True, host="localhost")


