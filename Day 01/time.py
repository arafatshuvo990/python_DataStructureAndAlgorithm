import time

text = """Give me some sunshine, give me some rain
Give me another chance, I wanna grow up once again
Give me some sunshine, give me some rain
Give me another chance, I wanna grow up once again"""

for line in text.splitlines():
    print(line)
    time.sleep(3)   
