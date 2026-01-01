
# station_data.py

STATION_DISTANCES = {
    ("mumbai", "delhi"): 1384,
    ("delhi", "mumbai"): 1384,
    ("mumbai", "pune"): 180,
    ("pune", "mumbai"): 180,
    ("chennai", "bangalore"): 359,
    ("bangalore", "chennai"): 359,
    ("kolkata", "delhi"): 1445,
    ("delhi", "kolkata"): 1445,
}

def get_distance(source: str, destination: str) -> int | None:
    """
    Returns the distance between two stations.
    Returns None if the distance is not found.
    """
    return STATION_DISTANCES.get((source.lower(), destination.lower()))
