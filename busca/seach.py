
def filter_error(token):
    
    filter = "?fromDate=lasthour&timeGap=false&realtime=true&type=live&token="+token+"&limit=500&filter=%5B%7B%22name%22%3A%22uniquefilter%22%2C%22rules%22%3A%7B%22typeview%22%3A%5B%22error%22%5D%2C%22device%22%3A%5B%22STB%22%5D%2C%22state_province%22%3A%5B%22PE%22%2C%22CE%22%2C%22PI%22%2C%22BA%22%2C%22PB%22%5D%7D%7D%5D"
    
    
    return filter