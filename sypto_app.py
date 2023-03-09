from flask import Flask, render_template, jsonify

app = Flask(__name__)

"""
BOTS = [
  {
  id: 1,
  title: "Athena Top 5"},
  {
  id: 1,
  title: "Athena Top 10"},
  {
  id: 1,
  title: "Athena Custom"}
]
# flask templating syntax for dynamic data 
"""
@app.route("/")
def Hello_world():
  return render_template('home.html')
  #return render_template('home.html', bots = BOTS)

@app.route("/api/current_price")
def trade_history(coin):
  pass


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)