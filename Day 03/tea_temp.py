import time
tea_temp = 40;

while tea_temp < 100:
    print(f"Current temp is {tea_temp}")
    time.sleep(1)
    tea_temp += 15
print(f"Tea is boiled now!")