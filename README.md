# Détection de Calories 🍎

Application d'estimation de calories pour les aliments courants, avec une base de données intégrée et une interface en ligne de commande.

> **Note :** La détection d'aliments par image (ML/IA) est prévue dans une prochaine version.

## Fonctionnalités

- Estimation du nombre de calories par aliment (base de données de plus de 60 aliments)
- Interface en ligne de commande simple d'utilisation
- Recherche partielle sur le nom de l'aliment
- Extensible avec vos propres données

## Prérequis

- Python 3.8+
- pip

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

### Estimation des calories d'un aliment

```bash
python detect_calories.py --food "pomme"
```

### Spécifier une quantité en grammes

```bash
python detect_calories.py --food "riz" --quantity 200
```

### Lister tous les aliments disponibles

```bash
python detect_calories.py --list
```

## Structure du projet

```
detection-calorie/
├── detect_calories.py   # Script principal de détection
├── requirements.txt     # Dépendances Python
├── data/
│   └── calories.json    # Base de données calories par aliment
└── README.md
```

## Base de données caloriques

Le fichier `data/calories.json` contient les valeurs caloriques (kcal pour 100g) pour de nombreux aliments courants. Vous pouvez l'enrichir avec vos propres données.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## Licence

MIT
