task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a high priority task. Try to complete it soon."
    
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that should be done in the next few days."
        else:
            reminder = f"Note: '{task}' is a medium priority task. Schedule it when convenient."
    
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task, but you should still finish it soon."
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    
    case _:
        reminder = "Invalid priority level entered."

print("\nReminder:", reminder)
