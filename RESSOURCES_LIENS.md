# 🎓 Ressources Complètes CPS - PDFs, Vidéos & Tutoriels

Guide organisé avec tous les liens directs pour chaque domaine et projet.

---

## 📊 Table des Ressources

| Domaine | Type | Ressource | Lien | Durée |
|---------|------|-----------|------|-------|
| **SENSORS** | Vidéo | DHT22 Tutorial | [YouTube](https://www.youtube.com/watch?v=DI_eXZhTYhE) | 15 min |
| | Vidéo | Python Data Logging | [YouTube](https://www.youtube.com/watch?v=A9pxSsS5U-4) | 20 min |
| | Vidéo | Matplotlib Guide | [YouTube](https://www.youtube.com/watch?v=UO98lJQ3QGY) | 30 min |
| | Cours | Adafruit DHT | [Learn](https://learn.adafruit.com/dht/python) | - |
| | Doc | Python CSV | [Docs](https://docs.python.org/3/library/csv.html) | - |
| | Doc | Pandas | [Docs](https://pandas.pydata.org/docs/) | - |
| **ROBOTICS** | Vidéo | Kinematics Basics | [YouTube](https://www.youtube.com/watch?v=RA2aHRFGxT0) | 45 min |
| | Vidéo | Forward Kinematics | [YouTube](https://www.youtube.com/watch?v=8jnxIbJxe4Q) | 20 min |
| | Vidéo | ROS Basics | [YouTube](https://www.youtube.com/watch?v=v9Rvg1b4lYg) | 60 min |
| | Cours | MIT Intro to Robotics | [OCW](https://ocw.mit.edu/courses/2-12-introduction-to-robotics/) | 12 weeks |
| | Cours | Coursera Robot Dynamics | [Coursera](https://www.coursera.org/learn/robot-dynamics) | 8 weeks |
| **AUTONOMOUS VEHICLES** | Vidéo | AV Course | [YouTube](https://www.youtube.com/watch?v=LQsNueLvXcs) | 3 hours |
| | Vidéo | CARLA Simulator | [YouTube](https://www.youtube.com/watch?v=7Q0jNFfECmM) | 30 min |
| | Vidéo | Path Planning | [YouTube](https://www.youtube.com/watch?v=sL3b2V7zNMw) | 45 min |
| | Platform | CARLA Simulator | [carla.org](http://carla.org/) | - |
| | Platform | Apollo AV | [apollo.auto](https://apollo.auto/) | - |
| **IoT** | Vidéo | MQTT Tutorial | [YouTube](https://www.youtube.com/watch?v=E-VY2m2u-PI) | 40 min |
| | Vidéo | Home Assistant | [YouTube](https://www.youtube.com/watch?v=JOoRt0rKAns) | 30 min |
| | Vidéo | Node-RED Dashboard | [YouTube](https://www.youtube.com/watch?v=2nfCVhqXRQI) | 25 min |
| | Platform | Home Assistant | [home-assistant.io](https://www.home-assistant.io/) | - |
| | Platform | Node-RED | [nodered.org](https://nodered.org/) | - |
| **NETWORK SECURITY** | Vidéo | Packet Analysis | [YouTube](https://www.youtube.com/watch?v=qdNvXi1wVyE) | 45 min |
| | Vidéo | Snort IDS | [YouTube](https://www.youtube.com/watch?v=LJ6v4TsHDdU) | 40 min |
| | Vidéo | Suricata Rules | [YouTube](https://www.youtube.com/watch?v=ZD-VXAJlqRQ) | 30 min |
| | Doc | Scapy | [scapy.io](https://scapy.readthedocs.io/) | - |
| | Platform | Snort | [snort.org](https://www.snort.org/) | - |
| | Platform | Suricata | [suricata.io](https://suricata.io/) | - |
| **REAL-TIME SYSTEMS** | Cours | CMU Real-Time | [cmu.edu](http://www.cs.cmu.edu/) | Semester |
| | Cours | Coursera RTOS | [coursera.org](https://www.coursera.org/learn/real-time-operating-systems) | 8 weeks |
| | Vidéo | RMS Scheduling | [YouTube](https://www.youtube.com/watch?v=e-JRyVDXqJ8) | 25 min |
| | Vidéo | FreeRTOS | [YouTube](https://www.youtube.com/watch?v=tKpDEF3f1u4) | 50 min |
| | Platform | FreeRTOS | [freertos.org](https://www.freertos.org/) | - |

---

## 🌡️ **SENSORS - Ressources Détaillées**

### Vidéos Essentielles
1. **[DHT22 Sensor Complete Tutorial](https://www.youtube.com/watch?v=DI_eXZhTYhE)** (15 min)
   - Brochage et connexion
   - Code Arduino/Python
   - Troubleshooting

2. **[Data Logging in Python](https://www.youtube.com/watch?v=A9pxSsS5U-4)** (20 min)
   - CSV basics
   - Timestamps
   - File I/O

3. **[Matplotlib Complete Guide](https://www.youtube.com/watch?v=UO98lJQ3QGY)** (30 min)
   - Line plots
   - Histograms
   - Real-time plotting

### Tutoriels et Documentation
- **Adafruit DHT Library**: https://learn.adafruit.com/dht/python
- **Python CSV Module**: https://docs.python.org/3/library/csv.html
- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **NumPy Array Guide**: https://numpy.org/doc/stable/

### Projets Pratiques
```python
# Projet 1: Temperature Monitoring
# Fichiers prêts:
# - temperature_sensor_reader.py
# - visualize_sensor_data.py
# - PROJECT_TEMPERATURE_SENSOR.md

cd sensors
python temperature_sensor_reader.py
```

### Concepts à Maîtriser
- [ ] Sensor types (analog vs digital)
- [ ] ADC conversion
- [ ] Calibration techniques
- [ ] Data smoothing
- [ ] Time-series analysis

---

## 🤖 **ROBOTICS - Ressources Détaillées**

### Vidéos Recommandées
1. **[Robotic Arm Kinematics](https://www.youtube.com/watch?v=RA2aHRFGxT0)** (45 min)
   - DH Parameters
   - Forward Kinematics
   - Inverse Kinematics

2. **[Forward Kinematics Explained](https://www.youtube.com/watch?v=8jnxIbJxe4Q)** (20 min)
   - Math foundations
   - Transformation matrices
   - Code examples

3. **[ROS Robotics Basics](https://www.youtube.com/watch?v=v9Rvg1b4lYg)** (60 min)
   - ROS architecture
   - Topics and services
   - Robot simulation

### Cours Universitaires Gratuits
- **MIT Introduction to Robotics**: https://ocw.mit.edu/courses/2-12-introduction-to-robotics/
  - 32 lectures
  - Homework + solutions
  - Video lectures

- **Coursera Robot Dynamics**: https://www.coursera.org/learn/robot-dynamics
  - Specialization on dynamics
  - 8-week course
  - Graded assignments

### Bibliothèques Python
```python
# PyBullet - Physics Simulation
pip install pybullet
import pybullet as p

# ROS Python
pip install rospy

# NumPy for matrices
pip install numpy scipy matplotlib
```

### Ressources Avancées
- **Stanford Robotics**: https://robotics.stanford.edu/
- **Berkeley DeepDrive**: https://deepdrive.berkeley.edu/
- **Robot Academy**: https://robotacademy.net.au/

---

## 🚗 **AUTONOMOUS VEHICLES - Ressources Détaillées**

### Simulateurs
1. **CARLA Simulator** (Gratuit)
   - Installation: http://carla.org/
   - Documentation: https://carla.readthedocs.io/
   - Python API: https://github.com/carla-simulator/carla

2. **Apollo Autonomous Driving**
   - Full stack AV
   - https://apollo.auto/
   - GitHub: https://github.com/ApolloAuto/apollo

### Vidéos Essentielles
1. **[Autonomous Vehicles Course](https://www.youtube.com/watch?v=LQsNueLvXcs)** (3 heures)
2. **[CARLA Simulator Tutorial](https://www.youtube.com/watch?v=7Q0jNFfECmM)** (30 min)
3. **[Path Planning Algorithms](https://www.youtube.com/watch?v=sL3b2V7zNMw)** (45 min)

### Datasets
- **Waymo Open Dataset**: https://waymo.com/open/
- **nuScenes**: https://www.nuscenes.org/
- **KITTI Dataset**: http://www.cvlibs.net/datasets/kitti/

### Livres Recommandés
- "Autonomous Vehicles" - Shladover & Bishop
- "Motion Planning" - LaValle

---

## 🏠 **IoT - Ressources Détaillées**

### Plateformes de Domotique
1. **Home Assistant** (Gratuit, Open Source)
   - https://www.home-assistant.io/
   - 2000+ intégrations
   - Community-driven

2. **Node-RED** (Flow-based programming)
   - https://nodered.org/
   - Visual automation
   - Integration hub

### MQTT Protocol
- **MQTT.org**: https://mqtt.org/
- **Mosquitto Broker**: https://mosquitto.org/
- **HiveMQ**: https://www.hivemq.com/

### Composants Populaires
```python
# ESP32 Microcontroller
# - WiFi built-in
# - GPIO pins
# - Analog inputs

# Sensors:
# - DHT22 (Temperature/Humidity)
# - BMP280 (Pressure)
# - LDR (Light)
# - Motion sensors
```

### Vidéos
1. **[MQTT Tutorial](https://www.youtube.com/watch?v=E-VY2m2u-PI)** (40 min)
2. **[Home Assistant Setup](https://www.youtube.com/watch?v=JOoRt0rKAns)** (30 min)
3. **[Node-RED Dashboard](https://www.youtube.com/watch?v=2nfCVhqXRQI)** (25 min)

### Frameworks
- **ESPHome**: https://esphome.io/
- **Tasmota**: https://tasmota.github.io/docs/

---

## 🔒 **NETWORK SECURITY - Ressources Détaillées**

### Outils Principaux
1. **Scapy** (Python packet manipulation)
   - https://scapy.readthedocs.io/
   - Network scanning
   - Packet crafting

2. **Snort IDS** (Signature-based detection)
   - https://www.snort.org/
   - Rules database
   - Ongoing updates

3. **Suricata** (Modern IDS/IPS)
   - https://suricata.io/
   - Faster than Snort
   - Multi-threading

### Vidéos Essentielles
1. **[Network Packet Analysis](https://www.youtube.com/watch?v=qdNvXi1wVyE)** (45 min)
2. **[Snort IDS Tutorial](https://www.youtube.com/watch?v=LJ6v4TsHDdU)** (40 min)
3. **[Suricata Rules](https://www.youtube.com/watch?v=ZD-VXAJlqRQ)** (30 min)

### Cours de Sécurité
- **Coursera Cybersecurity**: https://www.coursera.org/learn/cybersecurity-basics
- **edX Network Security**: https://www.edx.org/course/network-security
- **TryHackMe**: https://tryhackme.com/

### Livres
- "Network Security Essentials" - Stallings
- "Cybersecurity Essentials" - SANS Institute

---

## ⚡ **REAL-TIME SYSTEMS - Ressources Détaillées**

### RTOS Populaires
1. **FreeRTOS** (Open source)
   - https://www.freertos.org/
   - Arduino compatible
   - Documentation complète

2. **RT-Thread** (Industry standard)
   - https://github.com/rt-thread/rt-thread
   - Production-ready
   - Chinese origin

3. **QNX** (Commercial)
   - https://www.qnx.com/developers/
   - High-reliability
  - Critical systems

### Cours Universitaires
- **CMU Real-Time Systems**: http://www.cs.cmu.edu/
- **Coursera RTOS**: https://www.coursera.org/learn/real-time-operating-systems

### Vidéos
1. **[Rate Monotonic Scheduling](https://www.youtube.com/watch?v=e-JRyVDXqJ8)** (25 min)
2. **[FreeRTOS Tutorial](https://www.youtube.com/watch?v=tKpDEF3f1u4)** (50 min)

### Documentation Technique
- **POSIX Real-Time**: https://pubs.opengroup.org/onlinepubs/9699919799/
- **Linux Real-Time**: https://wiki.linuxfoundation.org/realtime/

---

## 🗂️ Fichiers Locaux

### Projet 1: Sensors
```
sensors/
├── temperature_sensor_reader.py    (420 lignes)
├── visualize_sensor_data.py        (200 lignes)
├── PROJECT_TEMPERATURE_SENSOR.md   (Guide complet)
└── requirements.txt                (Dépendances)
```

### Documentation
```
├── PROJETS_PRATIQUES.md           (5 projets)
├── RESSOURCES_LIENS.md            (Ce fichier)
├── CPS_LEARNING_GUIDE.md          (Guide maître)
└── README.md                       (Vue d'ensemble)
```

---

## 💻 Commandes Rapides

### Setup Sensor Project
```bash
cd sensors
pip install -r requirements.txt
python temperature_sensor_reader.py
python visualize_sensor_data.py sensor_data_*.csv --stats
```

### Setup Robotics Project (À créer)
```bash
pip install numpy scipy matplotlib
pip install pybullet
python robotics/arm_simulator.py
```

### Setup IoT Project (À créer)
```bash
pip install paho-mqtt flask
python iot/mqtt_controller.py
```

---

## 📅 Plan d'Apprentissage Recommandé

### Semaine 1-2: Sensors
- Vidéos: DHT22 + Data Logging + Matplotlib (1.5h)
- Projet: Temperature monitoring (2h)
- Extension: Multi-sensors (2h)

### Semaine 3-4: Robotics
- Cours: Kinematics basics (2h)
- Vidéos: Forward/Inverse K (1h)
- Projet: Arm simulator (3h)

### Semaine 5-6: Autonomous Vehicles
- Simulateur: CARLA setup (1h)
- Cours: Path planning (2h)
- Projet: Simple controller (3h)

### Semaine 7-8: IoT
- Protocole: MQTT fundamentals (1h)
- Platform: Home Assistant (2h)
- Projet: Smart home system (3h)

### Semaine 9-10: Security
- Outils: Scapy + Snort (2h)
- Vidéos: Packet analysis (1.5h)
- Projet: IDS system (3h)

### Semaine 11-12: Real-Time
- Concepts: Scheduling (2h)
- Cours: FreeRTOS (2h)
- Projet: Scheduler implementation (3h)

---

## ✅ Checklist des Ressources

- [ ] Vidéos DHT22 regardées
- [ ] Pandas tutorial complété
- [ ] Projet 1 exécuté avec succès
- [ ] Kinematics concepts compris
- [ ] CARLA simulator installé
- [ ] MQTT broker configuré
- [ ] Scapy testé en local
- [ ] FreeRTOS exploration initiée

---

## 🎓 Certifications Connexes

- **Arduino Certified Associate**
- **AWS IoT Specialty**
- **Cisco CCNA (Network)**
- **IEEE Computer Society Certificates**

---

## 🤝 Communautés

- **Robot Operating System (ROS)**: https://discourse.ros.org/
- **Arduino Forum**: https://forum.arduino.cc/
- **Stack Exchange - Robotics**: https://robotics.stackexchange.com/
- **Home Assistant Community**: https://community.home-assistant.io/

---

**Dernière mise à jour:** 30 Juin 2026

📌 **Conseil:** Commencez par Projet 1 (Sensors). C'est la fondation pour tous les autres!
