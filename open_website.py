import webbrowser
def run():
    '''pathToIndexHtmlFile = ''
    websiteTestingAddress = 'file:///' + pathToIndexHtmlFile
    webbrowser.open(websiteTestingAddress, new=2)'''
    self.send_response(301)
    self.send_header('Location','https://lancastersu.co.uk/groups/badminton-society')
    self.end_headers()

if __name__ == '__main__':
    run()
