task = input("Enter your task: ").lower
priority = input("Priority (high/medium/low): ").lower
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            reminder = "Finish project report, is a high priority task that requires immediate attendtion today."
            print(reminder)
        else:
            reminder = "Set a reminder for today for this high-priority task."
            print(reminder)
    case "medium":
        if time_bound == "yes":
            reminder = "Complete the task by the end of the week."
            print(reminder)
        else:
            reminder = "Schedule the task for later this week."
            print(reminder)
    case "low":
        if time_bound == "yes":
            reminder = "Try to finish the task by the end of the month."
            print(reminder)    
        else:
            reminder = "You can do this task whenever you have free time."
            print(reminder)