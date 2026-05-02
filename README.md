# 03_PradeepSir
RealTime Raspberry Pi Health Monitor System

# 📡 Raspberry Pi CPU Temperature Monitoring (InfluxDB + Grafana + Cloud)

## 🚀 Overview

This project monitors **CPU temperature** from a Raspberry Pi in real-time and visualizes it using Grafana dashboards.

It supports:

* ✅ Local monitoring (InfluxDB + Grafana on Raspberry Pi)
* ☁️ Cloud monitoring (InfluxDB Cloud free tier)
* 🔁 Optional dual-write (local + cloud)

---

## 🧠 Architecture

```
Raspberry Pi
   ├── CPU Temperature (vcgencmd)
   ├── Python / Telegraf
   ↓
InfluxDB (Local + / or Cloud)
   ↓
Grafana Dashboard (Local / Remote)
```

---

## ⚙️ Requirements

### Hardware

* Raspberry Pi (any model with network access)

### Software

* Python 3
* InfluxDB (local or cloud)
* Grafana
* (Optional) Telegraf

---
## ⚙️ Installing InfluxDB on Raspberry Pi
### 1. Update your system
sudo apt update && sudo apt upgrade
### 2. Install InfluxDB (v1.x – easier on Pi)
```bash
wget https://dl.influxdata.com/influxdb/releases/influxdb_1.8.10_armhf.deb
sudo dpkg -i influxdb_1.8.10_armhf.deb
```
### 3. Start the service
```bash
sudo systemctl start influxdb
sudo systemctl enable influxdb
```
### 4. Open InfluxDB CLI
```bash
influx
```
---

## 🔥 Step 1: Read CPU Temperature

```bash
vcgencmd measure_temp
```

Example:

```
temp=52.3'C
```

---

## 🐍 Step 2: Python Script (Push Data)

Install dependency:

```bash
pip3 install influxdb influxdb-client
```

### 📄 `cpu_temp.py`

```python
from influxdb import InfluxDBClient
from influxdb_client import InfluxDBClient as InfluxDBClientV2, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import subprocess
import time

# -------- LOCAL DB CONFIG --------
local_client = InfluxDBClient(host='localhost', port=8086)
local_client.switch_database('mydb')

# -------- CLOUD DB CONFIG --------
url = "https://YOUR_CLOUD_URL"
token = "YOUR_TOKEN"
org = "YOUR_ORG"
bucket = "mybucket"

cloud_client = InfluxDBClientV2(url=url, token=token)
cloud_write = cloud_client.write_api(write_options=SYNCHRONOUS)

def get_cpu_temp():
    temp = subprocess.getoutput("vcgencmd measure_temp")
    return float(temp.replace("temp=", "").replace("'C", ""))

while True:
    temp = get_cpu_temp()

    # Local write
    local_json = [{
        "measurement": "cpu_temp",
        "tags": {"host": "raspberrypi"},
        "fields": {"value": temp}
    }]
    local_client.write_points(local_json)

    # Cloud write
    point = Point("cpu_temp").field("value", temp)
    cloud_write.write(bucket=bucket, org=org, record=point)

    print(f"Sent: {temp} °C")

    time.sleep(5)
```

Run:

```bash
python3 cpu_temp.py
```

---

## 📊 Step 3: Install Grafana on Raspberry Pi

```bash
sudo apt install -y apt-transport-https software-properties-common

wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list

sudo apt update
sudo apt install grafana

Start it:

sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

### Access Grafana

```
http://<raspberry-pi-ip>:3000
```

Default login:

* username: admin
* password: admin

---

## 🔗 Add Data Source

### Local InfluxDB (v1.8)

* URL: `http://localhost:8086`
* Database: `mydb`
* Query Language: InfluxQL

### Cloud InfluxDB (v2)

* URL: your cloud endpoint
* Token: your API token
* Org + Bucket: as configured

---

## 📈 Step 4: Dashboard Query

```sql
SELECT mean("value") FROM "cpu_temp"
WHERE $timeFilter
GROUP BY time($__interval)
```

---

## 🎨 Visualization Tips

* Use **Line Graph** for trends
* Use **Gauge** for current temperature
* Set unit → **Celsius (°C)**
* Refresh interval → **5s–10s**

---

## 🔁 Optional: Telegraf (Recommended Alternative)

Instead of Python, use Telegraf for automatic metrics collection.

### Install:

```bash
sudo apt install telegraf
```

### Example Config:

```toml
[[inputs.cpu]]
[[inputs.system]]
[[inputs.temp]]

[[outputs.influxdb]]
  urls = ["http://localhost:8086"]
  database = "mydb"

[[outputs.influxdb_v2]]
  urls = ["https://YOUR_CLOUD_URL"]
  token = "YOUR_TOKEN"
  organization = "YOUR_ORG"
  bucket = "mybucket"
```

Start:

```bash
sudo systemctl start telegraf
```

---

## ⚠️ Notes

* Keep logging interval ≥ 5 seconds (avoid SD card wear)
* Free cloud tiers may have:

  * Storage limits
  * Request limits
* Use retention policies for long-term storage

---

## 🚀 Future Improvements

* Add CPU usage, RAM, disk monitoring
* Set alerts (e.g., temperature > 70°C)
* Remote dashboard access
* Dockerize the entire stack

---

## 📌 Summary

This project provides:

* Real-time CPU monitoring
* Local + cloud storage flexibility
* Clean visualization via Grafana

---

## 🧑‍💻 Author

Built for learning IoT monitoring, embedded systems, and time-series data pipelines.

