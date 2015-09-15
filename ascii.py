import random, os, sys, time
#Animate some ASCII art (thanks Philip: http://stackoverflow.com/a/2785568/1347629)
def draw_to_screen(content):
    clear_console = 'clear' if os.name == 'posix' else 'CLS'
    os.system(clear_console)
    sys.stdout.write(content)
    sys.stdout.flush()
    time.sleep(0.2)

def load_font():
    f=open("bigmoney.txt", 'r')
    result = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
        image = ""
        for j in range(11):
            image += f.readline()
        result[letter] = image
    return result

letter_dict = load_font()
for letter in "ANDY IS THE GREATEST":
    draw_to_screen(letter_dict[letter])