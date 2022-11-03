from flask import Flask, render_template
# instantiating the class ,get the value name of pythong project
app = Flask(__name__)


@app.route('/')  # decorator
def home():
    # this func will be mapped to url '/' above, if you want you can change the url
    return render_template("home.html")


@app.route('/about/')  # decorator
def about():
    # this func will be mapped to url '/' above, if you want you can change the url
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
