from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('IMC_fetch.html')
 
@app.route('/imc_fetch', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        result = request.get_json()
        weight = result['Weight']
        height = result['Height']
        imc = weight / (height * height)
        return jsonify(imc)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)