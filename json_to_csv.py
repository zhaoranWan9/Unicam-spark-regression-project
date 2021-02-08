import pandas as pd

df = pd.read_json('data_json/presences.json')
df2 = pd.read_json('data_json/roomBookings.json')
df3 = pd.read_json('data_json/roomSchedule.json')
df4 = pd.read_json('data_json/rooms.json')

df.to_csv('data_csv/presences.csv')
df2.to_csv('data_csv/roomBookings.csv')
df3.to_csv('data_csv/roomSchedule.csv')
df4.to_csv('data_csv/rooms.csv')