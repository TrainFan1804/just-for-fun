import datetime


days= ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

weekday = datetime.datetime.today().weekday()

print(weekday)
print(days[weekday])