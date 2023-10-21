import datetime
def current_date():
    date=datetime.date.today()
    date=date.strftime("%d %B %Y")
    print(date)
