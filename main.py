from models import Patient, Hospital
from utils import triage_priority, find_available_hospital, discharge_from_hospital

# Data Setup using a Python dictionary for faster hospital lookup
hospitals_dict = {
    "korle-bu": Hospital("Korle-Bu", 2),
    "37 military": Hospital("37 Military", 3000),
    "tema general": Hospital("Tema General", 2000),
    "cape coast teaching": Hospital("Cape Coast Teaching", 1500),
    "komfo anokye teaching": Hospital("Komfo Anokye Teaching", 10000),
    "tamale teaching": Hospital("Tamale Teaching", 8000),
    "ho teaching": Hospital("Ho Teaching", 5000),
    "sunyani regional": Hospital("Sunyani Regional", 3000),
    "effia nkwanta regional": Hospital("Effia Nkwanta Regional", 2000),
    "cape coast regional": Hospital("Cape Coast Regional", 1500),
    "koforidua regional": Hospital("Koforidua Regional", 1000),
    "bolgatanga regional": Hospital("Bolgatanga Regional", 500)
}

def run_system():
    print("--- Emergency Bed Referral System ---")
    while True:
        user_input = input("\nEnter Patient Name (or 'exit', or 'discharge'): ").strip().lower()

        if user_input == 'exit':
            break

        # Handle discharge request
        if user_input == 'discharge':
            hospital_name = input("Enter Hospital Name to discharge from: ")
            discharge_from_hospital(hospitals_dict, hospital_name)
            continue   # go back to menu

        # Otherwise, treat input as patient name
        name = user_input
        age = int(input("Enter Age: "))
        severity = int(input("Enter Severity (1-5): "))

        patient = Patient(name, age, severity)
        priority = triage_priority(patient)
        print(f"Triage Result: {priority} PRIORITY")

        # Find any hospital with free bed
        target_hospital = find_available_hospital(hospitals_dict)

        if target_hospital:
            if target_hospital.allocate_bed():
                print(f"SUCCESS: Bed assigned at {target_hospital.name}.")
            else:
                print("CRITICAL: Bed allocation failed unexpectedly.")
        else:
            print("ALERT: NO BEDS AVAILABLE in the network! Initiate emergency protocols.")


if __name__ == "__main__":
    run_system()