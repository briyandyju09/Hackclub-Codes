import json
import os
from datetime import datetime



class EventManager:
    def __init__(self, filename='events.json'):
        self.filename = filename
        self.events = self.load_events()
        self.run()


  
    def load_events(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error loading events file. File may be corrupted.")
                return []
        return []

  
    def save_events(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.events, file, indent=4)
        except IOError:
            print("Error saving events to file.")


  
    def add_event(self, name, date, location):
        if not name or not date or not location:
            print("Event name, date, and location cannot be empty.")
            return
        try:
            event_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Date format is incorrect. Use YYYY-MM-DD.")
            return
        self.events.append({'name': name, 'date': date, 'location': location})
        self.save_events()
        print(f"Added event: {name} on {date} at {location}")

  
    def delete_event(self, name):
        for event in self.events:
            if event['name'] == name:
                self.events.remove(event)
                self.save_events()
                print(f"Deleted event: {name}")
                return
        print("Event not found.")

  
    def view_events(self):
        if not self.events:
            print("No events available.")
        else:
            for event in self.events:
                print(f"Name: {event['name']}, Date: {event['date']}, Location: {event['location']}")

  
    def run(self):
        while True:
            print("\nEvent Manager")
            print("1. Add Event")
            print("2. Delete Event")
            print("3. View Events")
            print("4. Exit")
            choice = input("Choose an option: ").strip()

          
            if choice == '1':
                name = input("Enter event name: ").strip()
                date = input("Enter event date (YYYY-MM-DD): ").strip()
                location = input("Enter event location: ").strip()
                self.add_event(name, date, location)
            elif choice == '2':
                name = input("Enter event name to delete: ").strip()
                self.delete_event(name)
            elif choice == '3':
                self.view_events()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")



if __name__ == '__main__':
    EventManager()
