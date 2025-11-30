# src/charles_rant_generator.py
"""
Charles Hoskinson Infinite Rant Engine™
Officially endorsed by 47 chickens and one very tired YouTube moderator.

Features:
- 100% peer-reviewed by Ethiopian goats
- Zero knowledge proofs that you will never reach the end
- Built-in hydration reminder (you'll need it)

Run this and go make coffee. Come back in 2029.
"""

import random
import time
import sys

STARTERS = [
    "Look, I've been in this space since before you were born,",
    "When I was in Ethiopia with the goats, I realized,",
    "Let me explain this with a metaphor involving chickens,",
    "People don't understand that Cardano isn't just a blockchain,",
    "Back in 2015, Vitalik and I were having coffee and,",
    "The problem with Solana is they never solved,",
    "You have to understand the academic rigor,",
    "We've published more papers than the entire top 10 combined,",
    "This is why we can't have nice things in crypto,",
    "Hydra isn't just fast, it's mathematically,",
]

MIDDLE = [
    "and that's why Ouroboros is the most secure consensus mechanism",
    "which is why we need formal verification at the ISP level",
    "so the Voltaire phase will actually be a multi-decade governance journey",
    "meaning that by 2035 we'll have sidechains with sidechains that have sidechains",
    "because liquid democracy with recursive SNARKs is the only sane path",
    "and this is exactly why Bitcoin maximalists are intellectually bankrupt",
    "which brings us back to why the Basho era is actually about farming optimization",
    "so obviously we need a new CIP for chicken-based randomness oracles",
    "and that's before we even get into the lace wallet light mode dark mode toggle debate",
    "which is why the community voted to delay the hard fork until after my birthday",
]

TANGENTS = [
    "speaking of which, have I told you about my new pineapple farm?",
    "this one time in Puerto Rico with the hurricane,",
    "my wolf thinks you're wrong about this",
    "the Romans actually had a form of stake pools,",
    "in Game Theory, this is called the Hoskinson Paradox,",
    "I once debated this with Joseph Lubin for 14 hours straight,",
    "the ancient Greeks would have used Cardano for their aqueducts",
    "this is literally why I own 47 chickens",
    "and that's not even counting the alpacas",
    "did I mention we're building a hospital in Wyoming?",
]

ENDERS = [
    "but we'll talk about that in the next AMA.",
    "anyway, back to the original point,",
    "so yeah, that's why we're only 8 years behind schedule.",
    "and that's the beauty of the Cardano roadmap.",
    "questions? No? Good. Moving on.",
    "I'll make a longer video about this tomorrow.",
    "this is why we can't ship on time, but it's worth it.",
    "and that's why you're poor.",
    "see you in 2030 when this finally ships.",
    "hydra heads.",
]

def generate_rant(minutes: int = 45):
    print("CHARLES HOSKINSON LIVE STREAM SIMULATOR v3.7")
    print("Topic: Why Your Favorite Chain Is Trash (45+ minutes)")
    print("-" * 60)
    time.sleep(2)

    words_spoken = 0
    start_time = time.time()

    while time.time() - start_time < minutes * 60:
        line = random.choice(STARTERS)
        for _ in range(random.randint(3, 12)):
            line += " " + random.choice(MIDDLE)
            words_spoken += 1

            if random.random() < 0.3:
                line += " " + random.choice(TANGENTS)
                if random.random() < 0.1:
                    line += " " + random.choice(TANGENTS)  # double tangent = peak Charles

        line += " " + random.choice(ENDERS)
        print(line)
        words_spoken += 8

        # Real-time stats
        elapsed = int(time.time() - start_time)
        wpm = int(words_spoken / max(1, elapsed / 60))
        print(f"   ⏱  {elapsed//60:02d}:{elapsed%60:02d} | 📈 {wpm} wpm | 🔥 {words_spoken:,} words", end="\r")
        
        time.sleep(random.uniform(1.8, 4.2))  # natural speaking cadence

    print("\n\nSTREAM ENDED")
    print(f"Total duration: {minutes} minutes")
    print(f"Words spoken: {words_spoken:,}")
    print(f"Average: {words_spoken//minutes} words per minute")
    print("Hydration check: You are now clinically dehydrated.")
    print("The roadmap has been extended by 18 months.")

if __name__ == "__main__":
    try:
        length = int(input("How many minutes of your life minutes to sacrifice? (default 45): ") or "45")
        generate_rant(length)
    except KeyboardInterrupt:
        print("\n\nYou lasted 3 minutes. Weak. Charles is disappointed but not surprised.")
