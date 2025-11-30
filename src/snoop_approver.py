# src/snoop_approver.py
"""
Snoop Dogg Automatic Node Certification Oracle™
(Chief Vibe Officer Edition)

This is the actual on-chain approval mechanism used in production.
Snoop personally reviews every stake pool operator at 3 a.m. while eating
Flamin’ Hot Cheetos and watching SpongeBob reruns.

100% audited by Dogecoin Foundation (they said "lol lmao")
"""

import random
import time
import json
from typing import Dict, Any

SNOOP_QUOTES = [
    "This shit crisp, nephew!",
    "Fo’ shizzle my crypto nizzle",
    "That’s straight gas ⛽",
    "You got that dogg in ya",
    "Nah cousin, this mid as hell",
    "I’d rather stake with Patrick Star",
    "Smells like cope in here",
    "Drop it like it’s hot… wait it already dropped 97%",
    "Charles, explain this shit to me in chicken terms",
    "Certified West Coast classics only",
]

def snoop_loading_animation():
    print("Snoop is reviewing your node vibes", end="")
    for _ in range(15):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print()

def evaluate_pool_vibes(pool_data: Dict[str, Any]) -> Dict[str, Any]:
    name = pool_data.get("name", "Unnamed Pool #42069")
    pledge = pool_data.get("pledge_ada", 0)
    margin = pool_data.get("margin", 10.0)
    has_chickens = pool_data.get("has_chickens", False)
    theme_song = pool_data.get("theme_song", None)

    snoop_loading_animation()

    score = 0
    feedback = []

    # Actual sophisticated scoring algorithm
    if "dogg" in name.lower() or "snoop" in name.lower():
        score += 50
        feedback.append("Name got that dogg in it ✅")

    if pledge >= 1_000_000:
        score += 30
        feedback.append("Big bags = big respect")
    elif pledge < 5000:
        feedback.append("Bro you staking lunch money 💀")

    if margin > 5.0:
        feedback.append("5%+ margin? You wild for that one")
    ")

    if has_chickens:
        score += 100
        feedback.append("Charles detected. Instant approval.")

    if theme_song == "Still D.R.E.":
        score += 999
        feedback.append("POOL OF THE CENTURY")

    # Final judgment
    print("SNOOP'S VERDICT:\n")
    time.sleep(1)

    if score >= 150:
        print("           APPROVED")
        print("   Snoop Dogg has certified your pool")
        print("   ", random.choice(SNOOP_QUOTES[:4]))
        cert_level = "PLATINUM"
    elif score >= 80:
        print("           conditionally approved")
        print("   ", random.choice(SNOOP_QUOTES[4:7]))
        cert_level = "BRONZE"
    else:
        print("           REJECTED")
        print("   ", random.choice(SNOOP_QUOTES[7:]))
        cert_level = "COPE"

    print(f"\n   Certification tier: {cert_level}-DOGG")
    print("   Feedback:")
    for line in feedback or ["No vibes detected. Try harder."]:
        print(f"   • {line}")

    return {
        "approved": score >= 80,
        "certification_tier": cert_level,
        "snoop_quote": random.choice(SNOOP_QUOTES),
        "timestamp": time.time(),
        "blunt_smoked_during_review": random.randint(1, 3)
    }

if __name__ == "__main__":
    print("SNOOP DOGG NODE CERTIFICATION ORACLE v2.0")
    print("Now with 100% more blunt rotation\n")

    example_pool = {
        "name": input("Pool name: ") or "Bikini Bottom Stake Pool",
        "pledge_ada": float(input("Pledge in ADA: ") or "42069"),
        "margin": float(input("Margin %: ") or "3.33"),
        "has_chickens": input("Does operator own chickens? (y/n): ").lower() == "y",
        "theme_song": input("Pool theme song: ") or "Drop It Like It's Hot"
    }

    result = evaluate_pool_vibes(example_pool)

    if result["approved"]:
        print(f"\nYour pool is now officially {result['certification_tier']}-DOGG certified!")
        print("Expect +420% APY from pure vibes alone.")
    else:
        print("\nBetter luck next epoch, playa.")
        print("Tip: Add more chickens and lower that margin.")
