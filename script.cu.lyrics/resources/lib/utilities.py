#-*- coding: UTF-8 -*-
import sys
import xbmc
import unicodedata

__scriptname__ = sys.modules[ "__main__" ].__scriptname__

# special button codes
SELECT_ITEM = ( 11, 256, 61453, )
EXIT_SCRIPT = ( 247, 275, 61467, )
CANCEL_DIALOG  = ( 9, 10, 92, 216, 247, 257, 275, 61467, 61448, )
GET_EXCEPTION = ( 216, 260, 61448, )
SETTINGS_MENU = ( 229, 259, 261, 61533, )
SHOW_CREDITS = ( 195, 274, 61507, )
MOVEMENT_UP = ( 166, 270, 61478, )
MOVEMENT_DOWN = ( 167, 271, 61480, )

# special action codes
ACTION_SELECT_ITEM = ( 7, )
ACTION_EXIT_SCRIPT = ( 10, )
ACTION_CANCEL_DIALOG = ACTION_EXIT_SCRIPT + ( 9, )
ACTION_GET_EXCEPTION = ( 0, 11 )
ACTION_SETTINGS_MENU = ( 117, )
ACTION_SHOW_CREDITS = ( 122, )
ACTION_MOVEMENT_UP = ( 3, )
ACTION_MOVEMENT_DOWN = ( 4, )


def log(msg):
    xbmc.log("### [%s] - %s" % (__scriptname__,msg,),level=xbmc.LOGDEBUG ) 

def deAccent(str):
    return unicodedata.normalize('NFKD', unicode(unicode(str, 'utf-8'))).encode('ascii','ignore')

def replace(string):
    replace_char = [" ",",","'","&","and"]
    for char in replace_char:
        string.replace(char,"-")
    return string