#scrivere una pagina html/flask che visualizzi l'elenco delle regioni in un menù a tendina

#inizio esercizio
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')
    tabella = df['denominazione_regione'].drop_duplicates()
    return render_template('es_search.html', regioni = tabella)

@app.route('/es_search', methods = ['GET'])
def search():
    import pandas as pd
    regione = request.args['regione']
    dati_regioni = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')
    risultato = dati_regioni[dati_regioni['denominazione_regione']==regione.capitalize()].index
    if len(risultato) == 0:
        table = 'Regione non trovata'
    else:
        table = list(risultato)
    return render_template('es_radiobutton.html', tabella = table)

@app.route('/es_info', methods = ['GET'])
def info():
    import pandas as pd
    dati_regioni = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')
    id = int(request.args['id'])
    risultato = dati_regioni.iloc[[id]]
    if len(risultato) == 0:
        table = 'Regione non trovata'
    else:
        table = risultato.to_html()
    return render_template('tabella.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)