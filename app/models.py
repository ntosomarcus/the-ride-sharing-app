from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Literal
import uuid


Role = Literal["driver", "passenger"]
TripStatus = Literal["open", "matched", "completed", "cancelled"]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class User:
    id: str
    name: str
    age: int
    sex: str
    role: Role
    created_at: str

    @classmethod
    def create(cls, name: str, age: int, sex: str, role: Role) -> "User":
        return cls(
            id=str(uuid.uuid4()),
            name=name.strip(),
            age=age,
            sex=sex.strip(),
            role=role,
            created_at=utc_now_iso(),
        )

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Trip:
    id: str
    user_id: str
    role: Role
    start: str
    stop: str
    seats: int
    status: TripStatus
    created_at: str
    matched_trip_id: str | None = None

    @classmethod
    def create(
        cls,
        user_id: str,
        role: Role,
        start: str,
        stop: str,
        seats: int,
    ) -> "Trip":
        return cls(
            id=str(uuid.uuid4()),
            user_id=user_id,
            role=role,
            start=start.strip().lower(),
            stop=stop.strip().lower(),
            seats=seats,
            status="open",
            created_at=utc_now_iso(),
        )

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Match:
    id: str
    driver_trip_id: str
    passenger_trip_id: str
    status: Literal["proposed", "accepted", "declined"]
    created_at: str

    @classmethod
    def create(cls, driver_trip_id: str, passenger_trip_id: str) -> "Match":
        return cls(
            id=str(uuid.uuid4()),
            driver_trip_id=driver_trip_id,
            passenger_trip_id=passenger_trip_id,
            status="proposed",
            created_at=utc_now_iso(),
        )

    def to_dict(self) -> dict:
        return asdict(self)
