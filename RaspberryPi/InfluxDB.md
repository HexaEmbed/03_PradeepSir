## Method 1 (Recomended): Installing InfluxDB on Raspberry Pi

Install dependency:

```bash
pip3 install influxdb influxdb-client
Or 
sudo apt install python3-influxdb
```
---
## Method 2: Installing InfluxDB on Raspberry Pi
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
##### Page Maintained By: [hexaembed@gmail.com](hexaembed@gmail.com)
---
