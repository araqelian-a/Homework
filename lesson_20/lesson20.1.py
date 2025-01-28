# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule
class HospitalAccaunt:
    def __init__(self, patient_id):
        self.id = patient_id
        self.visits = []
    def add_visits(self,date):
        if date not in self.visits:
            self.visits.append(date)
        else:
            print(f"you have visit in this date {date}")
    def remove_visits(self,date):
        if date in self.visits:
            self.visits.remove(date)
        else:
            return f"this date {date} isnt busy"
    def show_visits(self):
        return self.visits

visits = HospitalAccaunt("12545")
visits.add_visits("12.02.2025")
print(visits.show_visits())

