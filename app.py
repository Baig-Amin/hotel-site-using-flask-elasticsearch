from flask import Flask, render_template, url_for, Markup
from elasticsearch import Elasticsearch
from data import *
from staticData import *

app = Flask(__name__)
es = Elasticsearch()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/hotel/')
def category():
    return render_template('category.html', allHotelImages=allHotelImages)


@app.route('/hotel/<int:id>')
def hotel(id):
    receiveId = id
    # Get Data By Id
    res = es.get(index='hotel', id=receiveId)
    hotelDataById = res['_source']
    # Query for data Except given id
    res = es.search(index="hotel",
                    query={"bool": {
                        "must_not": {
                            "term": {"_id": receiveId}
                        }
                    }
                    })
    # Query Result
    hits = res['hits']['hits']

    return render_template('index.html', allHotelImages=allHotelImages, hotelDataById=hotelDataById, hits=hits)


@app.route('/insert/data')
def insert():
    # Inserting Data to Elasticsearch
    es.index(index='hotel', doc_type='hotels_info', id=1, body=doc_1)
    es.index(index='hotel', doc_type='hotels_info', id=2, body=doc_2)
    es.index(index='hotel', doc_type='hotels_info', id=3, body=doc_3)
    es.index(index='hotel', doc_type='hotels_info', id=4, body=doc_4)
    es.index(index='hotel', doc_type='hotels_info', id=5, body=doc_5)
    es.index(index='hotel', doc_type='hotels_info', id=6, body=doc_6)

    return render_template('insert.html')


if __name__ == '__main__':
    app.run(debug=True)
