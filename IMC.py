from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/mainpage')
def form():
    return render_template('IMC.html')
 
@app.route('/imc', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        result = request.form
        weight = float(result['Weight'])
        height = float(result['Height'])
        imc = weight / (height * height)
        result['IMC'] = imc
        return render_template('dati.html', result=result)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)