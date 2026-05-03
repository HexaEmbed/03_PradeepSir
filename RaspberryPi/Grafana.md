## Install Grafana on Raspberry Pi
   Execute below steps on Raspberry Pi Terminal

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

## Add Data Source

### Local InfluxDB (v1.8)

* URL: `http://localhost:8086`
* Database: `mydb`
* Query Language: InfluxQL
---
##  Notes

* Keep logging interval ≥ 5 seconds (avoid SD card wear)
* Free cloud tiers may have:

  * Storage limits
  * Request limits
* Use retention policies for long-term storage

---

##  Future Improvements

* Add CPU usage, RAM, disk monitoring
* Set alerts (e.g., temperature > 70°C)
* Remote dashboard access
* Dockerize the entire stack
---
##### Page Maintained By: [hexaembed@gmail.com](hexaembed@gmail.com)
---
