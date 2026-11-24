#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<=140 chars) for the invented city
Drizzlewick to /output/entry.txt. Forecast register, concrete detail
(the 8:04 bus on time), and a small smile for a bored commuter.
"""
import os

ENTRY = (
    "In Drizzlewick, light rain until nine, then sunshine "
    "\u2014 the 8:04 bus is on time, and your umbrella finally "
    "gets the day off."
)


def main():
    text = ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
