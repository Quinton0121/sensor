import flask
from datetime import datetime
import json
import readings.temperature_reading
import readings.pressure_reading
import sensors.pressure_sensor_manager
import sensors.temperature_sensor_manager
app = flask.Flask(__name__)

@app.route("/<stype>/<seq>", methods=["GET"])
def gitem(stype, seq):
    """This funtion will return sequence number item"""
    m = None
    if "temp" in stype:
        m = sensors.temperature_sensor_manager.TemperatureSensorManager()
    elif "pres" in stype:
        m = sensors.pressure_sensor_manager.PressureSensorManager()
    else:
        return app.response_class(
            'Invalid sensor',
            status = 400
            )
    try:        
        newreading = m.get_reading(int(seq))
        return json.dumps({"date":datetime.strftime(newreading.get_timestamp(),'%Y-%m-%d %H:%M:%S.%f'),
                           "seq_num":newreading.get_sequence_num(),"sensor_name":newreading.get_sensor_model(),
                           "lowest_temp":newreading.get_min_value(), "avg_temp":newreading.get_avg_value(),
                           "highest_temp":newreading.get_max_value(), "status":newreading.get_status()})
        #return newreading.to_json()
    except:
        return app.response_class(
            'Invalid data',
            status = 400
            )

@app.route("/<stype>/", methods=["GET"])
def gAllitem(stype):
    """This funtion will return all items """
    m = None
    if "temp" in stype:
        m = sensors.temperature_sensor_manager.TemperatureSensorManager()
    elif "pres" in stype:
        m = sensors.pressure_sensor_manager.PressureSensorManager()
    else:
        return app.response_class(
            'Invalid sensor',
            status = 400
            )
    try:
        rs = [] 
        for reading in m.get_all_readings():
            newreading = reading
            rs.append({"date":datetime.strftime(newreading.get_timestamp(),'%Y-%m-%d %H:%M:%S.%f'),
                               "seq_num":newreading.get_sequence_num(),"sensor_name":newreading.get_sensor_model(),
                               "lowest_temp":newreading.get_min_value(), "avg_temp":newreading.get_avg_value(),
                               "highest_temp":newreading.get_max_value(), "status":newreading.get_status()})        
        return json.dumps(rs)
    except:
        return app.response_class(
            'Invalid data',
            status = 400
            )


@app.route("/<stype>/add", methods=["POST"])
def aitem(stype):
    """This funtion will return add a reading to the object list"""
    m = None
    if "temp" in stype:
        m = sensors.temperature_sensor_manager.TemperatureSensorManager()
    elif "pres" in stype:
        m = sensors.pressure_sensor_manager.PressureSensorManager()
    else:
        return app.response_class(
            'Invalid sensor',
            status = 400
            )
    #m.load_readings()
    newreading = None
    data = flask.request.data   
    dataDict = json.loads(data)
    if True:
    # try:
        if "temp" in stype:
            newreading = readings.temperature_reading.TemperatureReading(datetime.strptime(dataDict["date"],'%Y-%m-%d %H:%M:%S.%f'),
                                                               m.get_sequence_num()+1,dataDict["sensor_name"],dataDict["lowest_temp"],
                                                               dataDict["avg_temp"],dataDict["highest_temp"],dataDict["status"])
        else:
            newreading = readings.pressure_reading.PressureReading((datetime.strptime(dataDict["date"],'%Y-%m-%d %H:%M')).replace(second=0),dataDict["sensor_name"],
                                                          m.get_sequence_num()+1,dataDict["lowest_temp"],
                                                          dataDict["avg_temp"],dataDict["highest_temp"],dataDict["status"])    
        m.add_reading(newreading)
    
        return json.dumps({"date":datetime.strftime(newreading.get_timestamp(),'%Y-%m-%d %H:%M:%S.%f'),
                           "seq_num":newreading.get_sequence_num(),"sensor_name":newreading.get_sensor_model(),
                           "lowest_temp":newreading.get_min_value(), "avg_temp":newreading.get_avg_value(),
                           "highest_temp":newreading.get_max_value(), "status":newreading.get_status()})
    # except:
        return app.response_class(
            'Invalid data',
            status = 400
            )

@app.route("/<stype>/<seq>", methods=["PUT"])
def uitem(stype, seq):
    """update the sensor reading list and sensor file"""
    m = None
    if "temp" in stype:
        m = sensors.temperature_sensor_manager.TemperatureSensorManager()
    elif "pres" in stype:
        m = sensors.pressure_sensor_manager.PressureSensorManager()
    else:
        return app.response_class(
            'Invalid sensor',
            status = 400
            )
    try:        
        newreading = None
        data = flask.request.data
        dataDict = json.loads(data)
        if "temp" in stype:
            newreading = readings.temperature_reading.TemperatureReading(datetime.strptime(dataDict["date"],'%Y-%m-%d %H:%M:%S.%f'),
                                                               seq,dataDict["sensor_name"],dataDict["lowest_temp"],
                                                               dataDict["avg_temp"],dataDict["highest_temp"],dataDict["status"])
        else:
            newreading = readings.pressure_reading.PressureReading(datetime.strptime(dataDict["date"],'%Y-%m-%d %H:%M'),dataDict["sensor_name"],
                                                          seq,dataDict["lowest_temp"],
                                                          dataDict["avg_temp"],dataDict["highest_temp"],dataDict["status"])
        m.update_reading(int(seq),newreading)
        return json.dumps({"date":dataDict["date"],
                           "seq_num":seq,"sensor_name":dataDict["sensor_name"],
                           "lowest_temp":dataDict["lowest_temp"], "avg_temp":dataDict["avg_temp"],
                           "highest_temp":dataDict["highest_temp"], "status":dataDict["status"]})
    except:
        return app.response_class(
            'Invalid data',
            status = 400
            )


@app.route("/<stype>/<seq>", methods=["DELETE"])
def ditem(stype, seq):
    """ """
    m = None
    if "temp" in stype:
        m = sensors.temperature_sensor_manager.TemperatureSensorManager()
    elif "pres" in stype:
        m = sensors.pressure_sensor_manager.PressureSensorManager()
    else:
        return app.response_class(
            'Invalid sensor',
            status = 400
            )
    try:    
        m.delete_reading(seq)
        return ""
    except:
        
        return app.response_class(
            'Invalid data',
            status = 400
            )

@app.errorhandler(405)
def page_not_found(e):
    """handle page not found"""
    return app.response_class(
        'Invalid data',
            status = 400
        )

if __name__ == "__main__":
    app.run()