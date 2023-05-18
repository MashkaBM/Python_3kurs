from flask import (
    Flask,
    render_template
)


app = Flask(__name__)

@app.route("/site")
def site():
    return render_template('business_card.html')

@app.route("/")
@app.route("/Mariia")
def Mariia():
    return render_template('Mariia.html')




if __name__ == "__main__":
    app.run(debug=True)