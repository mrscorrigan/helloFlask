from flask import Flask, render_template

app = Flask(__name__)

countries = [{
    'Country' : 'Ireland',
    'Capital' : 'Dublin',
    'Population' : '4.5 million'},
    {'Country' : 'France',
     'Capital' : 'Paris',
     'Population' : '60 million'},
    {'Country' : 'England',
     'Capital' : 'London',
     'Population' : '65 million'
}]


@app.route('/')
def get_index():
    return render_template("index.html")

@app.route('/country')
def get_country():
    return render_template("index.html", data=countries)


if __name__ == '__main__':
    app.run()
