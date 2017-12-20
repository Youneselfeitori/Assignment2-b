# Created by : Younes Elfeitori
# Created on : 27-sep-2017
# Created for : ICS3U 
# Assignment : #2
# This program displays height of an object 

import ui

def calculate_touch_up_inside (sender):
    
    #input
    time = int(view['time_textbox'].text)
    
    
    
    #process
    height = 100 - 0.5* 9.81 * time
    
    #output
    view['height_answer_label'].text = 'The height is: ' + str(height) + 'm'
    

view = ui.load_view()
view.present('full_screen')
