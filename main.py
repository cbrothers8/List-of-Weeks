#Months
months = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec'
]

#Number of days in each month
days = {
  'Jan': 31,
  'Feb': 28,
  'Mar': 31,
  'Apr': 30,
  'May': 31,
  'Jun': 30,
  'Jul': 31,
  'Aug': 31,
  'Sep': 30,
  'Oct': 31,
  'Nov': 30,
  'Dec': 31
}

#The current year
leap_year = True


#Determine if leap year
def is_leap_year(year):
  if int(year) % 4 == 0:
    return True
  else:
    return False

#2,8
#9,15
#16,22
#23,29

#---------------------------------------------------------#
current_month = []

#Print Weeks in Month
def see_all_weeks(current, month):
  for i in range(len(current)):
    print('Week of ' + month + ' ' + str(current[i][0]) + ' - ' + str(current[i][1]))
  
#Determine if end of the month
def is_end(current_month):
  last_row = len(current_month) - 1
  next_Thursday = current_month[last_row][1] + 1
  if next_Thursday > days[month]:
    return False
  return next_Thursday

#Determine Days for the month
def new_dates(days, month, left):
  outer_list = []
  row = []
  if left != 0:
    row.append(left)
    new_date = left + 6
  else:
    row.append(1)
    new_date = left + 7
  row.append(new_date)
  outer_list.append(row)

  new_first = 0
  new_last = 0
  while new_last <= days[month]:
    row = []
    if new_date != 0:
      new_first = left + 7
      new_last = new_date + 7
      new_date = 0
    else:
      row.append(new_first)
      row.append(new_last)
      outer_list.append(row)
      new_first += 7
      new_last += 7

  
  return outer_list


#Find leftover days
def leftover(month, end):
  total = days[month]
  if end != False:
    difference = total - end
    left = 7 - difference
    return left
  else:
    left = 0
    return left

#-----------------------------------------#
month = ''
end = False
left = 0
ctr = 0
dates = []

#Ask Year and Determine if Leap Year
year = input('Enter Year: ')
leap_year = is_leap_year(year)

#Ask Number of Weeks and their Dates, then input into current_month List
weeks = input('Enter number of weeks in January: ')
for i in range(1, int(weeks) + 1):
  user_input = input('Enter Week ' + str(i) + ' in January Like This --> 2,8 (NO SPACES): ')
  user_input = user_input.split(',')
  user_input = [ int(x) for x in user_input]
  dates.append(user_input)
current_month.append(dates)

#Generate List of Weeks in the Year
while ctr < 12:
  if leap_year == True:
    days['Feb'] = 29
  month = months[ctr]
  print('-----------------')
  next_month = [] 

  if month == 'Jan':
    see_all_weeks(current_month[ctr], month)
    end = is_end(current_month[ctr])
    left = leftover(month, end)
    print('Week of ' + month + ' ' + str(end) + ' - ' + months[ctr + 1] + ' ' + str(left - 1))
  else:
    found_new_dates = new_dates(days, month, left)
    end = is_end(found_new_dates) 
    left = leftover(month, end)
    current_month.append(found_new_dates)
    see_all_weeks(current_month[ctr], month)
    if month == 'Dec':
      ctr += 1
      continue
    if days[month] != current_month[ctr][-1][1]:
      print('Week of ' + month + ' ' + str(end) + ' - ' + months[ctr + 1] + ' ' + str(left - 1))
  ctr += 1
