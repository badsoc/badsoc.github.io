import webbrowser
def run():
    pathToIndexHtmlFile = ''
    websiteTestingAddress = 'file:///' + pathToIndexHtmlFile
    webbrowser.open(websiteTestingAddress, new=2)

if __name__ == '__main__':
    run()