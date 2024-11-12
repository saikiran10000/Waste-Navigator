class WasteManagementSystem:
    def __init__(self):
        self.reports = []
        self.pickups = []

    def report_issue(self, location, issue_type):
        """Report a waste issue."""
        report = {
            'location': location,
            'issue_type': issue_type,
            'status': 'reported'
        }
        self.reports.append(report)
        print(f"Issue reported at {location}: {issue_type}")

    def schedule_pickup(self, location):
        """Schedule a waste pickup."""
        pickup = {
            'location': location,
            'status': 'scheduled'
        }
        self.pickups.append(pickup)
        print(f"Pickup scheduled at {location}")

    def view_reports(self):
        """View all reported issues."""
        return self.reports

    def view_pickups(self):
        """View all scheduled pickups."""
        return self.pickups


# Example usage
if __name__ == "__main__":
    waste_management = WasteManagementSystem()

    # Community members reporting issues
    waste_management.report_issue("789 Main st", "Overflowing bin")
    waste_management.report_issue("456 Elm St", "Illegal dumping")

    # Scheduling pickups
    waste_management.schedule_pickup("789 Main St")

    # View reports and pickups
    print("\nReported Issues:")
    for report in waste_management.view_reports():
        print(report)

    print("\nScheduled Pickups:")
    for pickup in waste_management.view_pickups():
        print(pickup)