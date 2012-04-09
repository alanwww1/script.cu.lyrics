import os
import utilities
import xbmc
import sys

__cwd__     = sys.modules[ "__main__" ].__cwd__
__profile__ = sys.modules[ "__main__" ].__profile__

class Song:
    def __init__( self ):
        self.artist = ""
        self.title = ""

    def __str__(self):
        return "Artist: %s, Title: %s" % ( self.artist, self.title)
    
    def __cmp__(self, song):
        if (self.artist != song.artist):
            return cmp(self.artist, song.artist)
        else:
            return cmp(self.title, song.title)
    
    def sanitize(self, str):
        return str.replace( "\\", "_" ).replace( "/", "_" ).replace(":","_").replace("?","_").replace("!","_")
    
    def path(self):
        return unicode( os.path.join( __profile__, "lyrics", self.sanitize(self.artist), self.sanitize(self.title) + ".txt" ), "utf-8" )
    
    @staticmethod
    def current():
        song = Song.by_offset(0)
        print "Current Song: %s:%s" % (song.artist, song.title)
        return song

    @staticmethod
    def next():
        song = Song.by_offset(1)
        print "Next Song: %s:%s" % (song.artist, song.title)
        
        return song

    @staticmethod
    def by_offset(offset = 0):
        song = Song()
    	if offset > 0:
            offset_str = ".offset(%i)" % offset
        else:
            offset_str = ""	
        song.title = xbmc.getInfoLabel( "MusicPlayer%s.Title" % offset_str)
        song.title = utilities.deAccent(song.title)
        song.artist = xbmc.getInfoLabel( "MusicPlayer%s.Artist" % offset_str)
        song.artist = utilities.deAccent(song.artist)
        
        return song
