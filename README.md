
<img width="1392" height="648" alt="Gemini_Generated_Image_6a1g476a1g476a1g" src="https://github.com/user-attachments/assets/8cd4e63e-36f5-4d6a-8e28-8816e5b1aced" />



# 🚀 MultiRadar - Advanced Multi-Network Radar Scanner

**Coded by: Mr. Sabaz Ali Khan**

MultiRadar is an advanced Python-based network scanning and visualization tool designed for cybersecurity enthusiasts, ethical hackers, and researchers. This project enables users to detect and monitor multiple network signals simultaneously, providing real-time insights into connected devices. It is optimized for Kali Linux and built with efficiency, accuracy, and usability in mind.

---

## 📌 Overview

MultiRadar is a powerful multi-network reconnaissance tool that scans and visualizes wireless and network signals. It displays detected devices in a radar-style interface, making it ideal for ethical hacking, cybersecurity analysis, and educational demonstrations.

---

## ✨ Features

* 📡 Real-Time Multi-Network Scanning
* 🎯 Radar-Style Visualization Interface
* 🌐 Detection of Active Hosts and Devices
* 📊 Live IP and MAC Address Monitoring
* 🔍 Open Port Identification
* ⚡ Fast and Lightweight Performance
* 🐍 Developed in Python
* 🐧 Optimized for Kali Linux
* 🎨 Interactive and User-Friendly Dashboard
* 🛡️ Designed for Ethical Hacking and Research

---

## 🛠️ Technologies Used

| Technology     | Purpose                              |
| -------------- | ------------------------------------ |
| Python 3       | Core Programming Language            |
| Scapy          | Packet Analysis and Network Scanning |
| Nmap           | Advanced Network Discovery           |
| Socket         | Network Communication                |
| Matplotlib     | Radar Visualization                  |
| NumPy          | Data Processing                      |
| Tkinter / PyQt | Graphical User Interface             |
| Kali Linux     | Security Testing Environment         |

---

## 📂 Project Structure

```
MultiRadar/
│── multiradar.py
│── radar_engine.py
│── network_scanner.py
│── visualization.py
│── utils.py
│── requirements.txt
│── README.md
│── LICENSE
│── assets/
│   └── multiradar_banner.png
└── screenshots/
    └── radar_interface.png
```

---

## ⚙️ Installation Guide (Kali Linux)

### Step 1: Update Your System

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Required Dependencies

```bash
sudo apt install python3 python3-pip nmap -y
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/whoami592/MultiRadar.git
cd MultiRadar
```

### Step 4: Install Python Libraries

```bash
pip3 install -r requirements.txt
```

### Step 5: Grant Root Privileges

```bash
sudo chmod +x multiradar.py
```

---

## ▶️ Usage

Run the tool using:

```bash
sudo python3 multiradar.py
```

Example with a target network:

```bash
sudo python3 multiradar.py --target 192.168.1.0/24
```

### Optional Arguments

| Argument      | Description                  |
| ------------- | ---------------------------- |
| `--target`    | Specify target network range |
| `--ports`     | Scan specific ports          |
| `--visualize` | Enable radar visualization   |
| `--output`    | Save scan results to a file  |
| `--fast`      | Enable fast scanning mode    |

Example:

```bash
sudo python3 multiradar.py --target 192.168.1.0/24 --visualize --output results.json
```

---

## 📦 requirements.txt

```
scapy
python-nmap
matplotlib
numpy
colorama
rich
```

Install them using:

```bash
pip3 install -r requirements.txt
```

---

## 📸 Screenshots

<img width="1420" height="620" alt="Gemini_Generated_Image_jkxztujkxztujkxz" src="https://github.com/user-attachments/assets/538890a6-8415-4538-93f9-2b4223e68485" />


Add screenshots in the `screenshots` folder to showcase the radar interface.

```
screenshots/radar_interface.png
```

---

## 🎯 Use Cases

* Cybersecurity Training
* Network Monitoring
* Ethical Hacking Labs
* Educational Demonstrations
* Digital Forensics Research
* Wireless Network Analysis

---

## ⚠️ Legal Disclaimer

This tool is intended for educational purposes and authorized security testing only. Unauthorized use of this software against networks without explicit permission is illegal. The developer is not responsible for any misuse or damage caused.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 👨‍💻 Author

**Mr. Sabaz Ali Khan**
🔹 Cybersecurity Enthusiast | Python Developer | Ethical Hacker
🔹 Kali Linux User

* GitHub: https://github.com/your-username
* YouTube: Tech & Hack with Sabaz

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## ⭐ Support

If you like this project, please consider giving it a star on GitHub!

**"Empowering Cybersecurity Through Innovation."**

