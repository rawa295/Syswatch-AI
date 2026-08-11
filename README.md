# SysWatch AI

**SysWatch AI** is a lightweight Linux system monitoring and health-check tool built with Python.

It continuously collects system metrics, evaluates overall system health, monitors processes and services, tracks active user sessions, reads system logs, and stores monitoring metrics in SQLite.

## Features

### System Monitoring

* CPU usage and status
* RAM usage and status
* Disk usage and status
* Network traffic
* Top running processes
* System services status
* Logged-in users
* System logs

### Health Monitoring

SysWatch AI evaluates the overall system condition and reports one of three health states:

* `HEALTHY`
* `WARNING`
* `CRITICAL`

Health status events are also recorded by the application logger.

### Process Monitoring

Displays the top processes based on CPU usage, including:

* PID
* Process name
* CPU usage
* RAM usage
* Process status

### Service Monitoring

Checks configured Linux services and reports whether they are:

* `running`
* `stopped`
* `not_found`

Services are configured through `config/config.yaml` instead of being hard-coded in the monitoring logic.

Example:

```yaml
services:
  - ssh
  - nginx
  - cron
```

### User Monitoring

Collects active user sessions, including:

* Username
* Terminal
* Host
* Session start time

### System Logs

Reads recent logs from the Linux `systemd journal` using `journalctl`.

### Database

Monitoring metrics are stored in SQLite for later analysis.

Stored metrics include:

* Timestamp
* CPU usage
* RAM usage
* Disk usage
* Network sent bytes
* Network received bytes
* System health status

### Linux Service

SysWatch AI can run as a `systemd` service and execute monitoring cycles automatically.

The monitoring cycle runs every **10 seconds**.

---

## Technologies

* Python 3
* psutil
* SQLite
* systemd
* journalctl
* Linux
* YAML
* Git
* GitHub

---

## Project Structure



```text
SysWatch-AI/
│
├── agent/
│   ├── main.py
│   └── health_check.py
├── collectors/
│   ├── cpu.py
│   ├── memory.py
│   ├── disk.py
│   ├── network.py
│   ├── processes.py
│   ├── services.py
│   ├── users.py
│   └── system_logs.py
├── config/
│   └── config.yaml
├── database/
│   └── database.py
├── logger/
│   └── logger.py
├── utils/
│   ├── colors.py
│   └── formatter.py
├── logs/
├── requirements.txt
├── .gitignore
└── README.md



---

## Requirements

SysWatch AI is designed for Linux systems using `systemd`.

Requirements:

* Linux
* Python 3
* `systemd`
* `journalctl`
* Python virtual environment

### Kali Linux

Install Python and virtual environment support:

```bash
sudo apt update
sudo apt install python3 python3-venv
```

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Configure the services to monitor in:

```text
config/config.yaml
```

Example:

```yaml
services:
  - ssh
  - nginx
  - cron
```

---

## Running SysWatch AI

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the monitoring agent:

```bash
python3 -m agent.main
```

Example output:

```text
CPU       6.1%      ● Excellent
RAM       14.8%     ● Excellent
DISK      29.9%     ● Excellent
NETWORK   Sent: 2.63 MB | Received: 76.19 MB

---

## System Status: ● HEALTHY

## Top Processes

PID     NAME                CPU       RAM       STATUS
1076    Xorg                0.0       1.94      sleeping
1770    xfwm4               0.0       1.56      sleeping
1878    orca               0.0       1.06      sleeping

## Services

NAME                STATUS
ssh                 running
nginx               stopped
cron                running

## Users

NAME                TERMINAL       HOST                STARTED
user                x11             None                Tue ...

## System Logs

...
```

---

## Running as a systemd Service

SysWatch AI can run continuously as a Linux `systemd` service.

Example service configuration:

```ini
[Unit]
Description=SysWatch AI Monitoring Service
After=network.target

[Service]
Type=simple
User=<linux-user>
WorkingDirectory=<project-path>
ExecStart=<project-path>/.venv/bin/python -m agent.main
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Replace `<linux-user>` and `<project-path>` with the values for your system.

Reload systemd:

```bash
sudo systemctl daemon-reload
```

Enable the service at boot:

```bash
sudo systemctl enable syswatch-ai
```

Start the service:

```bash
sudo systemctl start syswatch-ai
```

Check service status:

```bash
sudo systemctl status syswatch-ai
```

View live service logs:

```bash
sudo journalctl -u syswatch-ai -f
```

---

## Version

### SysWatch AI v1.0.0

The first release focuses on core Linux system monitoring and health checking.

### Included in v1

* CPU monitoring
* RAM monitoring
* Disk monitoring
* Network monitoring
* Process monitoring
* Service monitoring
* User session monitoring
* System log monitoring
* Health status evaluation
* SQLite metrics storage
* Application logging
* 10-second monitoring cycle
* Linux `systemd` service integration

---

## Future Improvements

Planned improvements for future versions include:

* AI-based anomaly detection
* Historical metrics analysis
* Web dashboard
* Alert notifications
* Advanced service health checks
* Disk I/O monitoring
* Security event detection
* Automated remediation
* Docker support
* Cloud monitoring integration

---

## License

This project is currently provided for educational and portfolio purposes.
