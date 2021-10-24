# Hotel-Website-using-flask-elasticsearch

## Setup Instructions

1. Creat virtual environment
2. Install requirements.txt
3. Start Elasticsearch server form cmd
4. Run the app.py file
5. To insert data type "/insert/data" afert "localhost:5000"

Now you are good to go. Thank You.

# Sample of my data in database

```
"hits" : [
      {
        "_index" : "samplehotel",
        "_type" : "hotels",
        "_id" : "1",
        "_score" : 1.0,
        "_ignored" : [
          "hDescription.keyword"
        ],
        "_source" : {
          "hImage" : "https://q-xx.bstatic.com/xdata/images/hotel/max300/157674722.jpg?k=bab6297144d0e071750f7c475116b051ee97b547a0c37805d66099999f4b3901&o=",
          "hCost" : "13530",
          "hName" : "Universal's Aventura Hotel",
          "hType" : "Resort",
          "hReview" : "1092",
          "hGuests" : "20",
          "hBedRooms" : "600",
          "hFeatures" : [
            "Air Conditioner",
            "Breakfast",
            "Internet",
            "Laundry",
            "Parking",
            "Pool",
            "Smoking"
          ],
          "hDescription" : """ Universal's Aventura Hotel offers early park admission to The Wizarding World of Harry Potter™ and Universal's Volcano Bay water theme park 1 hour before park opening (Valid theme park admission required; attractions).<span id="dots">...</span><span id="more"><br><br>All rooms include a 43-inch flat-screen TV. A small refrigerator and coffee maker are also available. Complimentary toiletries and a hairdryer are included, as well. Certain rooms feature a seating area.<br><br>A resort-style pool with a hot tub and kids' splash area is available for guests to enjoy. Complimentary WiFi and a free transfer to all Universal Orlando theme parks and Universal CityWalk are provided.<br><br>Restaurants come together inside a food hall offering multiple cuisines for breakfast, lunch, and dinner. The rooftop bar, lobby bar, and pool bar offer a wide range of cocktails. The Aventura also includes an onsite Starbucks®.</span>"""
        }
      }
    ]
```

# Sample of inserting data in database

```
index(index='hotel', doc_type='hotels_info', id=1, body=doc_1)
```

# Query sample

```
{
  "query": {
    "bool": {
      "must_not": {
        "term" : { "_id" : 1 }
        }
    }
  }
}
```
