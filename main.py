from selenium import webdriver
import time

offset = 7  # time for animation
driver = webdriver.Firefox()
driver.get("https://www.inwebson.com/demo/cross-the-bridge/")

characters = [{
    "name": "GINA",
    "time": 1,
    "char": 'A'
}, {
    "name": "KEN",
    "time": 2,
    "char": 'B'
}, {
    "name": "LISA",
    "time": 4,
    "char": 'C'
}, {
    "name": "TOM",
    "time": 6,
    "char": 'D'
}, {
    "name": "CINDY",
    "time": 8,
    "char": 'E'
}, {
    "name": "OMAN",
    "time": 12,
    "char": 'F'
}]


def move(buttons):
    if(len(buttons)<=0 or len(buttons)>2):
        print("Only first valid entries will be considered")
    for button in buttons:
        el = driver.find_element_by_id(f'thumb{button+1}')
        print(f"Moving {characters[button]['char']} : {characters[button]['name']} will take {characters[button]['time']}s")
        el.click()
    t = None
    # finding max time to cross bridge
    if(len(buttons)==2): 
        t = max(characters[buttons[0]]['time'],characters[buttons[1]]['time'])
    else:
        t = characters[buttons[0]]['time']
    # click go button
    driver.find_element_by_id("btn").click()
    print(f"Characters will take {t}s, but intentional wait of {t+offset}s added")
    time.sleep(t + offset)


# waiting to load the game
time.sleep(3)

# move 0 and 1
move([0,1])

# call 0 back
move([0])

# move 4 and 5
move([4,5])

# call 1 back
move([1])

# move 0 and 1
move([0,1])

# call 0 back
move([0])

# move 2 and 3
move([2,3])

# call 1 back
move([1])

# move 0 and 1
move([1,0])

print("Congratulation!")
