# 📚 CPS Learning Platform - Index Complet

> **Cyber-Physical Systems**: Où le calcul rencontre le monde physique  
> Une plateforme complète d'apprentissage avec **5 projets concrets**, **ressources vidéo**, et **guides progressifs**.

---

## 🎯 Commencer Ici

### ⚡ Quick Start (2 minutes)
```bash
# 1. Clone le projet
git clone https://github.com/MELAI-1/cyberphysical-systems.git
cd cyberphysical-systems

# 2. Setup automatique
bash setup.sh

# 3. Exécuter Projet 1
cd sensors
python temperature_sensor_reader.py
```

### 📖 Choisir son Chemin d'Apprentissage

```
┌─────────────────────────────────────────────────────────────┐
│  NIVEAU 1: DÉBUTANT                                         │
│  ⭐ Sensors (Température Monitoring) - 2h                   │
│  → Apprendre: Python OOP, Data Logging, Visualisation     │
│  → Ressources: PROJETS_PRATIQUES.md + Videos YouTube      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  NIVEAU 2: INTERMÉDIAIRE                                    │
│  ⭐⭐ Robotics (Bras Robotique) - 4h                        │
│  ⭐⭐ IoT (Domotique) - 3h                                  │
│  → Apprendre: Cinématique, MQTT, Automations             │
│  → Ressources: Cours MIT, Platforms (ROS, Home Assistant) │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  NIVEAU 3: AVANCÉ                                           │
│  ⭐⭐⭐ Autonomous Vehicles - 6h                            │
│  ⭐⭐⭐ Network Security (IDS) - 4h                         │
│  ⭐⭐⭐⭐ Real-Time Systems - 5h                            │
│  → Apprendre: Perception, Planning, Scheduling            │
│  → Ressources: Simulateurs (CARLA), Papers, Datasets      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Structure du Projet

```
cyberphysical-systems/
│
├── 📄 INDEX.md (CE FICHIER)
│   └─ Carte d'accueil complète
│
├── 📄 PROJETS_PRATIQUES.md ⭐⭐⭐ À LIRE EN PREMIER
│   └─ 5 projets concrets avec code starter
│      • Projet 1: Sensors - Temperature Monitoring
│      • Projet 2: Robotics - Bras Robotique Simulation
│      • Projet 3: Autonomous Vehicles - CARLA Simulator
│      • Projet 4: IoT - Smart Home System
│      • Projet 5: Network Security - IDS
│      • Projet 6: Real-Time Systems - Scheduler
│
├── 📄 RESSOURCES_LIENS.md ⭐⭐⭐ TOUS LES LIENS
│   └─ PDFs, Vidéos YouTube, Tutoriels, Cours Universitaires
│      • 50+ liens directs
│      • Organisés par domaine
│      • Ressources gratuites et payantes
│
├── 📄 CPS_LEARNING_GUIDE.md (Complet, 3500+ lignes)
│   └─ Guide de progression 3 niveaux (Beginner → Intermediate → Advanced)
│      • 13 domaines CPS
│      • 16 READMEs avec roadmaps
│      • Ressources et concepts par niveau
│
├── 🎬 manim_animations/ (Vidéo Manim)
│   └── presentation/
│       └── CybersecurityAndCPS.mp4 (Vidéo éducative 5 min)
│           └─ Vue d'ensemble du CPS + Cybersécurité
│
├── 🌡️ sensors/ (PROJET 1 - PRÊT À EXÉCUTER)
│   ├── temperature_sensor_reader.py (420 lignes, code complet)
│   ├── visualize_sensor_data.py (200 lignes, graphiques)
│   ├── PROJECT_TEMPERATURE_SENSOR.md (guide détaillé)
│   ├── requirements.txt (dépendances)
│   └── sensor_data_*.csv (données générées)
│
├── 🤖 robotics/ (Placeholder - À créer)
├── 🚗 autonomous-vehicles/ (Placeholder - À créer)
├── 🏠 iot/ (Placeholder - À créer)
├── 🔒 network-security/ (Placeholder - À créer)
├── ⚡ real-time-systems/ (Placeholder - À créer)
│
├── 🔧 setup.sh (Script d'installation automatique)
├── 📦 requirements.txt (Dépendances globales - À créer)
└── 📄 README.md (Vue d'ensemble du repo)
```

---

## 🗺️ Roadmap d'Apprentissage - Semaine par Semaine

### Semaine 1-2: DÉBUTANT - Fondations
| Jour | Activité | Temps | Ressources |
|------|----------|-------|-----------|
| **1-2** | Lire PROJETS_PRATIQUES.md | 1h | 📄 PROJETS_PRATIQUES.md |
| **3-4** | Regarder vidéos Sensors (DHT22, Matplotlib) | 1.5h | 📹 YouTube links |
| **5-6** | Exécuter Projet 1 | 2h | 💻 sensors/ |
| **7-8** | Étendre Projet 1 (multi-capteurs) | 2h | 💻 sensors/ + 📄 docs |
| **9-10** | Consolider et tester | 2h | ✅ Local testing |

**Résultat:** ✅ Système de monitoring température qui fonctionne

---

### Semaine 3-4: INTERMÉDIAIRE - Systèmes
| Jour | Activité | Temps | Ressources |
|------|----------|-------|-----------|
| **11-12** | Robotics Kinematics (cours + vidéos) | 2h | 📹 MIT OCW + YouTube |
| **13-14** | Implémenter Projet 2 starter | 2h | 💻 robotics/arm_simulator.py |
| **15-16** | Projet 4: IoT Setup (MQTT + Home Assistant) | 2h | 🏠 iot/ + 📹 setup videos |
| **17-18** | Créer automations simples | 2h | 💻 Node-RED |
| **19-20** | Tester et déboguer | 1h | ✅ Testing |

**Résultat:** ✅ Bras robotique simulé + Maison intelligente basique

---

### Semaine 5-6: AVANCÉ - Intégration
| Jour | Activité | Temps | Ressources |
|------|----------|-------|-----------|
| **21-22** | Setup CARLA simulator | 1h | 🚗 carla.org |
| **23-24** | Autonomous Vehicles basics | 2h | 📹 CARLA tutorials |
| **25-26** | Implémenter Projet 3 | 3h | 💻 autonomous-vehicles/ |
| **27-28** | Network Security (Scapy + Snort) | 2h | 📹 packet analysis videos |
| **29-30** | Implémenter Projet 5 (IDS) | 3h | 💻 network-security/ |

**Résultat:** ✅ Voiture autonome simulée + IDS en production

---

### Semaine 7-8: EXPERT - Temps-Réel
| Jour | Activité | Temps | Ressources |
|------|----------|-------|-----------|
| **31-32** | Real-Time Systems theory | 2h | 📚 Cours Coursera |
| **33-34** | FreeRTOS ou scheduler local | 2h | 💻 real-time-systems/ |
| **35-36** | Implémenter Projet 6 | 3h | 💻 scheduler_implementation.py |
| **37-40** | Intégration et optimisation | 3h | 🔧 Performance tuning |

**Résultat:** ✅ Système temps-réel avec garanties de planification

---

## 🎓 Par Où Commencer?

### 🟢 Je suis complètement débutant
1. Lire **PROJETS_PRATIQUES.md** (30 min)
2. Exécuter **Projet 1** (1-2h)
3. Regarder les vidéos recommandées (1-2h)
4. Modifier le code et expérimenter (2-3h)
5. Progresser vers Projet 2

### 🟡 J'ai des notions de programmation
1. Consulter **RESSOURCES_LIENS.md** pour trouver ressources intéressantes
2. Choisir **Projet 2, 3 ou 4** selon intérêt
3. Implémenter en parallèle avec d'autres projets
4. Progresser rapidement vers niveau AVANCÉ

### 🔴 Je suis un développeur expérimenté
1. Lire **CPS_LEARNING_GUIDE.md** pour vue d'ensemble
2. Ignorer Projet 1, commencer par Projet 3 (Autonomous Vehicles)
3. Approfondir concepts avancés (CARLA, Apollo, ROS)
4. Créer vos propres projets au-delà des 5 proposés

---

## 📚 Les 5 Projets en Détail

### Projet 1: 🌡️ Température Monitoring (PRÊT À EXÉCUTER)
```
Difficulté: ⭐ Débutant
Temps: 2-3h
État: ✅ 100% Complet
Fichiers: sensors/temperature_sensor_reader.py

Objectifs:
✅ Sensor abstraction
✅ Data logging (CSV + JSON)
✅ Statistics calculation
✅ Visualization (Matplotlib)
✅ Real-time monitoring

Commande:
cd sensors && python temperature_sensor_reader.py
```

### Projet 2: 🤖 Bras Robotique (À CRÉER)
```
Difficulté: ⭐⭐⭐ Intermédiaire
Temps: 4-6h
État: 📝 Code starter + guide
Fichiers: robotics/arm_simulator.py (À créer)

Objectifs:
□ Forward Kinematics
□ Inverse Kinematics
□ 3D Visualization
□ Trajectory Planning
□ Interactive Control

Ressources:
- MIT Kinematics Course
- PyBullet Physics Engine
- ROS Tutorials
```

### Projet 3: 🚗 Voiture Autonome (À CRÉER)
```
Difficulté: ⭐⭐⭐⭐ Avancé
Temps: 6-8h
État: 📝 Guide + starter code
Fichiers: autonomous-vehicles/carla_controller.py (À créer)

Objectifs:
□ Vehicle Kinematics
□ LiDAR Simulation
□ Obstacle Detection
□ Path Planning (A*, RRT)
□ Real-time Control

Ressources:
- CARLA Simulator
- Apollo AV Platform
- Path Planning Papers
```

### Projet 4: 🏠 IoT Smart Home (À CRÉER)
```
Difficulté: ⭐⭐ Intermédiaire
Temps: 3-4h
État: 📝 Architecture + code starter
Fichiers: iot/mqtt_controller.py (À créer)

Objectifs:
□ MQTT Communication
□ Multi-Sensor Integration
□ Automation Rules
□ Web Dashboard
□ Alerts & Notifications

Ressources:
- Home Assistant
- Node-RED
- MQTT Protocol
```

### Projet 5: 🔒 Intrusion Detection (À CRÉER)
```
Difficulté: ⭐⭐⭐ Intermédiaire
Temps: 4-5h
État: 📝 Guide + code starter
Fichiers: network-security/ids_system.py (À créer)

Objectifs:
□ Packet Capture
□ Traffic Analysis
□ Anomaly Detection
□ Attack Classification
□ Real-time Alerts

Ressources:
- Scapy Library
- Snort IDS
- Suricata Rules
```

### Projet 6: ⚡ Scheduler Temps-Réel (À CRÉER)
```
Difficulté: ⭐⭐⭐⭐ Avancé
Temps: 5-7h
État: 📝 Théorie + code starter
Fichiers: real-time-systems/scheduler.py (À créer)

Objectifs:
□ Rate Monotonic Scheduling
□ Priority Assignment
□ Schedulability Analysis
□ Gantt Diagram
□ WCET Estimation

Ressources:
- FreeRTOS
- Real-time Theory
- Embedded Systems
```

---

## 📖 Documentation Complète

| Document | Contenu | Publique d'accueil |
|----------|---------|------------------|
| **PROJETS_PRATIQUES.md** | 5 projets avec architecture + code starter | Débutants |
| **RESSOURCES_LIENS.md** | 50+ liens (vidéos, tutos, cours) | Tout le monde |
| **CPS_LEARNING_GUIDE.md** | Roadmap complète 13 domaines + 3 niveaux | Apprenants sérieux |
| **README.md** | Vue d'ensemble du repo | Premier contact |
| **sensors/PROJECT_TEMPERATURE_SENSOR.md** | Guide détaillé Projet 1 | Débutants |

---

## 🎯 Objectifs d'Apprentissage

### Phase 1: Fondations (Semaines 1-2)
- [ ] Comprendre architecture CPS
- [ ] Maîtriser Python OOP
- [ ] Implémenter Projet 1
- [ ] Lire 3 ressources externes

### Phase 2: Concepts (Semaines 3-4)
- [ ] Apprendre Kinematics/IoT
- [ ] Implémenter Projet 2 ou 4
- [ ] Consulter cours universitaire
- [ ] Créer extension au Projet 1

### Phase 3: Intégration (Semaines 5-6)
- [ ] Comprendre Perception + Planning
- [ ] Implémenter Projet 3 ou 5
- [ ] Setup simulateur (CARLA)
- [ ] Analyser réseau réel

### Phase 4: Expertise (Semaines 7-8)
- [ ] Maîtriser scheduling temps-réel
- [ ] Implémenter Projet 6
- [ ] Intégrer plusieurs projets
- [ ] Créer votre propre projet

---

## 🚀 Commandes Rapides

```bash
# 1. Setup complet
bash setup.sh

# 2. Démarrer Projet 1
cd sensors
python temperature_sensor_reader.py

# 3. Visualiser résultats
python visualize_sensor_data.py sensor_data_*.csv --stats

# 4. Lire documentation
cat PROJETS_PRATIQUES.md | less

# 5. Consulter ressources
cat RESSOURCES_LIENS.md | grep "YouTube"
```

---

## 🤝 Contribution et Extensions

Idées pour **étendre** chaque projet:

### Projet 1 (Sensors)
- [ ] Ajouter Database (SQLite/PostgreSQL)
- [ ] Cloud sync (AWS/Azure)
- [ ] Mobile app notification
- [ ] Machine learning anomaly detection

### Projet 2 (Robotics)
- [ ] Multi-arm coordination
- [ ] Obstacle avoidance
- [ ] Gripper control
- [ ] ROS integration

### Projet 3 (Autonomous Vehicles)
- [ ] Multi-sensor fusion
- [ ] Deep learning perception
- [ ] Trajectory optimization
- [ ] Safety verification

### Projet 4 (IoT)
- [ ] Voice control (Alexa)
- [ ] Energy optimization
- [ ] Predictive automation
- [ ] Edge computing

### Projet 5 (Security)
- [ ] Distributed IDS
- [ ] Threat intelligence
- [ ] Automated response
- [ ] Machine learning for detection

### Projet 6 (Real-Time)
- [ ] Hardware integration
- [ ] Safety certification
- [ ] Performance benchmarking
- [ ] Formal verification

---

## 📞 Support

**Questions?**
- 📍 GitHub Issues: [cyberphysical-systems/issues](https://github.com/MELAI-1/cyberphysical-systems/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/MELAI-1/cyberphysical-systems/discussions)
- 📧 Contact: Voir README.md

**Communautés:**
- ROS Discourse: https://discourse.ros.org/
- Arduino Forum: https://forum.arduino.cc/
- Stack Exchange: https://robotics.stackexchange.com/

---

## 📊 Statistiques

| Métrique | Valeur |
|----------|--------|
| Projets Concrets | 6 |
| Domaines CPS | 13 |
| Ressources Externes | 50+ |
| Lignes de Code | 1000+ |
| Heures d'Apprentissage | 30-40h |
| Documentation (lignes) | 5000+ |

---

## 📅 Versions

| Version | Date | Contenu |
|---------|------|---------|
| **v1.0** | 30 Juin 2026 | Release initial: 5 projets + ressources complètes |

---

## 🎉 Prochaines Étapes

### Maintenant:
1. ✅ Lire ce fichier (vous l'avez fait!)
2. → Aller à **PROJETS_PRATIQUES.md**

### Dans 5 minutes:
3. → Consulter **RESSOURCES_LIENS.md**
4. → Choisir un projet

### Dans 30 minutes:
5. → Exécuter `bash setup.sh`
6. → Lancer Projet 1

### Bonne chance! 🚀

---

<div align="center">

**Cyber-Physical Systems Learning Platform**

*Intégrer le calcul, les réseaux, et les processus physiques* 🌍

[GitHub](https://github.com/MELAI-1/cyberphysical-systems) | [Projets](./PROJETS_PRATIQUES.md) | [Ressources](./RESSOURCES_LIENS.md) | [Guide Complet](./CPS_LEARNING_GUIDE.md)

</div>
