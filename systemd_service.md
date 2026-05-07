# ⚙️ Create a systemd Service for Python Script on Raspberry Pi

## 🚀 Overview

This guide explains how to create a `systemd` service on a Raspberry Pi to automatically run a Python script after boot.

Example use case:

* Push CPU temperature data to InfluxDB
* Start sensor monitoring automatically
* Run IoT applications in the background

---

# 📁 Step 1: Verify Python Script

Example script location:

```bash id="u8mmpq"
/home/pi/cpu_temp.py
```

Test manually:

```bash id="33n7k0"
python3 /home/pi/cpu_temp.py
```

---

# ⚙️ Step 2: Create systemd Service File

Create a new service:

```bash id="m2v1qk"
sudo nano /etc/systemd/system/cpu_temp.service
```

Paste the following:

```ini id="w1s2q3"
[Unit]
Description=CPU Temperature Logger Service
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/cpu_temp.py
WorkingDirectory=/home/pi
Restart=always
RestartSec=5
User=pi

[Install]
WantedBy=multi-user.target
```

Save and exit:

```text
CTRL + O → ENTER → CTRL + X
```

---

# 🔄 Step 3: Reload systemd

Reload configuration:

```bash id="pz5v2l"
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
```

---

# ▶️ Step 4: Enable Service at Boot

Enable auto-start:

```bash id="89sl0p"
sudo systemctl enable cpu_temp.service
```

---

# ▶️ Step 5: Start Service Now

```bash id="r3k7wy"
sudo systemctl start cpu_temp.service
```

---

# 🔍 Step 6: Check Service Status

```bash id="6qv7k9"
sudo systemctl status cpu_temp.service
```

Expected:

```text
active (running)
```

---

# 📜 Step 7: View Logs

Live logs:

```bash id="t8v2ma"
journalctl -u cpu_temp.service -f
```

---

# 🔁 Step 8: Test Auto-Start on Boot

Reboot Raspberry Pi:

```bash id="m7j4ra"
sudo reboot
```

After reboot:

```bash id="0e4fnk"
sudo systemctl status cpu_temp.service
```

---

# 🛑 Stop or Disable Service

## Stop service

```bash id="4h7yud"
sudo systemctl stop cpu_temp.service
```

## Disable auto-start

```bash id="l0m3sc"
sudo systemctl disable cpu_temp.service
```

---

# ⚠️ Troubleshooting

## Service not starting?

Check logs:

```bash id="4wz7rq"
journalctl -u cpu_temp.service
```

---

## Python path issue?

Verify Python path:

```bash id="a2f9kc"
which python3
```

---

## Permission issue?

Ensure script is executable:

```bash id="h3r8np"
chmod +x /home/pi/cpu_temp.py
```

---

# 🧠 Explanation of Service File

| Option                        | Purpose                          |
| ----------------------------- | -------------------------------- |
| `After=network-online.target` | Wait for network before starting |
| `Restart=always`              | Restart if script crashes        |
| `RestartSec=5`                | Wait 5 seconds before restart    |
| `User=pi`                     | Run as pi user                   |
| `WantedBy=multi-user.target`  | Start during normal boot         |

---

# 📌 Summary

You now have:

* ✅ Python script running automatically after boot
* ✅ Auto-restart on failure
* ✅ Background execution using systemd

---

# 🧑‍💻 Example Use Cases

* CPU temperature monitoring
* Sensor logging
* IoT gateways
* MQTT clients
* Background automation tasks
