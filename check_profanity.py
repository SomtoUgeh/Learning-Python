import urllib

def read_text():
    quotes = open('/Users/mac/Desktop/movie_quotes.txt')
    content_files = quotes.read()
    quotes.close()
    profanity(content_files)
    
def profanity(text):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text)
    output = connection.read()
    connection.close()
    if 'true' in output:
        print ('Profanity Alert')
    elif 'false' in output:
        print ('Document is clean')
    else:
        print ('Could not scan document properly')

read_text()



