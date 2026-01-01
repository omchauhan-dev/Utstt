
# fare_calculator.py

FARE_SLABS = {
    5: 5, 10: 10, 15: 10, 20: 15, 25: 20, 30: 20, 35: 20, 40: 25, 45: 25, 50: 30,
    55: 30, 60: 35, 65: 35, 70: 35, 75: 40, 80: 40, 85: 40, 90: 45, 95: 45, 100: 50,
    110: 50, 120: 55, 130: 60, 140: 60, 150: 65, 160: 70, 170: 75, 180: 75, 190: 80,
    200: 85, 220: 90, 240: 95, 260: 100, 280: 105, 300: 110, 320: 115, 340: 120,
    360: 125, 380: 130, 400: 135, 420: 140, 440: 145, 460: 150, 480: 155, 500: 160,
}

def get_fare_and_validity(distance: int) -> tuple[int, str]:
    """
    Calculates the unreserved ticket fare and validity based on the distance
    using a slab-based system.
    The actual fare may vary.
    """
    fare = 0
    for slab_dist, slab_fare in FARE_SLABS.items():
        if distance <= slab_dist:
            fare = slab_fare
            break
    
    if fare == 0: # If distance is greater than the highest slab
        fare = 160 + round((distance - 500) * 0.3) # Approximate fare for longer distances

    if distance <= 199:
        validity = "3 hours"
    else:
        validity = "24 hours"

    return fare, validity
