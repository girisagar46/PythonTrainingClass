import sys
import calendar

if sys.argv[1] == "--help":
	print("this is help string")
if sys.argv[1] == "--os":
	print(os.name)
if sys.argv[1] == '--cal':
	if sys.argv[2] == "SUNDAY":
		c = calendar.TextCalendar(calendar.SUNDAY)
		cal = c.formatmonth(2017, 1)
		print(cal)
