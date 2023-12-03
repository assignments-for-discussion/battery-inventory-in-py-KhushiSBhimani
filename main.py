
def count_batteries_by_health(present_capacities):
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }
   # Rated capacity of a new battery
    rated_capacity = 120
    
    for present_capacity in present_capacities:
        # Calculate State of Health (SoH)
        soh_percentage = (present_capacity / rated_capacity) * 100
        
        # Classify batteries based on SoH and update counts
        if soh_percentage > 80:
            counts["healthy"] += 1
        elif 62 <= soh_percentage <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts


def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)

    # Print the counts for debugging
    print("Counts:", counts)

    assert counts["healthy"] == 2, f"Expected healthy count: 2, but got {counts['healthy']}"
    assert counts["exchange"] == 3, f"Expected exchange count: 3, but got {counts['exchange']}"
    assert counts["failed"] == 1, f"Expected failed count: 1, but got {counts['failed']}"
    print("Done counting :)")



if __name__ == '__main__':
  test_bucketing_by_health()
