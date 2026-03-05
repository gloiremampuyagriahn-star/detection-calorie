#!/usr/bin/env python3
"""
Détection de calories dans les aliments.

Usage:
    python detect_calories.py --food "pomme"
    python detect_calories.py --food "riz" --quantity 200
    python detect_calories.py --list
"""

import argparse
import json
import os
import sys


DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "calories.json")


def load_calorie_database():
    """Charge la base de données caloriques depuis le fichier JSON."""
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def detect_calories(food_name: str, quantity_g: float = 100.0) -> dict:
    """
    Estime les calories pour un aliment donné.

    Args:
        food_name: Nom de l'aliment (en français).
        quantity_g: Quantité en grammes (par défaut 100g).

    Returns:
        Dictionnaire avec le nom, la quantité et les calories estimées.
    """
    db = load_calorie_database()
    food_lower = food_name.lower().strip()

    # Recherche exacte
    if food_lower in db:
        kcal_per_100g = db[food_lower]
    else:
        # Recherche partielle
        matches = [k for k in db if food_lower in k or k in food_lower]
        if not matches:
            return {
                "food": food_name,
                "quantity_g": quantity_g,
                "calories_kcal": None,
                "error": f"Aliment '{food_name}' non trouvé dans la base de données.",
            }
        food_lower = matches[0]
        kcal_per_100g = db[food_lower]

    calories = round(kcal_per_100g * quantity_g / 100, 1)
    return {
        "food": food_lower,
        "quantity_g": quantity_g,
        "calories_kcal": calories,
        "kcal_per_100g": kcal_per_100g,
    }


def list_foods():
    """Affiche tous les aliments disponibles dans la base de données."""
    db = load_calorie_database()
    print(f"{'Aliment':<30} {'Calories (kcal/100g)':>20}")
    print("-" * 52)
    for food, kcal in sorted(db.items()):
        print(f"{food:<30} {kcal:>20}")


def main():
    parser = argparse.ArgumentParser(
        description="Estimation des calories pour un aliment donné."
    )
    parser.add_argument(
        "--food",
        "-f",
        type=str,
        help="Nom de l'aliment (ex: pomme, riz, poulet)",
    )
    parser.add_argument(
        "--quantity",
        "-q",
        type=float,
        default=100.0,
        help="Quantité en grammes (défaut: 100g)",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="Afficher tous les aliments disponibles",
    )

    args = parser.parse_args()

    if args.list:
        list_foods()
        return

    if not args.food:
        parser.print_help()
        sys.exit(1)

    result = detect_calories(args.food, args.quantity)

    if result.get("error"):
        print(f"❌ {result['error']}", file=sys.stderr)
        print("Utilisez --list pour voir les aliments disponibles.")
        sys.exit(1)

    print(f"\n🍽️  Aliment     : {result['food']}")
    print(f"⚖️  Quantité    : {result['quantity_g']}g")
    print(f"🔥 Calories    : {result['calories_kcal']} kcal")
    print(f"   (base: {result['kcal_per_100g']} kcal/100g)\n")


if __name__ == "__main__":
    main()
