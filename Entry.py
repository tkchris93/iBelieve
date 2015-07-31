import os

class Entry(object):
    def __init__(self, summary, author, body, tags, source, date, link="", files=""):
        self.summary = summary
        self.author = author
        self.body = body
        self.tags = tags
        self.source = source
        self.date = date
        self.link = link
        self.files = files

    def print_short(self):
        print self.summary
        
    def print_long(self):
        print self.body
        print self.author
        
    def print_write(self):
        tags = ""
        for word in self.tags:
            tags += word + " "
        tags = tags[:-1]
        
        return (self.summary + "\n" +
                self.author + "\n" +
                self.body + "\n" +
                tags + "\n" +
                self.source + "\n" +
                self.date + "\n" +
                self.link + "\n" +
                self.files + "\n")
        
    def open_files(self):
        #open associated files
        pass
        
    def open_source(self):
        #if it's a website, open up a webpage going to that website
        #if it's a source that is not online, just print the source.
        pass

    def __repr__(self): #TEMPORARY
        return self.summary 

        