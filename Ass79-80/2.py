import datetime
x = datetime.datetime.now()
print(x.date().strftime("%B-%d-%Y"))
print(x.date().strftime("%B,%d,%Y"))
print(x.date().strftime("%B:%d:%Y"))