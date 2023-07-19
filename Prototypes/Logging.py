import sqlite3

def log_to_database(data):
    sensor_id = data["sensor_id"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    wind_speed = data["wind_speed"]
    location = data["location"]
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS DataLogging(
                    sensor_id int,
                    temperature int,
                    humidity int,
                    wind_speed int,
                    location text)
                """)
    c.execute("INSERT INTO DataLogging VALUES (?,?,?,?,?)", (sensor_id, temperature, humidity, wind_speed, location))
    conn.commit()
    conn.close()