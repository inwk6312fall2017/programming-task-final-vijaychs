from weather import Weather
weather = Weather()

location = weather.lookup_by_location('halifax')
condition = location.condition()

# Get weather forecasts for the upcoming days.
#for forecasts in location.forecast():
#    print (forecasts['text'])
#    print (forecasts['date'])
#    print (forecasts['high'])
#    print (forecasts['low'])


max_temp = max(forecasts['high'] for forecasts in location.forecast())
print("MAX temp on next 5 days will be", max_temp)

for forecasts in location.forecast():
	if max_temp == forecasts['high']:
		print("And it falls on",forecasts['day'])


min_temp = min(forecasts['high'] for forecasts in location.forecast())
print("MIN temp on next 5 days will be", min_temp)

for forecasts in location.forecast():
	if min_temp == forecasts['low']:
		
		print("And it falls on",forecasts['day'])
for forecasts in location.forecast():
	if forecasts['text'] == "Showers":
		print("It will rain on", forecasts['day'])

