# imports
from flask import Flask, jsonify
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, text

#load in database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

#save to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session
session = Session(engine)

#set up flask
app = Flask(__name__)




@app.route("/")
def intro():
    return (
        f"Welcome to Hawaii Climate API<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"

    )



@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the Precipitation data"""
    query2 = """Select date, station, prcp 
                From measurement 
                Where date >= '2016-08-23'; 
"""

    df = pd.read_sql(text(query2), con = engine)

    data2 = df.to_dict(orient="records")

    return jsonify(data2)

#create new query
@app.route("/api/v1.0/stations")
def stations():
    """Return list of stations"""
    new_query = """Select *
                From station;"""
    
    df = pd.read_sql(text(new_query), con = engine)
    
    data2 = df.to_dict(orient="records")

    return jsonify(data2)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the temperature from the previous year from the most active Station"""
    query5 = """Select date, station, tobs 
                From measurement 
                Where date >= '2016-08-23' And station = 'USC00519281';"""
    
    df = pd.read_sql(text(query5), con = engine)

    data2 = df.to_dict(orient="records")

    return jsonify(data2)

# create 2 more new queries, one with just the start and one with start/end
@app.route("/api/v1.0/<start>")
def start_date(start):
    new_query2 = f"""Select min(tobs) as min_temp,
                    avg(tobs) as avg_temp,
                    max(tobs) as max_temp
                    From measurement
                    Where date >='{start}';
                    """
    df = pd.read_sql(text(new_query2), con = engine)

    data2 = df.to_dict(orient="records")

    return jsonify(data2)

@app.route("/api/v1.0/<start>/<end>")
def date_range(start, end):
    new_query3 = f"""Select min(tobs) as min_temp,
                    avg(tobs) as avg_temp,
                    max(tobs) as max_temp
                    From measurement
                    Where date >='{start}'
                    And date <= '{end};
                    """
    df = pd.read_sql(text(new_query3), con = engine)

    data2 = df.to_dict(orient="records")

    return jsonify(data2)

if __name__ == "__main__":
    app.run()
