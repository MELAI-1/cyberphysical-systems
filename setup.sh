#!/bin/bash
# 🚀 CPS Learning Platform - Quick Start Setup

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Cyber-Physical Systems - Learning Platform               ║"
echo "║  Bienvenue! 🎉                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${BLUE}[1/4]${NC} Vérification de l'environnement..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python $python_version détecté"

# Create virtual environment if needed
if [ ! -d "venv" ]; then
    echo -e "${BLUE}[2/4]${NC} Création d'un environnement virtuel..."
    python3 -m venv venv
    echo "✅ Environnement virtuel créé"
fi

# Activate venv
echo -e "${BLUE}[3/4]${NC} Activation de l'environnement virtuel..."
source venv/bin/activate
echo "✅ Environnement activé"

# Install dependencies
echo -e "${BLUE}[4/4]${NC} Installation des dépendances..."
pip install --upgrade pip > /dev/null 2>&1
pip install matplotlib pandas numpy scipy scikit-learn paho-mqtt > /dev/null 2>&1
echo "✅ Dépendances installées"

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  ✨ Setup Complet!                                         ║"
echo "╠════════════════════════════════════════════════════════════╣"
echo "║                                                            ║"
echo "║  📚 Documentation:                                         ║"
echo "║  • PROJETS_PRATIQUES.md - 5 projets concrets              ║"
echo "║  • RESSOURCES_LIENS.md - Tous les liens des formations    ║"
echo "║  • CPS_LEARNING_GUIDE.md - Guide complet                  ║"
echo "║                                                            ║"
echo "║  🚀 Démarrage Rapide (Projet 1 - Sensors):                ║"
echo "║                                                            ║"
echo "║     cd sensors                                             ║"
echo "║     pip install -r requirements.txt                        ║"
echo "║     python temperature_sensor_reader.py                    ║"
echo "║                                                            ║"
echo "║  📊 Visualiser les données:                                ║"
echo "║                                                            ║"
echo "║     python visualize_sensor_data.py sensor_data_*.csv      ║"
echo "║                                                            ║"
echo "║  📖 Prochaines étapes:                                     ║"
echo "║  1. Lire PROJETS_PRATIQUES.md                              ║"
echo "║  2. Choisir un projet (Sensors recommandé pour débuter)    ║"
echo "║  3. Consulter RESSOURCES_LIENS.md pour vidéos + tutos      ║"
echo "║  4. Exécuter le code et expérimenter                       ║"
echo "║  5. Progresser vers les projets avancés                    ║"
echo "║                                                            ║"
echo "║  💡 Conseil: Commencez par Projet 1 (Sensors)!             ║"
echo "║     C'est la fondation de tous les autres domaines 🌡️      ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}Environnement prêt! Bon apprentissage! 🚀${NC}"
