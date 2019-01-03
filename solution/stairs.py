
def count_combinations(stairs_count):
    if not isinstance(stairs_count, int):
        raise ValueError("stairs_count must be an integer")
    if stairs_count < 0:
        raise ValueError("stairs_count must be non-negative")
    if stairs_count == 0:
        return 1