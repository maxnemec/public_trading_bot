from connectedGUI import inputObject

def retrieve_price_history(inputObject):

    resource_url = "https://api.tdameritrade.com/v1/marketdata/BABA/pricehistory"
    print("Welcome to TradeMaster200. Please enter a ticker symbol and data paramaters. (You may type in help at any time for a list of commands and defaults) ")
    
    resource_url += "?periodType=" + inputObject.periodType
    resource_url = resource_url + "&period=" + inputObject.period
    resource_url = resource_url + "&frequencyType=" + inputObject.frequencyType
    resource_url = resource_url + "&frequency=" + inputObject.frequency

    print(resource_url)
    return resource_url