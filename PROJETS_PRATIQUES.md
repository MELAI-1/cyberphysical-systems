# 🚀 CPS Learning Roadmap - 5 Projets Pratiques avec Ressources

Un guide complet pour apprendre les **Cyber-Physical Systems** à travers 5 projets concrets avec vidéos, tutoriels et ressources.

---

## 📋 Table des Matières

1. [Vue d'ensemble](#-vue-densemble)
2. [5 Projets Pratiques](#-5-projets-pratiques)
3. [Ressources Complètes par Domaine](#-ressources-complètes-par-domaine)
4. [Roadmap d'Apprentissage](#-roadmap-dapprentissage)

---

## 🎯 Vue d'ensemble

### Qu'est-ce qu'un Cyber-Physical System?

Un CPS est l'intégration de **calcul, réseaux et processus physiques** :
- 🌡️ **Capteurs** - Mesurer le monde physique
- 🖥️ **Traitement** - Analyser et décider
- ⚙️ **Actionneurs** - Agir sur le monde physique

### 13 Domaines CPS

| Domaine | Difficulté | Secteur | Lien |
|---------|-----------|---------|------|
| 🌡️ **Sensors** | ⭐ | IoT, Mesure | [Voir](#-projet-1--système-de-monitoring-température) |
| 🤖 **Robotics** | ⭐⭐⭐ | Automatisation | [Voir](#-projet-2--bras-robotique-simulation) |
| 🚗 **Autonomous Vehicles** | ⭐⭐⭐⭐ | Transport | [Voir](#-projet-3--voiture-autonome-simulator) |
| 🏠 **IoT** | ⭐⭐ | Domotique | [Voir](#-projet-4--système-iot-smart-home) |
| 🔒 **Network Security** | ⭐⭐⭐ | Cybersécurité | [Voir](#-projet-5--intrusion-detection-system) |
| ⚡ **Real-Time Systems** | ⭐⭐⭐⭐ | Critique temps-réel | [Voir](#-projet-6--système-temps-réel-scheduling) |
| 🏭 **Industrial Control** | ⭐⭐⭐ | Industrie 4.0 | Plus tard |
| 📡 **Edge Computing** | ⭐⭐⭐ | Cloud Edge | Plus tard |
| 🌐 **Connectivity** | ⭐⭐ | Protocoles | Plus tard |
| ⚡ **Smart Grids** | ⭐⭐⭐⭐ | Énergie | Plus tard |
| 🏥 **Medical Devices** | ⭐⭐⭐⭐ | Santé | Plus tard |
| 🏙️ **Smart Cities** | ⭐⭐⭐⭐ | Urbain | Plus tard |

---

## 🔨 5 Projets Pratiques

### 🌡️ **PROJET 1 – Système de Monitoring Température**

**Difficulté:** ⭐ Débutant  
**Temps:** 2-3 heures  
**Domaine:** Sensors  

#### 📖 Description

Créer un système complet de monitoring de température avec :
- ✅ Acquisition de données (simulation + réel)
- ✅ Logging CSV/JSON avec timestamps
- ✅ Statistiques temps-réel
- ✅ Visualisation avec graphiques
- ✅ Alertes de seuil

#### 💻 Architecture

```
┌─────────────┐      ┌──────────────┐      ┌───────────┐
│   Capteur   │─────▶│  Data Logger │─────▶│  Storage  │
│ (DHT22)     │      │  (Python)    │      │ (CSV/JSON)│
└─────────────┘      └──────────────┘      └───────────┘
                            │
                            ▼
                      ┌─────────────┐
                      │ Visualizer  │
                      │ (Matplotlib)│
                      └─────────────┘
```

#### 📂 Fichiers Fournis

✅ [temperature_sensor_reader.py](./sensors/temperature_sensor_reader.py)  
✅ [visualize_sensor_data.py](./sensors/visualize_sensor_data.py)  
✅ [PROJECT_TEMPERATURE_SENSOR.md](./sensors/PROJECT_TEMPERATURE_SENSOR.md)

#### 🚀 Démarrage Rapide

```bash
cd sensors
pip install -r requirements.txt
python temperature_sensor_reader.py
python visualize_sensor_data.py sensor_data_*.csv --stats
```

#### 📚 Ressources d'Apprentissage

**Vidéos YouTube :**
- [DHT22 Sensor Tutorial](https://www.youtube.com/watch?v=DI_eXZhTYhE) - 15 min
- [Python Data Logging](https://www.youtube.com/watch?v=A9pxSsS5U-4) - 20 min
- [Matplotlib Visualization](https://www.youtube.com/watch?v=UO98lJQ3QGY) - 30 min

**Tutoriels Texte :**
- [Adafruit DHT Library](https://learn.adafruit.com/dht/python)
- [CSV Module Python](https://docs.python.org/3/library/csv.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

**Concepts à Maîtriser :**
- Classes Python OOP
- File I/O et formats
- Statistiques descriptives
- Séries temporelles

---

### 🤖 **PROJET 2 – Bras Robotique Simulation**

**Difficulté:** ⭐⭐⭐ Intermédiaire  
**Temps:** 4-6 heures  
**Domaine:** Robotics  

#### 📖 Description

Simuler et contrôler un **bras robotique 3-DOF** avec :
- ✅ Cinématique directe (Forward Kinematics)
- ✅ Cinématique inverse (Inverse Kinematics)
- ✅ Trajectoire planifiée
- ✅ Visualisation 3D
- ✅ Contrôle en temps-réel

#### 💻 Architecture

```
┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  Trajectoire │────▶│ Kinematics  │────▶│   Simulation │
│   (Points)   │     │ (FK + IK)   │     │   (Pygame)   │
└──────────────┘     └─────────────┘     └──────────────┘
                            ▲                     │
                            │                     │
                     ┌──────┴─────────┐           │
                     │  Config Joints │◀──────────┘
                     └────────────────┘
```

#### 💻 Code Starter

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class RoboticArm:
    def __init__(self, link_lengths=[1.0, 0.8, 0.6]):
        self.link_lengths = link_lengths
        self.dof = len(link_lengths)
    
    def forward_kinematics(self, angles):
        """Calculer position end-effector"""
        x, y, z = 0, 0, 0
        for i, (length, angle) in enumerate(zip(self.link_lengths, angles)):
            x += length * np.cos(angle)
            y += length * np.sin(angle)
        return x, y, z
    
    def visualize(self, angles):
        """Afficher le bras"""
        positions = [self.forward_kinematics(angles)]
        x, y, z = zip(*positions)
        plt.plot(x, y)
        plt.show()

# Utilisation
arm = RoboticArm()
angles = [np.pi/4, np.pi/3, np.pi/6]
arm.visualize(angles)
```

#### 📚 Ressources d'Apprentissage

**Vidéos :**
- [Robotic Arm Kinematics](https://www.youtube.com/watch?v=RA2aHRFGxT0) - 45 min
- [Forward Kinematics Explained](https://www.youtube.com/watch?v=8jnxIbJxe4Q) - 20 min
- [ROS Robotics Basics](https://www.youtube.com/watch?v=v9Rvg1b4lYg) - 60 min

**Cours :**
- [Introduction to Robotics](https://ocw.mit.edu/courses/2-12-introduction-to-robotics/) - MIT
- [Robot Dynamics](https://www.coursera.org/learn/robot-dynamics) - Coursera

**Bibliothèques :**
- [PyBullet](https://pybullet.org/) - Simulation physique
- [ROS](https://www.ros.org/) - Robot Operating System

---

### 🚗 **PROJET 3 – Voiture Autonome Simulator**

**Difficulté:** ⭐⭐⭐⭐ Avancé  
**Temps:** 6-8 heures  
**Domaine:** Autonomous Vehicles  

#### 📖 Description

Développer un **contrôleur de véhicule autonome** avec :
- ✅ Modèle de véhicule cinématique
- ✅ Capteurs simulés (LiDAR, caméra)
- ✅ Détection d'obstacles
- ✅ Planification de trajectoire
- ✅ Contrôle temps-réel

#### 💻 Architecture

```
┌─────────────────┐
│   Simulation    │
│   (Véhicule)    │
└────────┬────────┘
         │
    ┌────┴─────┐
    │           │
┌───▼───┐  ┌───▼────┐
│ LiDAR │  │ Caméra  │
└───┬───┘  └───┬────┘
    │          │
    └────┬─────┘
         │
    ┌────▼──────────────┐
    │ Perception Module │
    └────┬──────────────┘
         │
    ┌────▼──────────────┐
    │ Planning Module   │
    └────┬──────────────┘
         │
    ┌────▼──────────────┐
    │ Control Module    │
    └───────────────────┘
```

#### 💻 Code Starter

```python
import numpy as np

class VehicleModel:
    def __init__(self, wheelbase=2.7):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.wheelbase = wheelbase
        self.velocity = 0.0
    
    def update(self, v, delta, dt):
        """
        Mise à jour kinématique
        v: vitesse
        delta: angle de braquage
        dt: pas de temps
        """
        self.velocity = v
        self.theta += (v / self.wheelbase) * np.tan(delta) * dt
        self.x += v * np.cos(self.theta) * dt
        self.y += v * np.sin(self.theta) * dt
    
    def get_state(self):
        return np.array([self.x, self.y, self.theta, self.velocity])

class LiDARSensor:
    def __init__(self, range_max=100.0, num_rays=360):
        self.range_max = range_max
        self.num_rays = num_rays
    
    def scan(self, obstacles, vehicle_pos):
        """Simuler scan LiDAR"""
        ranges = np.ones(self.num_rays) * self.range_max
        # Calculer distances aux obstacles
        return ranges

# Utilisation
vehicle = VehicleModel()
lidar = LiDARSensor()

for t in range(1000):
    v, delta = 5.0, 0.1  # vitesse, braquage
    vehicle.update(v, delta, dt=0.01)
    ranges = lidar.scan(obstacles=[], vehicle_pos=vehicle.get_state())
```

#### 📚 Ressources d'Apprentissage

**Vidéos :**
- [Autonomous Vehicles Course](https://www.youtube.com/watch?v=LQsNueLvXcs) - 3h
- [CARLA Simulator Tutorial](https://www.youtube.com/watch?v=7Q0jNFfECmM) - 30 min
- [Path Planning Algorithms](https://www.youtube.com/watch?v=sL3b2V7zNMw) - 45 min

**Simulateurs :**
- [CARLA Simulator](http://carla.org/) - Simulation urbaine
- [Apollo Autonomous Driving](https://apollo.auto/) - Plateforme complète

**Concepts :**
- Cinématique de véhicule
- Planification de trajectoire (RRT, A*)
- Détection d'obstacles
- Contrôle PID/LQR

---

### 🏠 **PROJET 4 – Système IoT Smart Home**

**Difficulté:** ⭐⭐ Intermédiaire  
**Temps:** 3-4 heures  
**Domaine:** IoT  

#### 📖 Description

Construire une **maison intelligente miniature** avec :
- ✅ Capteurs multiples (température, lumière, humidité)
- ✅ Actionneurs (lampes, climatisation)
- ✅ Communication MQTT
- ✅ Dashboard web
- ✅ Automations et scénarios

#### 💻 Architecture

```
┌──────────────┐
│   Capteurs   │
│ (DHT22, LDR) │
└────────┬─────┘
         │
    ┌────▼─────────────────┐
    │  MQTT Broker         │
    │ (Mosquitto/HiveMQ)   │
    └────┬─────────────────┘
         │
    ┌────┴─────────┬──────────────┐
    │              │              │
┌───▼────┐  ┌─────▼──┐  ┌────────▼──┐
│ Node-RED│  │ Python │  │ Dashboard │
│ (Logic) │  │(Broker)│  │ (Web UI)  │
└────┬────┘  └───┬────┘  └───┬──────┘
     │           │            │
     └───────────┴────────────┘
            │
      ┌─────▼────────┐
      │  Actionneurs │
      │ (Relais, LED)│
      └──────────────┘
```

#### 💻 Code Starter

```python
import paho.mqtt.client as mqtt
import json
import time

class SmartHome:
    def __init__(self, broker="localhost"):
        self.client = mqtt.Client()
        self.broker = broker
        self.devices = {}
        
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
    
    def on_connect(self, client, userdata, flags, rc):
        print(f"Connecté au broker (code: {rc})")
        self.client.subscribe("home/+/+")
    
    def on_message(self, client, userdata, msg):
        """Traiter messages MQTT"""
        topic = msg.topic
        payload = json.loads(msg.payload)
        print(f"Message reçu: {topic} = {payload}")
        
        # Traiter automations
        self._process_automation(topic, payload)
    
    def _process_automation(self, topic, data):
        """Appliquer automations"""
        if topic == "home/bedroom/temperature":
            temp = data['value']
            if temp > 28:
                self.set_ac(enabled=True, temp=24)
    
    def set_ac(self, enabled, temp):
        """Contrôler climatisation"""
        msg = {"enabled": enabled, "target": temp}
        self.client.publish("home/ac/control", json.dumps(msg))
    
    def connect(self):
        self.client.connect(self.broker)
        self.client.loop_start()
    
    def run_forever(self):
        while True:
            time.sleep(1)

# Utilisation
home = SmartHome()
home.connect()
home.run_forever()
```

#### 📚 Ressources d'Apprentissage

**Vidéos :**
- [MQTT Tutorial for IoT](https://www.youtube.com/watch?v=E-VY2m2u-PI) - 40 min
- [Home Assistant Setup](https://www.youtube.com/watch?v=JOoRt0rKAns) - 30 min
- [Node-RED Dashboard](https://www.youtube.com/watch?v=2nfCVhqXRQI) - 25 min

**Plateformes :**
- [Home Assistant](https://www.home-assistant.io/) - Domotique complète
- [Node-RED](https://nodered.org/) - Automation visuelle
- [MQTT.org](https://mqtt.org/) - Standard MQTT

**Composants :**
- ESP32/Arduino
- Capteurs DHT22, BMP280
- Relais et LED
- Broker MQTT

---

### 🔒 **PROJET 5 – Intrusion Detection System (IDS)**

**Difficulté:** ⭐⭐⭐ Intermédiaire  
**Temps:** 4-5 heures  
**Domaine:** Network Security  

#### 📖 Description

Développer un **système de détection d'intrusion** avec :
- ✅ Capture et analyse de packets réseau
- ✅ Détection d'anomalies
- ✅ Classification d'attaques
- ✅ Alertes temps-réel
- ✅ Dashboard de monitoring

#### 💻 Architecture

```
┌─────────────────┐
│  Trafic Réseau  │
└────────┬────────┘
         │
    ┌────▼──────────────┐
    │ Packet Capture    │
    │ (Scapy/tcpdump)   │
    └────┬──────────────┘
         │
    ┌────▼──────────────┐
    │ Feature Extraction│
    │ (Protocol, Port)  │
    └────┬──────────────┘
         │
    ┌────▼──────────────┐
    │ Anomaly Detection │
    │ (ML/Rules)        │
    └────┬──────────────┘
         │
    ┌────▼──────────────┐
    │ Alert & Log       │
    └───────────────────┘
```

#### 💻 Code Starter

```python
from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import json
from datetime import datetime

class IDS:
    def __init__(self, threshold=100):
        self.traffic = defaultdict(int)
        self.threshold = threshold
        self.alerts = []
    
    def packet_callback(self, packet):
        """Callback pour chaque packet"""
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            
            # Déterminer protocole et port
            protocol = "Unknown"
            port = None
            
            if TCP in packet:
                protocol = "TCP"
                port = packet[TCP].dport
            elif UDP in packet:
                protocol = "UDP"
                port = packet[UDP].dport
            
            # Compter connections
            flow_key = f"{src_ip}:{dst_ip}:{protocol}:{port}"
            self.traffic[flow_key] += 1
            
            # Vérifier anomalies
            self._check_anomalies(flow_key, src_ip, dst_ip, port)
    
    def _check_anomalies(self, flow_key, src, dst, port):
        """Détecter anomalies"""
        count = self.traffic[flow_key]
        
        # Port scan detection
        if port and port < 1024:
            if count > self.threshold:
                self._alert(
                    f"Port scan detected from {src} to {dst}:{port}",
                    severity="HIGH"
                )
        
        # DDoS detection
        if count > self.threshold * 10:
            self._alert(
                f"Potential DDoS: {flow_key}",
                severity="CRITICAL"
            )
    
    def _alert(self, message, severity="MEDIUM"):
        """Générer alerte"""
        alert = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "severity": severity
        }
        self.alerts.append(alert)
        print(f"[{severity}] {message}")
    
    def start_sniffing(self, interface=None, packet_count=0):
        """Commencer à sniffer le réseau"""
        print("Démarrage IDS...")
        sniff(
            iface=interface,
            prn=self.packet_callback,
            store=False,
            count=packet_count
        )
    
    def get_alerts(self):
        return self.alerts

# Utilisation
ids = IDS(threshold=50)
ids.start_sniffing()
```

#### 📚 Ressources d'Apprentissage

**Vidéos :**
- [Network Packet Analysis](https://www.youtube.com/watch?v=qdNvXi1wVyE) - 45 min
- [Snort IDS Tutorial](https://www.youtube.com/watch?v=LJ6v4TsHDdU) - 40 min
- [Suricata IDS Rules](https://www.youtube.com/watch?v=ZD-VXAJlqRQ) - 30 min

**Outils :**
- [Scapy](https://scapy.readthedocs.io/) - Packet manipulation
- [Snort](https://www.snort.org/) - IDS classique
- [Suricata](https://suricata.io/) - IDS moderne
- [Zeek](https://zeek.org/) - Network framework

**Concepts :**
- Protocol analysis
- Anomaly detection
- Machine learning for security
- Network forensics

---

### ⚡ **PROJET 6 – Système Temps-Réel: Scheduler**

**Difficulté:** ⭐⭐⭐⭐ Avancé  
**Temps:** 5-7 heures  
**Domaine:** Real-Time Systems  

#### 📖 Description

Implémenter un **scheduler temps-réel** avec :
- ✅ Tâches périodiques
- ✅ Priorités (Rate Monotonic Scheduling)
- ✅ Garanties temps-réel
- ✅ Analyse de planificabilité
- ✅ Simulation avec visualisation

#### 💻 Code Starter

```python
import heapq
import time
from dataclasses import dataclass
from typing import List, Callable

@dataclass
class Task:
    name: str
    period: float
    deadline: float
    execution_time: float
    priority: int
    function: Callable
    next_activation: float = 0.0

class RealtimeScheduler:
    def __init__(self):
        self.tasks: List[Task] = []
        self.current_time = 0.0
        self.schedule_log = []
    
    def add_task(self, task: Task):
        """Ajouter une tâche"""
        self.tasks.append(task)
        self.tasks.sort(key=lambda t: t.priority, reverse=True)
    
    def is_schedulable(self) -> bool:
        """Vérifier si ensemble de tâches est planifiable"""
        # Utiliser test d'utilisation CPU
        utilization = sum(t.execution_time / t.period for t in self.tasks)
        n = len(self.tasks)
        
        # Test Liu-Layland
        bound = n * (2**(1/n) - 1)
        return utilization <= bound
    
    def schedule(self, duration: float):
        """Exécuter scheduler"""
        end_time = self.current_time + duration
        
        while self.current_time < end_time:
            # Trouver tâche prêt à exécuter
            ready_tasks = [t for t in self.tasks 
                          if t.next_activation <= self.current_time]
            
            if not ready_tasks:
                # Idle
                self.current_time += 0.001
                continue
            
            # Sélectionner tâche prioritaire
            task = max(ready_tasks, key=lambda t: t.priority)
            
            # Exécuter tâche
            self.schedule_log.append({
                'task': task.name,
                'start': self.current_time,
                'duration': task.execution_time
            })
            
            task.function()
            self.current_time += task.execution_time
            task.next_activation = self.current_time + task.period
    
    def visualize_schedule(self):
        """Afficher diagramme de Gantt"""
        # À implémenter avec matplotlib
        pass

# Utilisation
scheduler = RealtimeScheduler()

def task_a():
    print("Tâche A exécutée")

def task_b():
    print("Tâche B exécutée")

scheduler.add_task(Task(
    name="Task A",
    period=10,
    deadline=10,
    execution_time=3,
    priority=2,
    function=task_a
))

scheduler.add_task(Task(
    name="Task B",
    period=15,
    deadline=15,
    execution_time=4,
    priority=1,
    function=task_b
))

if scheduler.is_schedulable():
    print("✅ Ensemble planifiable")
    scheduler.schedule(100)
else:
    print("❌ Impossible à planifier")
```

#### 📚 Ressources d'Apprentissage

**Cours :**
- [Real-Time Systems (CMU)](http://www.cs.cmu.edu/afs/cs/academic/class/15-445-f21/www/) - Université
- [Embedded Systems with Real-Time](https://www.coursera.org/learn/real-time-operating-systems)

**Vidéos :**
- [Rate Monotonic Scheduling](https://www.youtube.com/watch?v=e-JRyVDXqJ8) - 25 min
- [FreeRTOS Tutorial](https://www.youtube.com/watch?v=tKpDEF3f1u4) - 50 min

**Concepts :**
- Rate Monotonic Scheduling
- Deadline Monotonic Scheduling
- WCET (Worst-Case Execution Time)
- Schedulability analysis

---

## 📚 Ressources Complètes par Domaine

### 🌡️ Sensors

**Vidéos :**
- [Sensors 101](https://www.youtube.com/playlist?list=PLBCeHRBYCVgRgaCSyIqYnqJlvPMbZc3VL)
- [IoT Sensors](https://www.youtube.com/watch?v=b2eI7z6Z9EQ)

**PDFs :**
- [Sensor Types Guide](https://www.ti.com/lit/an/sloa030b/sloa030b.pdf) - TI
- [Signal Conditioning](https://www.analog.com/en/resources/technical-articles/signal-conditioning.html)

**Documentation :**
- [Adafruit Sensors](https://learn.adafruit.com/)
- [Arduino Sensor Guide](https://docs.arduino.cc/learn)

---

### 🤖 Robotics

**Ressources :**
- [ROS Official](https://www.ros.org/install/)
- [PyBullet Docs](https://pybullet.org/wordpress/)
- [Robotics Stack Exchange](https://robotics.stackexchange.com/)

**Cours :**
- [MIT Robotics](https://ocw.mit.edu/search/?d=Robotics&s=most_recent) (MIT OpenCourseWare)
- [Stanford Robotics](https://robotics.stanford.edu/courses/)

---

### 🚗 Autonomous Vehicles

**Ressources :**
- [CARLA Docs](https://carla.readthedocs.io/)
- [Apollo Documentation](https://github.com/ApolloAuto/apollo)
- [Waymo Datasets](https://waymo.com/open/)

**Cours :**
- [Autonomous Driving (Udacity)](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013)
- [Berkeley AV](https://deepdrive.berkeley.edu/)

---

### 🏠 IoT

**Ressources :**
- [Home Assistant Docs](https://www.home-assistant.io/docs/)
- [Node-RED](https://nodered.org/docs/)
- [MQTT.org](https://mqtt.org/)

**Projets :**
- [ESPHome](https://esphome.io/)
- [Tasmota](https://tasmota.github.io/docs/)

---

### 🔒 Network Security

**Ressources :**
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [Snort Rules](https://www.snort.org/rules)
- [Suricata Docs](https://suricata.readthedocs.io/)

**Cours :**
- [Cybersecurity Basics (Coursera)](https://www.coursera.org/learn/cybersecurity-basics)
- [Network Security (edX)](https://www.edx.org/course/network-security)

---

### ⚡ Real-Time Systems

**Ressources :**
- [FreeRTOS](https://www.freertos.org/)
- [RT-Thread](https://github.com/rt-thread/rt-thread)
- [RTOS Comparison](https://www.embedded.com/compare-operating-systems/)

**Documentation :**
- [POSIX Real-Time](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)
- [QNX RTOS](https://www.qnx.com/developers/)

---

## 🗺️ Roadmap d'Apprentissage

### **Phase 1: Fondations (Semaine 1-2)**
```
[Semaine 1]
├─ Projet 1: Sensors (Température)
├─ Apprendre Python OOP
├─ Maîtriser data logging
└─ Intro visualisation

[Semaine 2]
├─ Étendre Projet 1 (multi-capteurs)
├─ Apprendre I/O et fichiers
├─ Comprendre statistiques
└─ Consolidation
```

### **Phase 2: Systèmes (Semaine 3-4)**
```
[Semaine 3]
├─ Projet 4: IoT Smart Home
├─ Apprendre MQTT
├─ Automations basiques
└─ Dashboard web

[Semaine 4]
├─ Projet 2: Robotics (simulation)
├─ Apprendre cinématique
├─ Visualisation 3D
└─ Planification simple
```

### **Phase 3: Avancé (Semaine 5-6)**
```
[Semaine 5]
├─ Projet 3: Autonomous Vehicles
├─ Perception et planning
├─ Contrôle temps-réel
└─ Simulation CARLA

[Semaine 6]
├─ Projet 5: Network Security
├─ Analyse de trafic
├─ Détection anomalies
└─ ML for security
```

### **Phase 4: Spécialisation (Semaine 7-8)**
```
[Semaine 7-8]
├─ Projet 6: Real-Time Systems
├─ Scheduler temps-réel
├─ Analyse planificabilité
└─ Intégration matériel
```

---

## 🎯 Checklist de Progression

### Projet 1: Sensors ✅
- [ ] Code exécutable
- [ ] Données CSV générées
- [ ] Graphiques affichés
- [ ] Statistiques correctes
- [ ] Multi-capteurs (extension)

### Projet 2: Robotics ⏳
- [ ] Cinématique directe
- [ ] Cinématique inverse
- [ ] Visualisation 3D
- [ ] Trajectoires planifiées
- [ ] Contrôle interactive

### Projet 3: Autonomous Vehicles ⏳
- [ ] Modèle véhicule
- [ ] Capteurs simulés
- [ ] Détection obstacles
- [ ] Planification chemin
- [ ] Contrôle temps-réel

### Projet 4: IoT ⏳
- [ ] Broker MQTT
- [ ] Capteurs multiples
- [ ] Automations
- [ ] Dashboard
- [ ] Alertes

### Projet 5: Security ⏳
- [ ] Capture packets
- [ ] Extraction features
- [ ] Détection anomalies
- [ ] Alertes
- [ ] Dashboard monitoring

### Projet 6: Real-Time ⏳
- [ ] Scheduler basique
- [ ] Priorités
- [ ] Analyse planificabilité
- [ ] Simulation
- [ ] Diagramme Gantt

---

## 📞 Support et Questions

**Ressources :**
- GitHub Issues: [cyberphysical-systems Issues](https://github.com/MELAI-1/cyberphysical-systems/issues)
- Stack Exchange: [robotics.stackexchange.com](https://robotics.stackexchange.com/)
- Forums: [ROS Discourse](https://discourse.ros.org/)

**Documents Connexes :**
- [CPS_LEARNING_GUIDE.md](./CPS_LEARNING_GUIDE.md) - Guide complet
- [README.md](./README.md) - Vue d'ensemble
- [sensors/README.md](./sensors/README.md) - Projet 1 détaillé

---

**Happy Learning! 🚀**

Prochaine étape → **Choisir un projet et commencer!**

```bash
cd cyberphysical-systems
python sensors/temperature_sensor_reader.py
```
