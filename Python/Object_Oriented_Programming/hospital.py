class Patient(object):
    def __init__(self, id_number, name, bed_number, *allergies):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number
class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def addPatient(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
        else:
            print "The hospital is full."
        return self
    def discharge(self, patient):
        for patient1 in self.patients:
            if patient1.name == patient.name:
                self.patients.remove(patient)
                patient.bed_number = 0
        return self
    def displayInfo(self):
        for patient in self.patients:
            print "Id Number:", patient.id_number
            print "Name:", patient.name
            print "Bed Number:", patient.bed_number
            print "Allergies:", patient.allergies
        return self

patientA = Patient(1235, "Helen Smith", 10, ("peanuts", "seafood"))
patientB = Patient(1594, "Robert Brown", 15, "eggs")
patientC = Patient(1587, "Amy Beard", 26, ("guinea pigs", "cats"))
patientD = Patient(1658, "Robin Meggs", 51, "coconut")
hospital1 = Hospital("Inova Fairfax", 2)
hospital1.addPatient(patientA).addPatient(patientB).addPatient(patientC).addPatient(patientD).discharge(patientA).displayInfo()
