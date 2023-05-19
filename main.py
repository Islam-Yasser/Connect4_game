import sys
import tkinter as tk
import alpha_beta
import minimax
def newloopAlphaBeta():
    choosingDif = tk.Tk(className="Alpha-Beta")
    l = tk.Label(choosingDif, text="choose level of difficulty", font="500")
    Easy = tk.Button(choosingDif, activebackground='blue'
                      ,background='green',text='Easy', font='large', width='10'
                      , height='5', border='8', borderwidth='5'
                      , foreground='black', relief='ridge',command=lambda: alpha_beta.playEasy())
    Normal = tk.Button(choosingDif, activebackground='blue'
                     ,bg='yellow' ,text='Normal', font='large', width='10'
                     , height='5', border='8', borderwidth='5'
                     , foreground='black', relief='ridge',command=lambda: alpha_beta.playNormal())
    hard = tk.Button(choosingDif, activebackground='blue'
                     , bg='red', text='Hard', font='large', width='10'
                     , height='5', border='8', borderwidth='5'
                     , foreground='black', relief='ridge', command=lambda: alpha_beta.playHard())
    l.pack(pady='30')
    Easy.pack(padx='200',pady='25')
    Normal.pack(padx='200',pady='25')
    hard.pack(padx='200')

def newloopMinimax():
    choosingDif = tk.Tk(className="Mini-Max")
    l = tk.Label(choosingDif, text="choose level of difficulty", font="500")
    Easy = tk.Button(choosingDif, activebackground='blue'
                      ,background='green',text='Easy', font='large', width='10'
                      , height='5', border='8', borderwidth='5'
                      , foreground='black', relief='ridge',command=lambda: minimax.playEasy())
    Normal = tk.Button(choosingDif, activebackground='blue'
                     ,bg='yellow' ,text='Normal', font='large', width='10'
                     , height='5', border='8', borderwidth='5'
                     , foreground='black', relief='ridge',command=lambda: minimax.playNormal())
    hard = tk.Button(choosingDif, activebackground='blue'
                     , bg='red', text='Hard', font='large', width='10'
                     , height='5', border='8', borderwidth='5'
                     , foreground='black', relief='ridge', command=lambda: minimax.playHard())
    l.pack(pady='30')

    Easy.pack(padx='200', pady='25')
    Normal.pack(padx='200', pady='25')
    hard.pack(padx='200')


top = tk.Tk(className='Connect four')
# Create label
l = tk.Label(top, text="Welcome to connect four",font="500")
startAlpha = tk.Button(master=top, activebackground='green'
                       , text='Start With Alpha-Beta', font='large', width='25'
                       , height='5', border='8', borderwidth='5'
                       , foreground='black', background='yellow', relief='ridge', command=lambda: newloopAlphaBeta())
startMinimax = tk.Button(master=top, activebackground='green'
                       , text='Start With minimax', font='large', width='25'
                       , height='5', border='8', borderwidth='5'
                       , foreground='black', background='blue', relief='ridge', command=lambda: newloopMinimax())

exit= tk.Button(master=top, activebackground='green'
              ,text='Exit',font='large',width='25'
              ,height='5',border='8',borderwidth='5'
              ,foreground='white',background='black',relief='ridge',command=lambda:sys.exit())

l.pack(pady='30')
startAlpha.pack(padx='200',pady='100')
startMinimax.pack(padx='200')
exit.pack(pady='100')
top.mainloop()
