class common(object):
    """description of class"""
    def generateData(dat):
       updateDic = {
            "Cartisian.position.x":dat['Cartisian[position][x]'],
            "Cartisian.position.y":dat['Cartisian[position][y]'],
            "Cartisian.position.z":dat['Cartisian[position][z]'],
            "Cartisian.orientation.x":dat['Cartisian[orientation][x]'],
            "Cartisian.orientation.y":dat['Cartisian[orientation][y]'],
            "Cartisian.orientation.z":dat['Cartisian[orientation][z]'],
            "Cartisian.orientation.w":dat['Cartisian[orientation][w]'],
            "FriendlyName":dat["FriendlyName"],
            "Order":dat["Order"],
            "Speed":dat["Speed"],
             "Action":dat["Action"]
        }
       return updateDic

    def generateData2(dat):
       updateDic = {
            "FriendlyName":dat["FriendlyName"],
            "Order":dat["Order"],
            "Speed":dat["Speed"],
             "Action":dat["Action"],
             "Name":dat["Name"]

        }
       updateDic["Cartisian"] = {}
       updateDic["Cartisian"]["position"] = {}
       updateDic["Cartisian"]["orientation"] = {}
       updateDic["Cartisian"]["position"]["x"] = dat['Cartisian[position][x]']
       updateDic["Cartisian"]["position"]["y"] = dat['Cartisian[position][y]']
       updateDic["Cartisian"]["position"]["z"] = dat['Cartisian[position][z]']
       updateDic["Cartisian"]["orientation"]["x"] = dat['Cartisian[orientation][x]']
       updateDic["Cartisian"]["orientation"]["y"] = dat['Cartisian[orientation][y]']
       updateDic["Cartisian"]["orientation"]["z"] = dat['Cartisian[orientation][z]']
       updateDic["Cartisian"]["orientation"]["w"] = dat['Cartisian[orientation][w]']

       return updateDic
