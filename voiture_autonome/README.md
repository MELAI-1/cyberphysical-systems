# 🚗 Voiture Autonome - Learning Path

## Aperçu
Explorez les systèmes de véhicules autonomes avec un accent sur la perception, la planification et le contrôle en français et en détail.

**Langages Primaires:** C++, Python | **Langages Secondaires:** Rust

---

## 🎓 Progression de l'Apprentissage

### **NIVEAU DÉBUTANT (0-3 mois)**
**Objectif:** Comprendre la dynamique des véhicules et la perception basique

#### Concepts Clés:
- Modèle de véhicule bicyclette
- Capteurs automobiles (caméra, LiDAR, radar)
- Traitement d'image basique
- Localisation et GPS
- Communication CAN bus
- Simulation avec CARLA
- Méthodologie de développement V2X

#### Projets:
1. Configurer l'environnement de développement
2. Simuler un véhicule dans CARLA
3. Développer un lecteur de capteurs
4. Implémenter un suivi de trajectoire basique
5. Créer un système de surveillance simul

#### Outils:
- CARLA Simulator
- ROS2
- Python pour prototypage
- OpenCV pour vision
- CAN bus tools

#### Structure du Code:
```
voiture_autonome/beginner/
├── simulation_setup/
├── sensor_reading/
├── vehicle_dynamics/
├── basic_perception/
├── can_communication/
└── localization_basics/
```

---

### **NIVEAU INTERMÉDIAIRE (3-9 mois)**
**Objectif:** Implémenter la perception et la planification

#### Concepts Clés:
- Fusion multi-capteurs (caméra + LiDAR + Radar)
- Détection d'objets en temps réel
- Segmentation de scène
- Planification de chemin (path planning)
- Décision et comportement
- Contrôle de mouvement (longitudinal/latéral)
- Tests de sécurité
- Validation fonctionnelle

#### Projets:
1. Pipeline de détection d'objets
2. Fusion capteurs multi-modalités
3. Planification de trajectoire
4. Algorithme de décision comportementale
5. Contrôle du véhicule
6. Tests en simulation CARLA
7. Système de sécurité et fallback
8. Dashboard de monitoring

#### Bibliothèques:
- TensorFlow/PyTorch pour ML
- PCL pour traitement point cloud
- ROS2 pour intégration système
- Behavior Tree pour décisions
- OpenCV pour vision

#### Structure du Code:
```
voiture_autonome/intermediate/
├── object_detection/
├── sensor_fusion/
├── path_planning/
├── behavior_planning/
├── vehicle_control/
├── safety_systems/
├── testing_framework/
└── monitoring_dashboard/
```

---

### **NIVEAU AVANCÉ (9+ mois)**
**Objectif:** Systèmes autonomes complets avec garanties de sécurité

#### Concepts Clés:
- Apprentissage bout-en-bout (end-to-end learning)
- Fusion avancée de capteurs
- Contrôle prédictif (MPC)
- Vérification formelle de sécurité
- Robustesse aux conditions adverses
- Communication V2X
- Déploiement sur matériel embarqué
- Certification et conformité

#### Projets:
1. Modèle end-to-end avec CNN
2. Contrôle prédictif optimisé
3. Détection de défaillances
4. Système de secours (fallback)
5. Communication V2X fonctionnelle
6. Tests hardware-in-the-loop
7. Déploiement production
8. Vérification de sécurité

#### Outils Avancés:
- PyTorch avec export ONNX
- Optlang pour optimisation
- ROS2 en production
- Rust pour systèmes critiques
- Docker pour déploiement
- Systèmes temps réel

#### Structure du Code:
```
voiture_autonome/advanced/
├── end_to_end_learning/
├── advanced_sensor_fusion/
├── model_predictive_control/
├── safety_verification/
├── v2x_communication/
├── hardware_deployment/
├── production_systems/
└── certification_compliance/
```

---

## 📚 Recommandations par Langage

### **Python** (Prototypage & ML)
- TensorFlow/PyTorch pour perception
- API CARLA Python
- Analyse de données
- Développement rapide

### **C++** (Performance & Temps Réel)
- Contrôle temps réel
- ROS2 client libraries
- Optimisation performance
- Boucles critiques

### **Rust** (Sécurité Critique)
- Code sécurisé sans GC
- Garanties mémoire
- Systèmes critiques
- Concurrence sans données-race

---

## 🛠️ Installation

```bash
# CARLA
wget https://carla-releases.s3.amazonaws.com/linux/CARLA_0.9.15.tar.gz
tar xzf CARLA_0.9.15.tar.gz

# ROS2
sudo apt install ros-humble-desktop

# Frameworks ML
pip install torch torchvision tensorflow opencv-python

# Développement
sudo apt install cmake g++ clang-format
```

---

## ✅ Checklist de Progression

- [ ] Dynamique véhicule comprise
- [ ] Capteurs intégrés
- [ ] Perception basique fonctionnelle
- [ ] Fusion capteurs implémentée
- [ ] Localisation et cartographie
- [ ] Planification de chemin
- [ ] Comportement et décision
- [ ] Contrôle du véhicule
- [ ] Apprentissage bout-en-bout
- [ ] Système de sécurité
- [ ] Tests en simulation
- [ ] Déploiement hardware
- [ ] Certification atteinte

---

## 📖 Ressources Recommandées

1. "Autonomous Vehicles: How Self-Driving Cars are Changing the World" - Sparrow
2. "Motion Planning for Mobile Robot Navigation" - Parrish et al.
3. CARLA Documentation
4. Autoware AV Stack
5. Cours MIT 6.S094 (Autonomous Vehicles)
6. Papers CVPR/ICCV (vision autonome)

---

## ⚠️ Sécurité D'Abord

Le développement de véhicules autonomes est très critique pour la sécurité. Respectez les normes ISO 26262, fonctionnez en simulation avant tout matériel réel, et priori toujours la sécurité.

---

## 🚀 Prochaines Étapes

Commencez avec **simulation CARLA** → **perception** → **planification** → **contrôle** → **systèmes complets** → **déploiement**
