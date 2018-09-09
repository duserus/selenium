import numpy as np
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
import time

def play():    
    
    try:
        rand = WebDriverWait(dr, 15).until(\
        EC.presence_of_element_located((By.NAME, "Quick-Pick")))
        mail = dr.find_element_by_xpath("//input[@placeholder\
        ='Enter Email Address Here']")
        mail.clear()
        mail.send_keys('qwer0000'+str(np.random.choice(range(30)))+'@internet.mail')
        rn = np.random.randint(1,10) 
        print ('rnd =', rn)
        for k in range(rn):
            rand.send_keys(Keys.ENTER)
        subm = dr.find_element_by_id("ticket-submit")
        subm.send_keys(Keys.ENTER) 
        subm2 = WebDriverWait(dr, 15).until(\
        EC.visibility_of_element_located((By.ID, "submitButton")))
        subm2.send_keys(Keys.ENTER)

    except Exception:
        print ("i am exception in play()")
        #dr.close()
        w2.destroy()
        w3.destroy()
        start()

def fgame():
    
    for k in range(7):
        play()
        print 'playing...'
        time.sleep(1)

def create_dr():
    
    global dr
    
    try:
        dr = webdriver.Chrome(executable_path=raw_input
        ('\33[1;33menter path to chrome driver, e.g. /home/<user>/anaconda2/bin/chromedriver: \033[0m \n'))
        print ('\033[1;32mSuccess!\033[0m\n')
        dr.get('https://www.proxysite.com/')
    
    except Exception:
        print ('\n \033[1;31m wrong path! ')
        create_dr()

def visitbl():

    global menu
    global proxy_list

    menu = dr.find_element_by_class_name('server-option')
    proxy_list = (menu.text).split('\n')[2:]
    np.random.shuffle(proxy_list)

    print ("---Got proxy list---")

    sel = Select(menu)
    sel.select_by_visible_text(proxy_list[-1])
    
    inp_field = dr.find_element_by_name('d')
    inp_field.send_keys("http://www.boxlotto.com")
    inp_field.send_keys(Keys.ENTER)
    
    dx = dr.find_element_by_class_name('intro-img')
    dx.click()

def f1():
    create_dr()
    wn2()

def f2():
    visitbl()
    wn3()
    
def destr2():
    dr.close()
    w2.destroy()
def destr3():
    dr.close()
    w3.destroy()
    
def wn2():
    w1.destroy()
    global w2
    w2 = tk.Tk()
    w2.title('win 2')
    bt2 =tk.Button(w2, text = 'visit -> boxlotto.com', command = f2)
    bt2.pack(pady=5)
    bt6 =tk.Button(w2, text = '<x>', command = destr2)
    bt6.pack(pady=5)
    w2.mainloop()

def wn3():
    
    w2.destroy(); global w3
    
    w3 = tk.Tk()
    w3.title('win 3')
    bt3 =tk.Button(w3, text = 'Play!', command = play)
    bt3.pack(pady=5)
    bt4 =tk.Button(w3, text = 'Autoplay! (7)', command = fgame)
    bt4.pack(pady=5)
    bt6 =tk.Button(w3, text = '<x>', command = destr3)
    bt6.pack(pady=5)
    w3.mainloop()

def start():    
    
    global w1; w1 = tk.Tk()
    w1.title('win 1')
    bt = tk.Button(w1, text='press to enter path -> visit proxysite.com', command = f1)
    bt.pack(pady=5)
    bt6 =tk.Button(w1, text = '<x>', command = w1.destroy)
    bt6.pack(pady=5)
    w1.mainloop()

start()
