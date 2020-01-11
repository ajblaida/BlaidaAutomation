from phue import Bridge

b = Bridge('192.168.0.109')

b.connect()

b.get_api()
light_names = b.get_light_objects('name')
print(light_names)
userin = input("value")
while userin != "quit":
	brightness = int(userin)
	if brightness < 0:
		brightness = 0
	elif brightness > 254:
		brightness = 254
	
	isOn = True if brightness > 0 else False

	b.set_group('Living Room', 'on', isOn)
	if isOn:
		b.set_group('Living Room', 'bri', brightness)
	userin = input("value")