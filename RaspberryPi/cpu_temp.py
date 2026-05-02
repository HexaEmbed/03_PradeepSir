from influxdb import InfluxDBClient
import subprocess
import time

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('mydb')

def get_cpu_temp():
    temp = subprocess.getoutput("vcgencmd measure_temp")
    return float(temp.replace("temp=", "").replace("'C", ""))

while True:
    temp = get_cpu_temp()

    json_body = [
        {
            "measurement": "cpu_temp",
            "tags": {
                "host": "raspberrypi"
            },
            "fields": {
                "value": temp
            }
        }
    ]

    client.write_points(json_body)
    print(f"Sent: {temp} °C")

    time.sleep(5)  # every 5 seconds