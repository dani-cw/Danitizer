from os import remove
from tkinter import Tk

symbols_array = ['.', ',', '/', ';', '!', '[', ']', '{', '}', '-', '_', '=', '+', '|', '&'];

print('Bem vinde ao sanitizador do Dani! Qualquer dúvida, @dani no Slack ( ˘ ³˘)♥', '\n')
       
while 1:
    user = input('Input: ')
    if(user == 'shut down'):
        break

    splitStr = user.split()
    sent = ''
    for w in splitStr:
        wrd = ''
        for c in range(len(w)):
            if not (w[c] in symbols_array):
                if(c == 0):
                    wrd += w[c].upper()
                else:
                    wrd += w[c].lower()
        #print(wrd)
        sent += wrd    
        sent += ' '
    
    sent = sent[:-1]
    print(sent)
    
    isDone = False
    while not isDone: 
        copyClip = input('Copy to clipboard? (Y/N) ')
        if(copyClip == 'Y' or copyClip == 'y'):
            print('Copied')
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(sent)
            r.update() # now it stays on the clipboard after the window is closed
            r.destroy()
            isDone = True
        elif (copyClip == 'N' or copyClip == 'n'):
            isDone = True
     
    