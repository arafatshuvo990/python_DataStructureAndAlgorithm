# device_status = input(("What is the current status: ")).lower()
# device_temp = input(("what is the current temp: "))

# if device_status == "active" and device_temp >= 35:
#     print(f"WARN: hign temparature alert")
# elif device_status != "active":
#     print(f"device is offline")
# else:
#     print(f"Device temp is normal")

device_status = "active";
device_temp = 36;

if device_status == 'active':
    if device_temp > 35:
        print(f"WARN: hign temparature alert")
    else:
        print(f"Device temp is normal")
else:
    print(f"device is offline")
    