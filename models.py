class Patient:
    """Represents a patient with name, age, and severity score."""
    def __init__(self, name, age, severity):
        self.name = name
        self.age = age
        self.severity = severity   # 1 (minimal) to 5 (critical)


class Hospital:
    """Manages bed occupancy for a single hospital."""
    def __init__(self, name, total_beds):
        self.name = name
        self.total_beds = total_beds
        self.occupied_beds = 0

    def has_space(self):
        """Return True if at least one bed is free."""
        return self.occupied_beds < self.total_beds

    def allocate_bed(self):
        """Assign a bed if available. Return True on success."""
        if self.has_space():
            self.occupied_beds += 1
            return True
        return False

    def discharge(self):
        """Free one bed if any patient occupies one. Return True if bed freed."""
        if self.occupied_beds > 0:
            self.occupied_beds -= 1
            return True
        return False