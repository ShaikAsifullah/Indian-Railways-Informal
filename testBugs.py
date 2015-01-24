'''
Created on 06-Oct-2013

@author: Kashaj
'''


"""This file is just for testing 
It is of no actual use in PROJECT"""

import os

def do():
    save_path = r'C:/Users/kashaj/Desktop/proj/data/schedule/'
    text = 'This'
    text += '.txt'
    completeName = os.path.join(save_path, text)
    f = open(completeName,'w')
    f.write(text)
    f.close
    print 'Done'
   
if __name__ == '__main__':
    do()
    