task = input("Enter your task: ").lower
priority = input("Priority (high/medium/low): ").lower
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print("Finish project report, is a high priority task that requires immediate attendtion today.")
        else:
            print("Set a reminder for today for this high-priority task.")
    case "medium":
        if time_bound == "yes":
            print("Complete the task by the end of the week.")
        else:
            print("Schedule the task for later this week.")
    case "low":
        if time_bound == "yes":
            print("Try to finish the task by the end of the month.")    
        else:
            print("You can do this task whenever you have free time.")
    