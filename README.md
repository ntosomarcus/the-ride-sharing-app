## Ride Sharing App

A minimal but real ride-sharing backend simulation with:

- Driver/passenger registration
- Trip creation with persistence (`app/data.json`)
- Automatic route matching (driver/passenger with same start + stop)
- Match acceptance flow

## Run

```bash
cd /workspace/the-ride-sharing-app
python app/app.py
```

## Menu

1. Register user
2. Create trip
3. List driver trips
4. List passenger trips
5. Find matches
6. Accept match
7. Exit

## Notes

- Location matching is currently exact-text match after lowercase normalization.
- Storage is JSON-file based for easy local usage.
