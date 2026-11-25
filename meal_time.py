def main():
   time_of_the_day = input("What time is it? ")
   hours, minutes = time_of_the_day.split(':')
   converter_tod = float(convert(hours, minutes))
   if 7.0 <= converter_tod <= 8.0:
      print('breakfast time')
   elif 12.0 <= converter_tod <= 13.0:
      print('lunch time')
   elif 18.0 <= converter_tod <= 19.0:
      print('dinner time')
   else:
      print('')

def convert(h, m):
   time_of_the_day = float(h) + float(m) / 60
   return time_of_the_day

if __name__ == "__main__":
    main()