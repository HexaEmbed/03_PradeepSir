# Raspberry Pi Remote Access using Tailscale VPN

## Overview

This guide shows how to securely access your Raspberry Pi from anywhere using a zero-config VPN powered by **Tailscale**.

With this setup, you can:

*  Access your Raspberry Pi remotely (SSH, Grafana, InfluxDB, etc.)
*  Avoid port forwarding and firewall complexity
*  Get secure, encrypted connections instantly

---

## What is Tailscale?

Tailscale is a modern VPN built on WireGuard that creates a secure private network (called a *tailnet*) between your devices.

---

## Pre-Requisite
* [A Tailscale account](https://tailscale.com/docs/install/linux)
---

## Step 1: Install Tailscale on Raspberry Pi

Run the official install script on Raspberry Pi Terminal:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

---

## Step 2: Authenticate & Connect

Start Tailscale:

```bash
sudo tailscale up
```

This will:

* Print a login URL in the terminal
* Open it in your browser
* Ask you to log in

Once done, your Raspberry Pi joins your private network.

---

## Step 3: Get Your Pi’s VPN IP

Check assigned IP:

```bash
tailscale ip -4
```

Example:

```
100.101.102.103
```

---

## Step 4: Access Your Raspberry Pi Remotely

From another device connected to Tailscale:

### SSH

```bash
ssh debian@100.101.102.103
```

### Access services

* Grafana → `http://100.x.x.x:3000`
* InfluxDB → `http://100.x.x.x:8086`

---

## Example Use Case

```text
Laptop (Tailscale)
        ↓
   Secure VPN
        ↓
Raspberry Pi → Grafana Dashboard
```

No port forwarding. No public IP required.

---

## Optional Configurations

### Enable Tailscale at boot

```bash
sudo systemctl enable tailscaled
```

---

### Enable SSH via Tailscale (no password needed)

```bash
sudo tailscale up --ssh
```

Then connect:

```bash
ssh debian@raspberrypi
```
---

## Verify Connection

Check status:

```bash
tailscale status
```
or
```bash
https://login.tailscale.com/admin/machines
```

---

## Notes

* Free plan supports up to 100 devices
* Devices must be logged into same Tailscale account
* Works behind NAT, CGNAT, and firewalls

---

## Uninstall (Do not Execute this step)

```bash
sudo tailscale down
sudo apt remove tailscale
```
---
##### Page Maintained By: [hexaembed@gmail.com](hexaembed@gmail.com)
---

