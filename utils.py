def triage_priority(patient):
    """
    Determine urgency based on severity + age.
    This uses nested if logic as requested.
    """
    if patient.severity >= 4:
        # High severity: check age vulnerability
        if patient.age > 60 or patient.age < 5:
            return "IMMEDIATE"
        else:
            return "URGENT"
    elif patient.severity >= 2:
        return "STABLE"
    else:
        return "NON-URGENT"


def find_available_hospital(hospitals_dict):
    """Return the first hospital that has a free bed (dictionary version)."""
    for hospital in hospitals_dict.values():
        if hospital.has_space():
            return hospital
    return None


def discharge_from_hospital(hospitals_dict, hospital_name):
    """
    Locate a hospital by case-insensitive name and free one bed.
    Returns True if discharge succeeded, False otherwise.
    """
    key = hospital_name.lower()
    if key in hospitals_dict:
        hospital = hospitals_dict[key]
        if hospital.discharge():
            print(f"SUCCESS: Freed a bed at {hospital.name}. "
                  f"Occupied: {hospital.occupied_beds}/{hospital.total_beds}")
            return True
        else:
            print(f"INFO: No occupied beds at {hospital.name}.")
            return False
    else:
        print(f"ERROR: Hospital '{hospital_name}' not found in network.")
        return False