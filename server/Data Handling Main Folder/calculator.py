import pandas as pd

# =============================================================================
# %reset -f
# =============================================================================

dataset = pd.read_csv("allMatches.csv")

team2008 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0}
team2009 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0}
team2010 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0}
team2011 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KTK":0, "KXIP":0, "MI":0, "PW":0, "RCB":0, "RR":0}
team2012 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "PW":0, "RCB":0, "RR":0}
team2013 = {"CSK":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "PW":0, "RCB":0, "RR":0, "SH":0}
team2014 = {"CSK":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0, "SH":0}
team2015 = {"CSK":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0, "SH":0}
team2016 = {"DD":0, "GL":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RPS":0, "SH":0}
team2017 = {"DD":0, "GL":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RPS":0, "SH":0}


# Calculating The Total Match per Team per Season
for i in range(0,640):
    if(dataset["season"][i]==2008):
        if((dataset["home_team"][i]=="CSK" or dataset["away_team"][i]=="CSK")):
            team2008["CSK"]+=1
        if((dataset["home_team"][i]=="DC" or dataset["away_team"][i]=="DC")):
            team2008["DC"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2008["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2008["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2008["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2008["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2008["RCB"]+=1
        if((dataset["home_team"][i]=="RR" or dataset["away_team"][i]=="RR")):
            team2008["RR"]+=1
    elif(dataset["season"][i]==2009):
        if((dataset["home_team"][i]=="CSK" or dataset["away_team"][i]=="CSK")):
            team2009["CSK"]+=1
        if((dataset["home_team"][i]=="DC" or dataset["away_team"][i]=="DC")):
            team2009["DC"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2009["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2009["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2009["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2009["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2009["RCB"]+=1
        if((dataset["home_team"][i]=="RR" or dataset["away_team"][i]=="RR")):
            team2009["RR"]+=1
    elif(dataset["season"][i]==2010):
        if((dataset["home_team"][i]=="CSK" or dataset["away_team"][i]=="CSK")):
            team2010["CSK"]+=1
        if((dataset["home_team"][i]=="DC" or dataset["away_team"][i]=="DC")):
            team2010["DC"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2010["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2010["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2010["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2010["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2010["RCB"]+=1
        if((dataset["home_team"][i]=="RR" or dataset["away_team"][i]=="RR")):
            team2010["RR"]+=1
    elif(dataset["season"][i]==2011):
        if((dataset["home_team"][i]=="CSK" or dataset["away_team"][i]=="CSK")):
            team2011["CSK"]+=1
        if((dataset["home_team"][i]=="DC" or dataset["away_team"][i]=="DC")):
            team2011["DC"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2011["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2011["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2011["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2011["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2011["RCB"]+=1
        if((dataset["home_team"][i]=="RR" or dataset["away_team"][i]=="RR")):
            team2011["RR"]+=1
        if((dataset["home_team"][i]=="KTK" or dataset["away_team"][i]=="KTK")):
            team2011["KTK"]+=1
        if((dataset["home_team"][i]=="PW" or dataset["away_team"][i]=="PW")):
            team2011["PW"]+=1
    elif(dataset["season"][i]==2012):
        if((dataset["home_team"][i]=="CSK" or dataset["away_team"][i]=="CSK")):
            team2012["CSK"]+=1
        if((dataset["home_team"][i]=="DC" or dataset["away_team"][i]=="DC")):
            team2012["DC"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2012["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2012["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2012["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2012["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2012["RCB"]+=1
        if((dataset["home_team"][i]=="RR" or dataset["away_team"][i]=="RR")):
            team2012["RR"]+=1
        if((dataset["home_team"][i]=="PW" or dataset["away_team"][i]=="PW")):
            team2012["PW"]+=1
    elif(dataset["season"][i]==2013):
        if((dataset["home_team"][i]=="CSK" or dataset["away_team"][i]=="CSK")):
            team2013["CSK"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2013["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2013["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2013["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2013["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2013["RCB"]+=1
        if((dataset["home_team"][i]=="RR" or dataset["away_team"][i]=="RR")):
            team2013["RR"]+=1
        if((dataset["home_team"][i]=="PW" or dataset["away_team"][i]=="PW")):
            team2013["PW"]+=1
        if((dataset["home_team"][i]=="SH" or dataset["away_team"][i]=="SH")):
            team2013["SH"]+=1
    elif(dataset["season"][i]==2014):
        if((dataset["home_team"][i]=="CSK" or dataset["away_team"][i]=="CSK")):
            team2014["CSK"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2014["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2014["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2014["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2014["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2014["RCB"]+=1
        if((dataset["home_team"][i]=="RR" or dataset["away_team"][i]=="RR")):
            team2014["RR"]+=1
        if((dataset["home_team"][i]=="SH" or dataset["away_team"][i]=="SH")):
            team2014["SH"]+=1
    elif(dataset["season"][i]==2015):
        if((dataset["home_team"][i]=="CSK" or dataset["away_team"][i]=="CSK")):
            team2015["CSK"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2015["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2015["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2015["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2015["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2015["RCB"]+=1
        if((dataset["home_team"][i]=="RR" or dataset["away_team"][i]=="RR")):
            team2015["RR"]+=1
        if((dataset["home_team"][i]=="SH" or dataset["away_team"][i]=="SH")):
            team2015["SH"]+=1
    elif(dataset["season"][i]==2016):
        if((dataset["home_team"][i]=="GL" or dataset["away_team"][i]=="GL")):
            team2016["GL"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2016["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2016["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2016["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2016["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2016["RCB"]+=1
        if((dataset["home_team"][i]=="RPS" or dataset["away_team"][i]=="RPS")):
            team2016["RPS"]+=1
        if((dataset["home_team"][i]=="SH" or dataset["away_team"][i]=="SH")):
            team2016["SH"]+=1
    elif(dataset["season"][i]==2017):
        if((dataset["home_team"][i]=="GL" or dataset["away_team"][i]=="GL")):
            team2017["GL"]+=1
        if((dataset["home_team"][i]=="DD" or dataset["away_team"][i]=="DD")):
            team2017["DD"]+=1
        if((dataset["home_team"][i]=="KKR" or dataset["away_team"][i]=="KKR")):
            team2017["KKR"]+=1
        if((dataset["home_team"][i]=="KXIP" or dataset["away_team"][i]=="KXIP")):
            team2017["KXIP"]+=1
        if((dataset["home_team"][i]=="MI" or dataset["away_team"][i]=="MI")):
            team2017["MI"]+=1
        if((dataset["home_team"][i]=="RCB" or dataset["away_team"][i]=="RCB")):
            team2017["RCB"]+=1
        if((dataset["home_team"][i]=="RPS" or dataset["away_team"][i]=="RPS")):
            team2017["RPS"]+=1
        if((dataset["home_team"][i]=="SH" or dataset["away_team"][i]=="SH")):
            team2017["SH"]+=1
    
# Inserting The Total Matche per Team per Season into dataset
for i in range(0,640):
    if(dataset["season"][i]==2008):
        if((dataset["home_team"][i]=="CSK")):
            dataset["totMatch_home"][i]=team2008["CSK"]
        if(( dataset["away_team"][i]=="CSK")):
            dataset["totMatch_away"][i]=team2008["CSK"]
        if((dataset["home_team"][i]=="DC")):
            dataset["totMatch_home"][i]=team2008["DC"]
        if((dataset["away_team"][i]=="DC")):
            dataset["totMatch_away"][i]=team2008["DC"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2008["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2008["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2008["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2008["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2008["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2008["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2008["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2008["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2008["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2008["RCB"]
        if((dataset["home_team"][i]=="RR")):
            dataset["totMatch_home"][i]=team2008["RR"]
        if((dataset["away_team"][i]=="RR")):
            dataset["totMatch_away"][i]=team2008["RR"]
    elif(dataset["season"][i]==2009):
        if((dataset["home_team"][i]=="CSK")):
            dataset["totMatch_home"][i]=team2009["CSK"]
        if(( dataset["away_team"][i]=="CSK")):
            dataset["totMatch_away"][i]=team2009["CSK"]
        if((dataset["home_team"][i]=="DC")):
            dataset["totMatch_home"][i]=team2009["DC"]
        if((dataset["away_team"][i]=="DC")):
            dataset["totMatch_away"][i]=team2009["DC"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2009["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2009["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2009["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2009["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2009["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2009["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2009["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2009["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2009["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2009["RCB"]
        if((dataset["home_team"][i]=="RR")):
            dataset["totMatch_home"][i]=team2009["RR"]
        if((dataset["away_team"][i]=="RR")):
            dataset["totMatch_away"][i]=team2009["RR"]
    elif(dataset["season"][i]==2010):
        if((dataset["home_team"][i]=="CSK")):
            dataset["totMatch_home"][i]=team2010["CSK"]
        if(( dataset["away_team"][i]=="CSK")):
            dataset["totMatch_away"][i]=team2010["CSK"]
        if((dataset["home_team"][i]=="DC")):
            dataset["totMatch_home"][i]=team2010["DC"]
        if((dataset["away_team"][i]=="DC")):
            dataset["totMatch_away"][i]=team2010["DC"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2010["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2010["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2010["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2010["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2010["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2010["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2010["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2010["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2010["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2010["RCB"]
        if((dataset["home_team"][i]=="RR")):
            dataset["totMatch_home"][i]=team2010["RR"]
        if((dataset["away_team"][i]=="RR")):
            dataset["totMatch_away"][i]=team2010["RR"]
    elif(dataset["season"][i]==2011):
        if((dataset["home_team"][i]=="CSK")):
            dataset["totMatch_home"][i]=team2011["CSK"]
        if(( dataset["away_team"][i]=="CSK")):
            dataset["totMatch_away"][i]=team2011["CSK"]
        if((dataset["home_team"][i]=="DC")):
            dataset["totMatch_home"][i]=team2011["DC"]
        if((dataset["away_team"][i]=="DC")):
            dataset["totMatch_away"][i]=team2011["DC"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2011["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2011["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2011["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2011["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2011["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2011["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2011["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2011["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2011["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2011["RCB"]
        if((dataset["home_team"][i]=="RR")):
            dataset["totMatch_home"][i]=team2011["RR"]
        if((dataset["away_team"][i]=="RR")):
            dataset["totMatch_away"][i]=team2011["RR"]
        if((dataset["home_team"][i]=="KTK")):
            dataset["totMatch_home"][i]=team2011["KTK"]
        if((dataset["away_team"][i]=="KTK")):
            dataset["totMatch_away"][i]=team2011["KTK"]
        if((dataset["home_team"][i]=="PW")):
            dataset["totMatch_home"][i]=team2011["PW"]
        if((dataset["away_team"][i]=="PW")):
            dataset["totMatch_away"][i]=team2011["PW"]
    elif(dataset["season"][i]==2012):
        if((dataset["home_team"][i]=="CSK")):
            dataset["totMatch_home"][i]=team2012["CSK"]
        if(( dataset["away_team"][i]=="CSK")):
            dataset["totMatch_away"][i]=team2012["CSK"]
        if((dataset["home_team"][i]=="DC")):
            dataset["totMatch_home"][i]=team2012["DC"]
        if((dataset["away_team"][i]=="DC")):
            dataset["totMatch_away"][i]=team2012["DC"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2012["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2012["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2012["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2012["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2012["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2012["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2012["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2012["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2012["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2012["RCB"]
        if((dataset["home_team"][i]=="RR")):
            dataset["totMatch_home"][i]=team2012["RR"]
        if((dataset["away_team"][i]=="RR")):
            dataset["totMatch_away"][i]=team2012["RR"]
        if((dataset["home_team"][i]=="PW")):
            dataset["totMatch_home"][i]=team2012["PW"]
        if((dataset["away_team"][i]=="PW")):
            dataset["totMatch_away"][i]=team2012["PW"]
    elif(dataset["season"][i]==2013):
        if((dataset["home_team"][i]=="CSK")):
            dataset["totMatch_home"][i]=team2013["CSK"]
        if(( dataset["away_team"][i]=="CSK")):
            dataset["totMatch_away"][i]=team2013["CSK"]
        if((dataset["home_team"][i]=="SH")):
            dataset["totMatch_home"][i]=team2013["SH"]
        if((dataset["away_team"][i]=="SH")):
            dataset["totMatch_away"][i]=team2013["SH"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2013["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2013["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2013["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2013["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2013["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2013["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2013["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2013["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2013["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2013["RCB"]
        if((dataset["home_team"][i]=="RR")):
            dataset["totMatch_home"][i]=team2013["RR"]
        if((dataset["away_team"][i]=="RR")):
            dataset["totMatch_away"][i]=team2013["RR"]
        if((dataset["home_team"][i]=="PW")):
            dataset["totMatch_home"][i]=team2013["PW"]
        if((dataset["away_team"][i]=="PW")):
            dataset["totMatch_away"][i]=team2013["PW"]
    elif(dataset["season"][i]==2014):
        if((dataset["home_team"][i]=="CSK")):
            dataset["totMatch_home"][i]=team2014["CSK"]
        if(( dataset["away_team"][i]=="CSK")):
            dataset["totMatch_away"][i]=team2014["CSK"]
        if((dataset["home_team"][i]=="SH")):
            dataset["totMatch_home"][i]=team2014["SH"]
        if((dataset["away_team"][i]=="SH")):
            dataset["totMatch_away"][i]=team2014["SH"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2014["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2014["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2014["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2014["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2014["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2014["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2014["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2014["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2014["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2014["RCB"]
        if((dataset["home_team"][i]=="RR")):
            dataset["totMatch_home"][i]=team2014["RR"]
        if((dataset["away_team"][i]=="RR")):
            dataset["totMatch_away"][i]=team2014["RR"]
    elif(dataset["season"][i]==2015):
        if((dataset["home_team"][i]=="CSK")):
            dataset["totMatch_home"][i]=team2015["CSK"]
        if(( dataset["away_team"][i]=="CSK")):
            dataset["totMatch_away"][i]=team2015["CSK"]
        if((dataset["home_team"][i]=="SH")):
            dataset["totMatch_home"][i]=team2015["SH"]
        if((dataset["away_team"][i]=="SH")):
            dataset["totMatch_away"][i]=team2015["SH"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2015["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2015["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2015["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2015["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2015["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2015["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2015["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2015["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2015["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2015["RCB"]
        if((dataset["home_team"][i]=="RR")):
            dataset["totMatch_home"][i]=team2015["RR"]
        if((dataset["away_team"][i]=="RR")):
            dataset["totMatch_away"][i]=team2015["RR"]
    elif(dataset["season"][i]==2016):
        if((dataset["home_team"][i]=="GL")):
            dataset["totMatch_home"][i]=team2016["GL"]
        if(( dataset["away_team"][i]=="GL")):
            dataset["totMatch_away"][i]=team2016["GL"]
        if((dataset["home_team"][i]=="SH")):
            dataset["totMatch_home"][i]=team2016["SH"]
        if((dataset["away_team"][i]=="SH")):
            dataset["totMatch_away"][i]=team2016["SH"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2016["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2016["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2016["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2016["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2016["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2016["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2016["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2016["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2016["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2016["RCB"]
        if((dataset["home_team"][i]=="RPS")):
            dataset["totMatch_home"][i]=team2016["RPS"]
        if((dataset["away_team"][i]=="RPS")):
            dataset["totMatch_away"][i]=team2016["RPS"]
    elif(dataset["season"][i]==2017):
        if((dataset["home_team"][i]=="GL")):
            dataset["totMatch_home"][i]=team2017["GL"]
        if(( dataset["away_team"][i]=="GL")):
            dataset["totMatch_away"][i]=team2017["GL"]
        if((dataset["home_team"][i]=="SH")):
            dataset["totMatch_home"][i]=team2017["SH"]
        if((dataset["away_team"][i]=="SH")):
            dataset["totMatch_away"][i]=team2017["SH"]
        if((dataset["home_team"][i]=="DD")):
            dataset["totMatch_home"][i]=team2017["DD"]
        if((dataset["away_team"][i]=="DD")):
            dataset["totMatch_away"][i]=team2017["DD"]
        if((dataset["home_team"][i]=="KKR")):
            dataset["totMatch_home"][i]=team2017["KKR"]
        if((dataset["away_team"][i]=="KKR")):
            dataset["totMatch_away"][i]=team2017["KKR"]
        if((dataset["home_team"][i]=="KXIP")):
            dataset["totMatch_home"][i]=team2017["KXIP"]
        if((dataset["away_team"][i]=="KXIP")):
            dataset["totMatch_away"][i]=team2017["KXIP"]
        if((dataset["home_team"][i]=="MI")):
            dataset["totMatch_home"][i]=team2017["MI"]
        if((dataset["away_team"][i]=="MI")):
            dataset["totMatch_away"][i]=team2017["MI"]
        if((dataset["home_team"][i]=="RCB")):
            dataset["totMatch_home"][i]=team2017["RCB"]
        if((dataset["away_team"][i]=="RCB")):
            dataset["totMatch_away"][i]=team2017["RCB"]
        if((dataset["home_team"][i]=="RPS")):
            dataset["totMatch_home"][i]=team2017["RPS"]
        if((dataset["away_team"][i]=="RPS")):
            dataset["totMatch_away"][i]=team2017["RPS"]
dataset.to_csv("allMatches_modified.csv")


# inserting Total player point sum in DATAset
dataset1 = pd.read_csv("allMatches_modified.csv")
dataset2 = pd.read_csv("tppsswCSV.csv")

pts2008 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0}
pts2009 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0}
pts2010 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0}
pts2011 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KTK":0, "KXIP":0, "MI":0, "PW":0, "RCB":0, "RR":0}
pts2012 = {"CSK":0, "DC":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "PW":0, "RCB":0, "RR":0}
pts2013 = {"CSK":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "PW":0, "RCB":0, "RR":0, "SH":0}
pts2014 = {"CSK":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0, "SH":0}
pts2015 = {"CSK":0, "DD":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RR":0, "SH":0}
pts2016 = {"DD":0, "GL":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RPS":0, "SH":0}
pts2017 = {"DD":0, "GL":0, "KKR":0, "KXIP":0, "MI":0, "RCB":0, "RPS":0, "SH":0}

# Storing pts data into dictionary
for i in range(0,100):
    if(dataset2["season"][i]==2008):
        if(dataset2["team"][i]=="CSK"):
            pts2008["CSK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DC"):
            pts2008["DC"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2008["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2008["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2008["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2008["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2008["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RR"):
            pts2008["RR"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2009):
        if(dataset2["team"][i]=="CSK"):
            pts2009["CSK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DC"):
            pts2009["DC"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2009["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2009["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2009["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2009["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2009["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RR"):
            pts2009["RR"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2010):
        if(dataset2["team"][i]=="CSK"):
            pts2010["CSK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DC"):
            pts2010["DC"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2010["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2010["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2010["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2010["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2010["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RR"):
            pts2010["RR"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2011):
        if(dataset2["team"][i]=="CSK"):
            pts2011["CSK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DC"):
            pts2011["DC"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2011["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2011["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2011["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2011["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2011["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RR"):
            pts2011["RR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KTK"):
            pts2011["KTK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="PW"):
            pts2011["PW"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2012):
        if(dataset2["team"][i]=="CSK"):
            pts2012["CSK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DC"):
            pts2012["DC"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2012["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2012["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2012["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2012["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2012["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RR"):
            pts2012["RR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="PW"):
            pts2012["PW"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2013):
        if(dataset2["team"][i]=="CSK"):
            pts2013["CSK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="SH"):
            pts2013["SH"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2013["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2013["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2013["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2013["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2013["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RR"):
            pts2013["RR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="PW"):
            pts2013["PW"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2014):
        if(dataset2["team"][i]=="CSK"):
            pts2014["CSK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="SH"):
            pts2014["SH"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2014["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2014["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2014["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2014["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2014["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RR"):
            pts2014["RR"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2015):
        if(dataset2["team"][i]=="CSK"):
            pts2015["CSK"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="SH"):
            pts2015["SH"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2015["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2015["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2015["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2015["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2015["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RR"):
            pts2015["RR"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2016):
        if(dataset2["team"][i]=="GL"):
            pts2016["GL"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="SH"):
            pts2016["SH"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2016["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2016["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2016["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2016["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2016["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RPS"):
            pts2016["RPS"] = dataset2["teamPlayerPtsSum"][i]
    elif(dataset2["season"][i]==2017):
        if(dataset2["team"][i]=="GL"):
            pts2017["GL"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="SH"):
            pts2017["SH"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="DD"):
            pts2017["DD"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KKR"):
            pts2017["KKR"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="KXIP"):
            pts2017["KXIP"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="MI"):
            pts2017["MI"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RCB"):
            pts2017["RCB"] = dataset2["teamPlayerPtsSum"][i]
        if(dataset2["team"][i]=="RPS"):
            pts2017["RPS"] = dataset2["teamPlayerPtsSum"][i]
            
#Inserting The Data into database
for i in range(0,640):
    if(dataset1["season"][i]==2008):
        if((dataset1["home_team"][i]=="CSK")):
            dataset1["playerPtsSum_home"][i]=pts2008["CSK"]
        if(( dataset1["away_team"][i]=="CSK")):
            dataset1["playerPtsSum_away"][i]=pts2008["CSK"]
        if((dataset1["home_team"][i]=="DC")):
            dataset1["playerPtsSum_home"][i]=pts2008["DC"]
        if((dataset1["away_team"][i]=="DC")):
            dataset1["playerPtsSum_away"][i]=pts2008["DC"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2008["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2008["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2008["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2008["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2008["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2008["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2008["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2008["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2008["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2008["RCB"]
        if((dataset1["home_team"][i]=="RR")):
            dataset1["playerPtsSum_home"][i]=pts2008["RR"]
        if((dataset1["away_team"][i]=="RR")):
            dataset1["playerPtsSum_away"][i]=pts2008["RR"]
    elif(dataset1["season"][i]==2009):
        if((dataset1["home_team"][i]=="CSK")):
            dataset1["playerPtsSum_home"][i]=pts2009["CSK"]
        if(( dataset1["away_team"][i]=="CSK")):
            dataset1["playerPtsSum_away"][i]=pts2009["CSK"]
        if((dataset1["home_team"][i]=="DC")):
            dataset1["playerPtsSum_home"][i]=pts2009["DC"]
        if((dataset1["away_team"][i]=="DC")):
            dataset1["playerPtsSum_away"][i]=pts2009["DC"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2009["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2009["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2009["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2009["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2009["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2009["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2009["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2009["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2009["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2009["RCB"]
        if((dataset1["home_team"][i]=="RR")):
            dataset1["playerPtsSum_home"][i]=pts2009["RR"]
        if((dataset1["away_team"][i]=="RR")):
            dataset1["playerPtsSum_away"][i]=pts2009["RR"]
    elif(dataset1["season"][i]==2010):
        if((dataset1["home_team"][i]=="CSK")):
            dataset1["playerPtsSum_home"][i]=pts2010["CSK"]
        if(( dataset1["away_team"][i]=="CSK")):
            dataset1["playerPtsSum_away"][i]=pts2010["CSK"]
        if((dataset1["home_team"][i]=="DC")):
            dataset1["playerPtsSum_home"][i]=pts2010["DC"]
        if((dataset1["away_team"][i]=="DC")):
            dataset1["playerPtsSum_away"][i]=pts2010["DC"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2010["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2010["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2010["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2010["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2010["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2010["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2010["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2010["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2010["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2010["RCB"]
        if((dataset1["home_team"][i]=="RR")):
            dataset1["playerPtsSum_home"][i]=pts2010["RR"]
        if((dataset1["away_team"][i]=="RR")):
            dataset1["playerPtsSum_away"][i]=pts2010["RR"]
    elif(dataset1["season"][i]==2011):
        if((dataset1["home_team"][i]=="CSK")):
            dataset1["playerPtsSum_home"][i]=pts2011["CSK"]
        if(( dataset1["away_team"][i]=="CSK")):
            dataset1["playerPtsSum_away"][i]=pts2011["CSK"]
        if((dataset1["home_team"][i]=="DC")):
            dataset1["playerPtsSum_home"][i]=pts2011["DC"]
        if((dataset1["away_team"][i]=="DC")):
            dataset1["playerPtsSum_away"][i]=pts2011["DC"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2011["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2011["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2011["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2011["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2011["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2011["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2011["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2011["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2011["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2011["RCB"]
        if((dataset1["home_team"][i]=="RR")):
            dataset1["playerPtsSum_home"][i]=pts2011["RR"]
        if((dataset1["away_team"][i]=="RR")):
            dataset1["playerPtsSum_away"][i]=pts2011["RR"]
        if((dataset1["home_team"][i]=="KTK")):
            dataset1["playerPtsSum_home"][i]=pts2011["KTK"]
        if((dataset1["away_team"][i]=="KTK")):
            dataset1["playerPtsSum_away"][i]=pts2011["KTK"]
        if((dataset1["home_team"][i]=="PW")):
            dataset1["playerPtsSum_home"][i]=pts2011["PW"]
        if((dataset1["away_team"][i]=="PW")):
            dataset1["playerPtsSum_away"][i]=pts2011["PW"]
    elif(dataset1["season"][i]==2012):
        if((dataset1["home_team"][i]=="CSK")):
            dataset1["playerPtsSum_home"][i]=pts2012["CSK"]
        if(( dataset1["away_team"][i]=="CSK")):
            dataset1["playerPtsSum_away"][i]=pts2012["CSK"]
        if((dataset1["home_team"][i]=="DC")):
            dataset1["playerPtsSum_home"][i]=pts2012["DC"]
        if((dataset1["away_team"][i]=="DC")):
            dataset1["playerPtsSum_away"][i]=pts2012["DC"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2012["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2012["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2012["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2012["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2012["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2012["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2012["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2012["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2012["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2012["RCB"]
        if((dataset1["home_team"][i]=="RR")):
            dataset1["playerPtsSum_home"][i]=pts2012["RR"]
        if((dataset1["away_team"][i]=="RR")):
            dataset1["playerPtsSum_away"][i]=pts2012["RR"]
        if((dataset1["home_team"][i]=="PW")):
            dataset1["playerPtsSum_home"][i]=pts2012["PW"]
        if((dataset1["away_team"][i]=="PW")):
            dataset1["playerPtsSum_away"][i]=pts2012["PW"]
    elif(dataset1["season"][i]==2013):
        if((dataset1["home_team"][i]=="CSK")):
            dataset1["playerPtsSum_home"][i]=pts2013["CSK"]
        if(( dataset1["away_team"][i]=="CSK")):
            dataset1["playerPtsSum_away"][i]=pts2013["CSK"]
        if((dataset1["home_team"][i]=="SH")):
            dataset1["playerPtsSum_home"][i]=pts2013["SH"]
        if((dataset1["away_team"][i]=="SH")):
            dataset1["playerPtsSum_away"][i]=pts2013["SH"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2013["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2013["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2013["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2013["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2013["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2013["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2013["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2013["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2013["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2013["RCB"]
        if((dataset1["home_team"][i]=="RR")):
            dataset1["playerPtsSum_home"][i]=pts2013["RR"]
        if((dataset1["away_team"][i]=="RR")):
            dataset1["playerPtsSum_away"][i]=pts2013["RR"]
        if((dataset1["home_team"][i]=="PW")):
            dataset1["playerPtsSum_home"][i]=pts2013["PW"]
        if((dataset1["away_team"][i]=="PW")):
            dataset1["playerPtsSum_away"][i]=pts2013["PW"]
    elif(dataset1["season"][i]==2014):
        if((dataset1["home_team"][i]=="CSK")):
            dataset1["playerPtsSum_home"][i]=pts2014["CSK"]
        if(( dataset1["away_team"][i]=="CSK")):
            dataset1["playerPtsSum_away"][i]=pts2014["CSK"]
        if((dataset1["home_team"][i]=="SH")):
            dataset1["playerPtsSum_home"][i]=pts2014["SH"]
        if((dataset1["away_team"][i]=="SH")):
            dataset1["playerPtsSum_away"][i]=pts2014["SH"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2014["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2014["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2014["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2014["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2014["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2014["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2014["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2014["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2014["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2014["RCB"]
        if((dataset1["home_team"][i]=="RR")):
            dataset1["playerPtsSum_home"][i]=pts2014["RR"]
        if((dataset1["away_team"][i]=="RR")):
            dataset1["playerPtsSum_away"][i]=pts2014["RR"]
    elif(dataset1["season"][i]==2015):
        if((dataset1["home_team"][i]=="CSK")):
            dataset1["playerPtsSum_home"][i]=pts2015["CSK"]
        if(( dataset1["away_team"][i]=="CSK")):
            dataset1["playerPtsSum_away"][i]=pts2015["CSK"]
        if((dataset1["home_team"][i]=="SH")):
            dataset1["playerPtsSum_home"][i]=pts2015["SH"]
        if((dataset1["away_team"][i]=="SH")):
            dataset1["playerPtsSum_away"][i]=pts2015["SH"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2015["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2015["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2015["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2015["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2015["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2015["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2015["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2015["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2015["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2015["RCB"]
        if((dataset1["home_team"][i]=="RR")):
            dataset1["playerPtsSum_home"][i]=pts2015["RR"]
        if((dataset1["away_team"][i]=="RR")):
            dataset1["playerPtsSum_away"][i]=pts2015["RR"]
    elif(dataset1["season"][i]==2016):
        if((dataset1["home_team"][i]=="GL")):
            dataset1["playerPtsSum_home"][i]=pts2016["GL"]
        if(( dataset1["away_team"][i]=="GL")):
            dataset1["playerPtsSum_away"][i]=pts2016["GL"]
        if((dataset1["home_team"][i]=="SH")):
            dataset1["playerPtsSum_home"][i]=pts2016["SH"]
        if((dataset1["away_team"][i]=="SH")):
            dataset1["playerPtsSum_away"][i]=pts2016["SH"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2016["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2016["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2016["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2016["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2016["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2016["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2016["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2016["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2016["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2016["RCB"]
        if((dataset1["home_team"][i]=="RPS")):
            dataset1["playerPtsSum_home"][i]=pts2016["RPS"]
        if((dataset1["away_team"][i]=="RPS")):
            dataset1["playerPtsSum_away"][i]=pts2016["RPS"]
    elif(dataset1["season"][i]==2017):
        if((dataset1["home_team"][i]=="GL")):
            dataset1["playerPtsSum_home"][i]=pts2017["GL"]
        if(( dataset1["away_team"][i]=="GL")):
            dataset1["playerPtsSum_away"][i]=pts2017["GL"]
        if((dataset1["home_team"][i]=="SH")):
            dataset1["playerPtsSum_home"][i]=pts2017["SH"]
        if((dataset1["away_team"][i]=="SH")):
            dataset1["playerPtsSum_away"][i]=pts2017["SH"]
        if((dataset1["home_team"][i]=="DD")):
            dataset1["playerPtsSum_home"][i]=pts2017["DD"]
        if((dataset1["away_team"][i]=="DD")):
            dataset1["playerPtsSum_away"][i]=pts2017["DD"]
        if((dataset1["home_team"][i]=="KKR")):
            dataset1["playerPtsSum_home"][i]=pts2017["KKR"]
        if((dataset1["away_team"][i]=="KKR")):
            dataset1["playerPtsSum_away"][i]=pts2017["KKR"]
        if((dataset1["home_team"][i]=="KXIP")):
            dataset1["playerPtsSum_home"][i]=pts2017["KXIP"]
        if((dataset1["away_team"][i]=="KXIP")):
            dataset1["playerPtsSum_away"][i]=pts2017["KXIP"]
        if((dataset1["home_team"][i]=="MI")):
            dataset1["playerPtsSum_home"][i]=pts2017["MI"]
        if((dataset1["away_team"][i]=="MI")):
            dataset1["playerPtsSum_away"][i]=pts2017["MI"]
        if((dataset1["home_team"][i]=="RCB")):
            dataset1["playerPtsSum_home"][i]=pts2017["RCB"]
        if((dataset1["away_team"][i]=="RCB")):
            dataset1["playerPtsSum_away"][i]=pts2017["RCB"]
        if((dataset1["home_team"][i]=="RPS")):
            dataset1["playerPtsSum_home"][i]=pts2017["RPS"]
        if((dataset1["away_team"][i]=="RPS")):
            dataset1["playerPtsSum_away"][i]=pts2017["RPS"]
dataset1.to_csv("allMatches_modified1.csv")

 
dataset3 = pd.read_csv("allMatches_modified1.csv")