# Raspberry Pi CPU Temperature Monitoring (InfluxDB + Grafana + Cloud)

## Overview

This project monitors **CPU temperature** from a Raspberry Pi in real-time and visualizes it using Grafana dashboards.

It supports:

* Local monitoring (InfluxDB + Grafana on Raspberry Pi)
* Cloud monitoring (InfluxDB Cloud free tier)
* Optional dual-write (local + cloud)

---

## Architecture

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

## Requirements

### Hardware

* Raspberry Pi (any model with network access)

### Software

* Python 3
* InfluxDB (local or cloud)
* Grafana
* (Optional) Telegraf

---
## Run cpu_temp.py script:

```bash
python3 cpu_temp.py
```

---
### Access Grafana

```
http://<raspberry-pi-ip>:3000
```

Default login:

* username: admin
* password: admin

---
##  Summary

This project provides:

* Real-time CPU monitoring
* Local + cloud storage flexibility
* Clean visualization via Grafana
---
##### Page Maintained By: [hexaembed@gmail.com](hexaembed@gmail.com)
---
