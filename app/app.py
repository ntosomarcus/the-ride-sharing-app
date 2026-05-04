from __future__ import annotations

import json
from pathlib import Path
from typing import Any

try:
    from .models import Match, Trip, User
except ImportError:
    from models import Match, Trip, User


class RideSharingApp:
    def __init__(self, db_path: str = "app/data.json"):
        self.db_path = Path(db_path)
        self.data: dict[str, Any] = {"users": [], "trips": [], "matches": []}
        self._load()

    def _load(self) -> None:
        if self.db_path.exists():
            self.data = json.loads(self.db_path.read_text())

    def _save(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.db_path.write_text(json.dumps(self.data, indent=2))

    def register_user(self, name: str, age: int, sex: str, role: str) -> dict:
        if role not in {"driver", "passenger"}:
            raise ValueError("Role must be 'driver' or 'passenger'.")
        user = User.create(name=name, age=age, sex=sex, role=role)  # type: ignore[arg-type]
        self.data["users"].append(user.to_dict())
        self._save()
        return user.to_dict()

    def create_trip(self, user_id: str, start: str, stop: str, seats: int = 1) -> dict:
        user = self._find_user(user_id)
        if not user:
            raise ValueError("User not found")
        if seats < 1:
            raise ValueError("Seats must be at least 1")

        trip = Trip.create(user_id=user_id, role=user["role"], start=start, stop=stop, seats=seats)
        self.data["trips"].append(trip.to_dict())
        self._save()
        return trip.to_dict()

    def list_trips(self, role: str | None = None) -> list[dict]:
        trips = self.data["trips"]
        if role:
            trips = [t for t in trips if t["role"] == role]
        return trips

    def find_matches(self) -> list[dict]:
        open_drivers = [
            t for t in self.data["trips"] if t["role"] == "driver" and t["status"] == "open"
        ]
        open_passengers = [
            t for t in self.data["trips"] if t["role"] == "passenger" and t["status"] == "open"
        ]

        new_matches = []
        for driver_trip in open_drivers:
            for passenger_trip in open_passengers:
                if driver_trip["start"] == passenger_trip["start"] and driver_trip["stop"] == passenger_trip["stop"]:
                    if self._already_matched(driver_trip["id"], passenger_trip["id"]):
                        continue
                    match = Match.create(driver_trip_id=driver_trip["id"], passenger_trip_id=passenger_trip["id"])
                    self.data["matches"].append(match.to_dict())
                    new_matches.append(match.to_dict())

        self._save()
        return new_matches

    def accept_match(self, match_id: str) -> dict:
        match = next((m for m in self.data["matches"] if m["id"] == match_id), None)
        if not match:
            raise ValueError("Match not found")
        if match["status"] != "proposed":
            raise ValueError("Match cannot be accepted")

        match["status"] = "accepted"
        driver_trip = self._find_trip(match["driver_trip_id"])
        passenger_trip = self._find_trip(match["passenger_trip_id"])

        if not driver_trip or not passenger_trip:
            raise ValueError("Trip not found for this match")

        driver_trip["status"] = "matched"
        passenger_trip["status"] = "matched"
        driver_trip["matched_trip_id"] = passenger_trip["id"]
        passenger_trip["matched_trip_id"] = driver_trip["id"]

        self._save()
        return match

    def _find_user(self, user_id: str) -> dict | None:
        return next((u for u in self.data["users"] if u["id"] == user_id), None)

    def _find_trip(self, trip_id: str) -> dict | None:
        return next((t for t in self.data["trips"] if t["id"] == trip_id), None)

    def _already_matched(self, driver_trip_id: str, passenger_trip_id: str) -> bool:
        return any(
            m
            for m in self.data["matches"]
            if m["driver_trip_id"] == driver_trip_id and m["passenger_trip_id"] == passenger_trip_id
        )


def main() -> None:
    app = RideSharingApp()
    print("=== Ride Sharing App (persistent CLI) ===")

    while True:
        print("\n1. Register user")
        print("2. Create trip")
        print("3. List driver trips")
        print("4. List passenger trips")
        print("5. Find matches")
        print("6. Accept match")
        print("7. Exit")
        choice = input("Select option: ").strip()

        try:
            if choice == "1":
                name = input("Name: ")
                age = int(input("Age: "))
                sex = input("Sex: ")
                role = input("Role (driver/passenger): ").strip().lower()
                user = app.register_user(name, age, sex, role)
                print(f"Registered: {user['id']}")
            elif choice == "2":
                user_id = input("User ID: ").strip()
                start = input("Start location: ")
                stop = input("Destination: ")
                seats = int(input("Seats (default 1): ") or "1")
                trip = app.create_trip(user_id, start, stop, seats)
                print(f"Trip created: {trip['id']}")
            elif choice == "3":
                print(app.list_trips(role="driver"))
            elif choice == "4":
                print(app.list_trips(role="passenger"))
            elif choice == "5":
                matches = app.find_matches()
                print(matches if matches else "No new matches")
            elif choice == "6":
                match_id = input("Match ID: ").strip()
                print(app.accept_match(match_id))
            elif choice == "7":
                print("Bye")
                break
            else:
                print("Invalid option")
        except Exception as exc:  # CLI guard
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
