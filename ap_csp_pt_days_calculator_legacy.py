#this is the original days calculator i wrote for ap csp exam when i was a sophomore, it is unoptimized and can be improved!

from datetime import date, datetime, timedelta #tools to create and manipulate datetime objects

months_of_the_year = { #this dictionary allows us to convert the user's month input into an integer that the datetime object can use
  "january": 1,
  "february": 2,
  "march": 3,
  "april": 4,
  "may": 5,
  "june": 6,
  "july": 7,
  "august": 8,
  "september": 9,
  "october": 10,
  "november": 11,
  "december": 12,
}

days_of_the_week = { #this dictionary allows us to convert the day of the week integer that the datetime object returns into the actual day of the week.
  0: "Monday",
  1: "Tuesday",
  2: "Wednesday",
  3: "Thursday",
  4: "Friday",
  5: "Saturday",
  6: "Sunday"
}
def format_start(start):
  match start.day: #universal function to convert datetime object into usable form
    case 1 | 21 | 31:
      formatted_start = start.strftime("%B %-dst, %Y")
    case 2 | 22:
      formatted_start = start.strftime("%B %-dnd, %Y")
    case 3 | 23:
      formatted_start = start.strftime("%B %-drd, %Y")
    case _:
      formatted_start = start.strftime("%B %-dth, %Y")
  return formatted_start
      
def format_end(end):
  match end.day:
    case 1 | 21 | 31:
      formatted_end = end.strftime("%B %-dst, %Y")
    case 2 | 22:
      formatted_end = end.strftime("%B %-dnd, %Y")
    case 3 | 23:
      formatted_end = end.strftime("%B %-drd, %Y")
    case _:
      formatted_end = end.strftime("%B %-dth, %Y")
  return formatted_end
      
def years_ago_from_x(start_year, start_month, start_day, end_year, end_month, end_day):
  unformatted_end_date = datetime(end_year, months_of_the_year[end_month.lower()], end_day)
  unformatted_start_date = datetime(start_year, months_of_the_year[start_month.lower()], start_day)
  formatted_end_date = format_end(unformatted_end_date)
  formatted_start_date = format_start(unformatted_start_date)
  
  delta = unformatted_end_date.date() - unformatted_start_date.date()
  if delta.days == 0:
    print("\n It's the same day.")
  elif delta.days < 0:
    print(f"\n {days_of_the_week[unformatted_end_date.weekday()]}, {formatted_end_date} is {round(((delta.days * -1)/365.2421), 2)} year(s) before {days_of_the_week[unformatted_start_date.weekday()]}, {formatted_start_date}.")
  elif delta.days > 0:
    print(f"\n {days_of_the_week[unformatted_end_date.weekday()]}, {formatted_end_date} is {round(((delta.days)/365.2421), 2)} year(s) after {days_of_the_week[unformatted_start_date.weekday()]}, {formatted_start_date}.")

def days_ago_from_x(start_year, start_month, start_day, end_year, end_month, end_day):
  unformatted_end_date = datetime(end_year, months_of_the_year[end_month.lower()], end_day)
  unformatted_start_date = datetime(start_year, months_of_the_year[start_month.lower()], start_day)
  formatted_end_date = format_end(unformatted_end_date)
  formatted_start_date = format_start(unformatted_start_date)
      
  delta = unformatted_end_date.date() - unformatted_start_date.date()
  if delta.days == 0:
    print("\n It's the same day.")
  elif delta.days < 0:
    print(f"\n {days_of_the_week[unformatted_end_date.weekday()]}, {formatted_end_date} is {delta.days * -1} day(s) before {days_of_the_week[unformatted_start_date.weekday()]}, {formatted_start_date}.")
  elif delta.days > 0:
    print(f"\n {days_of_the_week[unformatted_end_date.weekday()]}, {formatted_end_date} is {delta.days} day(s) after {days_of_the_week[unformatted_start_date.weekday()]}, {formatted_start_date}.")

def weeks_ago_from_x(start_year, start_month, start_day, end_year, end_month, end_day):
  unformatted_end_date = datetime(end_year, months_of_the_year[end_month.lower()], end_day)
  unformatted_start_date = datetime(start_year, months_of_the_year[start_month.lower()], start_day)
  formatted_end_date = format_end(unformatted_end_date)
  formatted_start_date = format_start(unformatted_start_date)
      
  delta = unformatted_end_date.date() - unformatted_start_date.date()
  if delta.days == 0:
    print("\n It's the same day.")
  elif delta.days < 0:
    print(f"\n {days_of_the_week[unformatted_end_date.weekday()]}, {formatted_end_date} is {(delta.days * -1)//7} week(s) and {(delta.days * -1) % 7} day(s) before {days_of_the_week[unformatted_start_date.weekday()]}, {formatted_start_date}.")
  elif delta.days > 0:
    print(f"\n {days_of_the_week[unformatted_end_date.weekday()]}, {formatted_end_date} is {(delta.days)//7} week(s) and {(delta.days) % 7} day(s) after {days_of_the_week[unformatted_start_date.weekday()]}, {formatted_start_date}.")

def find_years(target_month, target_day, target_weekday, start_year, end_year):
  matches = []
  if ((target_month.lower()+str(target_day)) != "february29"):
    ignore_leap_years = input("\n Ignore leap years?: ")
  else:
    ignore_leap_years = "no"

  for year in range(start_year, end_year + 1):
    try:
      dt_check_unformatted = datetime(year, months_of_the_year[target_month.lower()], target_day)
      if year % 4 == 0 and ignore_leap_years.lower() == "yes":
        if year % 100 == 0 and year % 400 == 0:
          continue
        elif year % 100 != 0: 
          continue
        else:
          if days_of_the_week[dt_check_unformatted.weekday()].lower() == target_weekday.lower():
            matches.append(year)
      else:
        if days_of_the_week[dt_check_unformatted.weekday()].lower() == target_weekday.lower():
          matches.append(year)
    except ValueError:
      continue

  match target_day:
    case 1 | 21 | 31:
      dt_check_formatted = dt_check_unformatted.strftime("%B %-dst")
    case 2 | 22:
      dt_check_formatted = dt_check_unformatted.strftime("%B %-dnd")
    case 3 | 23:
      dt_check_formatted = dt_check_unformatted.strftime("%B %-drd")
    case _:
      dt_check_formatted = dt_check_unformatted.strftime("%B %-dth")


  result = ""
  for i in range(len(matches)):
    if i == len(matches) - 1:
      result += str(matches[i])
    else:
      result += str(matches[i]) + ", "
      
  print(f"\n Between {start_year} and {end_year}, {dt_check_formatted} falls on a {target_weekday.capitalize()} in {len(matches)} different year(s): \n \n {result}.")


print("\n Works for years 1 through 9999")  
while True:
  try:
    choice = int(input('''\n Type 1 to calculate years between two dates, type 2 to calculate days between two dates, type 3 to calculate weeks between two dates, 
    \n type 4 to find all years in which a date falls on a specific day of the week, type 5 to quit: '''))
    
    match choice:
      case 1:
        years_ago_from_x(int(input("\n Enter the year of the start date in four digits: ")), (input("\n Enter the month of the start date as a word: ")), 
                         int(input("\n Enter the day of the start date in one or two digits: ")), int(input("\n Enter the year of the end date in four digits: ")), 
                         (input("\n Enter the month of the end date as a word: ")), int(input("\n Enter the day of the end date in one or two digits: ")))
      case 2: 
        days_ago_from_x(int(input("\n Enter the year of the start date in four digits: ")), (input("\n Enter the month of the start date as a word: ")), 
                        int(input("\n Enter the day of the start date in one or two digits: ")), int(input("\n Enter the year of the end date in four digits: ")), 
                        (input("\n Enter the month of the end date as a word: ")), int(input("\n Enter the day of the end date in one or two digits: ")))
      case 3:
        weeks_ago_from_x(int(input("\n Enter the year of the start date in four digits: ")), (input("\n Enter the month of the start date as a word: ")), 
                         int(input("\n Enter the day of the start date in one or two digits: ")), int(input("\n Enter the year of the end date in four digits: ")), 
                         (input("\n Enter the month of the end date as a word: ")), int(input("\n Enter the day of the end date in one or two digits: ")))
      case 4:
        find_years(input("\n Enter the month of the date you're looking for (case insensitive): "), 
                   int(input("\n Enter the day of the date you're looking for: ")), input("\n Enter the day of the week you're looking for (case insensitive): "), 
                   int(input("\n Check all years starting from: ")), int(input("\n Check all years ending at: ")))
      case 5:
        break
      case _:
        print("\n Invalid response")
  except ValueError:
    print("\n Invalid response")
    continue
