# You're building a smart thermostat alert system:
# If the device_status is "active" 
# And temperature is > 35 -> Warm: "High temperature alert!"
# Else: "Temperature is normal."
# If device_status off -> "Device is offline."

device_status = input("Enter device status (active/off): ").lower()
if device_status == "active":
    temperature = int(input("Enter current temperature: "))
    print(f"Device status: {device_status}, Temperature: {temperature}°C")
    if(temperature > 35):
        print("High temperature alert!")
    else:
        print("Temperature is normal.")
elif device_status == "off":
    print("Device is offline.")
elif device_status != "active" and device_status != "off":
    print("Invalid device status.")
else:
    print("System error.")