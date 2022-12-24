def add_time(start, duration, day=""):
  
  start_point = start.strip().split()
  st_per = start_point[1]
  st = start_point[0].strip().split(":")
  st_hour = int(st[0])
  st_min = st[1]
  dt = duration.strip().split(":")
  dt_hour = int(dt[0])
  dt_min = dt[1]
  
  # SUM OF MİNUTES
  day_counter = 0

  total_min = int(st_min) + int(dt_min)
  if total_min <= 59:
    new_min = total_min
  else:
  # CONVERT TO HOUR
    dt_hour += 1
    new_min = (total_min) % 60


  # Minimaze the duration hours under 24 hour(1 day)
  if dt_hour >= 24:
    day_counter += dt_hour // 24
    dt_hour = dt_hour % 24
  
  
  new_hour = st_hour
  new_per = st_per
  # SUM OF HOURS
  while dt_hour != 0:
    dt_hour -=1
    new_hour = (new_hour%12) + 1
    if new_hour == 12 and st_per == "AM":
      new_per = "PM"
    elif new_hour == 12 and st_per == "PM":
      new_per = "AM"
      day_counter +=1
    else:
      pass
  
  
  
  
  
  
  
  if day == "":
    if day_counter == 0:
      new_min = str(new_min).zfill(2)
      new_time = "{}:{} {}".format(new_hour,new_min,new_per)
      return new_time
    elif day_counter == 1:
      new_min = str(new_min).zfill(2)
      new_time = "{}:{} {}".format(new_hour,new_min,new_per) + " (next day)"
      return new_time
    else:
      new_min = str(new_min).zfill(2)
      new_time = "{}:{} {}".format(new_hour,new_min,new_per)+" ({} days later)".format(day_counter)
      return new_time
  else:
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    current_index = days.index(day.lower())
    days[current_index].capitalize()
    
    if day_counter == 0:
      new_min = str(new_min).zfill(2)
      new_time = "{}:{} {}, {}".format(new_hour,new_min,new_per,days[current_index].lower().capitalize())
      return new_time
    
    elif day_counter == 1:
      new_min = str(new_min).zfill(2)
      new_time = "{}:{} {}, {}".format(new_hour,new_min,new_per,days[current_index+1].lower().capitalize()) + " (next day)"
      return new_time
    else:
      new_min = str(new_min).zfill(2)
      index = days.index(day.lower())
      counter = day_counter
      while counter != 0:
        counter -= 1
        index += 1
        if index == 7:
          index = 0
        else:
          pass
      new_time = "{}:{} {}, {}".format(new_hour,new_min,new_per,days[index].capitalize())+" ({} days later)".format(day_counter)
      return new_time