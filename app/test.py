import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.app import RideSharingApp


def test_match_flow(tmp_path):
    db = tmp_path / "data.json"
    app = RideSharingApp(db_path=str(db))

    driver = app.register_user("Driver A", 30, "M", "driver")
    passenger = app.register_user("Passenger B", 24, "F", "passenger")

    d_trip = app.create_trip(driver["id"], "Accra", "Kumasi", seats=3)
    p_trip = app.create_trip(passenger["id"], "accra", "kumasi", seats=1)

    matches = app.find_matches()
    assert len(matches) == 1

    accepted = app.accept_match(matches[0]["id"])
    assert accepted["status"] == "accepted"

    trips = app.list_trips()
    d_state = [t for t in trips if t["id"] == d_trip["id"]][0]
    p_state = [t for t in trips if t["id"] == p_trip["id"]][0]
    assert d_state["status"] == "matched"
    assert p_state["status"] == "matched"
