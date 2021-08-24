import datetime

data = datetime.datetime.now()
print(data)
print(data.strftime("%d/%m/%Y %H:%M:%S"))
print(data.strftime("%d/%m/%Y"))
print(data.strftime("%H:%M:%S"))
print(data.strftime("%Y-%m-%d"))

print(f'Data de Hoje: {datetime.datetime.now().strftime("%d/%m/%Y")}')
proxima_semana = datetime.datetime.now() + datetime.timedelta(weeks=2)
print(f'Semana que vem sera: {proxima_semana.strftime("%d/%m/%Y")}')
