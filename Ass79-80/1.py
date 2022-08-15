import datetime
fr = datetime.datetime(1995, 5, 30)  # 2021, 6, 25
n_W = datetime.datetime.now()
print(
    f'days from {fr.date()} to {n_W.date()} ==> {(n_W-fr).days} days'.title())
