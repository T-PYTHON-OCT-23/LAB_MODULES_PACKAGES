from datetime import date
## extract current local date
def current_date():
 today = date.today()
 # print("Today's date:", current_date)
# show date in different format
 today = today.strftime("%d/%m/%Y")
 print("Today's date:", today)