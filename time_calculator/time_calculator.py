seconds = float(input("Enter the number of seconds: "))

if seconds < 60:
    print(format(seconds, ".2f"), "seconds")
elif seconds >= 60 and seconds < 3600:
    minutes = seconds // 60
    seconds = seconds % 60
    print(format(minutes, ".2f"), "minutes |",
          format(seconds, ".2f"), "seconds")
elif seconds >= 3600 and seconds < 86400:
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    print(format(hours, ".2f"), "hours |",
          format(minutes, ".2f"), "minutes |",
          format(seconds, ".2f"), "seconds")
else:
    days = seconds // 86400
    remaining_seconds = seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    print(format(days, ".2f"), "days |",
          format(hours, ".2f"), "hours |",
          format(minutes, ".2f"), "minutes |",
          format(seconds, ".2f"), "seconds")
