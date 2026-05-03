# Raspberry Pi Setup Guide (Flash SD Card + System Configuration)

## Overview

This guide walks you through preparing a fresh Raspberry Pi setup:

* Flash Raspberry Pi OS to SD card
* Enable SSH (headless access)
* Configure Internet (Wi-Fi or Ethernet)
---

## Pre-Requisite

* Raspberry Pi board
* MicroSD card (≥16GB recommended)
* SD card reader
* Laptop/PC
* Internet connection
* [Complete Setup kit](https://robu.in/product/raspberry-pi-3-model-b-plus-starter-kit)

---

## Step 1: Download Raspberry Pi OS

Download the official tool:

```text
https://www.raspberrypi.com/software/
```
---

## Step 2: Flash OS to SD Card

1. Insert SD card into your computer
2. Open Raspberry Pi Imager
3. Click **Choose OS**

   * Select: *Raspberry Pi OS (32-bit)*
4. Click **Choose Storage**

   * Select your SD card
5. After Flashing completes, Boot Raspberry Pi

   * Insert SD card into Raspberry Pi
   * Connect PC Monitor and Keyboard to Raspberry Pi
   * Power it ON
   * Wait ~1–2 minutes for first boot
   * Enter User Name: eg: debian
   * Enter Password: eg: password@000
---

## Enable SSH

* Enable SSH
* Enter the command:
  ```text
  sudo raspi-config
  ```
* Navigate to Interface Options (or Interfacing Options) using the arrow keys.
* Select SSH, then choose Yes to enable it.
* Select Finish to exit.

---

## Configure Internet (Wi-Fi or Ethernet)

* Connect Internet Ethernet Cable or Configure wireless LAN
* Open terminal and run:
  ```text
  sudo raspi-config
  ```
* Navigate to System Options > Wireless LAN.
* Select your country, enter SSID, and password.
---

## Step 3: Find Raspberry Pi IP

Check from your router OR use:

```bash
ifconfig
```
or
```bash
ping raspberrypi.local
```

---

## Step 4: Connect via SSH

From your PC:

```bash
ssh debian@raspberrypi.local
```

or using IP:

```bash
ssh pi@192.168.x.x
```

---

## Optional Manual Setup (if needed)

### Set timezone manually

```bash
sudo raspi-config
```

Go to:

```text
Localisation Options → Timezone → Asia → Kolkata
```

---

### Set keyboard layout

```bash
sudo raspi-config
```

```text
Localisation Options → Keyboard → English (India) or US
```

---

## Next Steps

* Install updates:

```bash
sudo apt update && sudo apt upgrade
```

* Install tools:

  * InfluxDB -> Refer: INFLUXDB.md
  * Grafana -> Refer: GRAFANA.md
  * Tailscale -> [https://github.com/HexaEmbed/RealTimeMonitoringSystem/blob/main/TAILSCALE_VPN.md](https://github.com/HexaEmbed/RealTimeMonitoringSystem/blob/main/TAILSCALE_VPN.md)

---
##### Page Maintained By: [hexaembed@gmail.com](hexaembed@gmail.com)
---
