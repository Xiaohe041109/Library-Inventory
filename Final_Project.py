                                     from datetime import datetime, timedelta
import time

def scheduleTimer(dayOfWeek, startTime, durationMinutes):
    currentTime = datetime.now()
    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    targetDay = daysOfWeek.index(dayOfWeek.capitalize())

    daysUntilTarget = (targetDay - currentTime.weekday() + 7) % 7
    if daysUntilTarget == 0 and currentTime.time() > datetime.strptime(startTime, '%H:%M').time():
        daysUntilTarget = 7

    targetDatetime = (currentTime + timedelta(days=daysUntilTarget))
    targetDatetime = targetDatetime.replace(hour=int(startTime.split(':')[0]), minute=int(startTime.split(':')[1]), second=0)

    end_time = targetDatetime + timedelta(minutes=durationMinutes)

    print(f"Timer set for {dayOfWeek} at {startTime}, which will run for {durationMinutes} minutes.")
    print(f"Starts at: {targetDatetime}")
    print(f"Ends at: {end_time}")

    while datetime.now() < targetDatetime:
        time.sleep(1)
    print("Timer started!")
    while datetime.now() < end_time:
        time.sleep(1)
    print("Timer ended!")

# Example usage
if __name__ == "__main__":
    scheduleTimer('Monday', '16:00', 240)  # Day, start time in 24H format, duration in minutes
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
