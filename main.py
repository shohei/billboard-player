import billboard
import tornado.ioloop
import tornado.web

def getHotOneHundred():
    chart = billboard.ChartData('hot-100')
    songs = []
    for c in chart:
        songs.append(c)
    return songs

def playSongs():
    #wip
    pass

def MainHandler():
    def get(self):
        self.renderFile("")
        songs = getHotOneHundred()
        playSongs(songs)

if __name__=="__main__":
    application = tornado.web.Application([
        (r"/",MainHandler)    
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


