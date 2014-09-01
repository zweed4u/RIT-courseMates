#Zachary Weeden
#@zweed4u  display classlist RIT MyCourses 
#Tested on Python 2.6.6

import mechanize
import urllib
import cookielib
from bs4 import BeautifulSoup
import html2text
import re
import sys
import StringIO
import getpass
from easygui import passwordbox

try:
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)


    br.set_handle_gzip(False)


    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Chrome')]

    # The site we will navigate into, handling it's session
    br.open('https://mycourses.rit.edu/')

    # Inspect name of the form
    '''
    for f in br.forms():
        print f
    '''
    # Select the second (index one) form - the first form is a search query box
    br.select_form(nr=0)





    # User credentials
    #####HANDLE LOGIN CHECKING#####



    print "   ______                           __  ___      __      "     
    print "  / ____/___  __  _______________  /  |/  /___ _/ /____  _____"
    print " / /   / __ \/ / / / ___/ ___/ _ \/ /|_/ / __ `/ __/ _ \/ ___/"
    print "/ /___/ /_/ / /_/ / /  (__  )  __/ /  / / /_/ / /_/  __(__  ) "
    print "\____/\____/\__,_/_/  /____/\___/_/  /_/\__,_/\__/\___/____/  "

    print " _               _______        __            _ _  _         "
    print "| |__  _   _ _  |__  /\ \      / /__  ___  __| | || |  _   _ "
    print "|  _ \| | | (_)   / /  \ \ /\ / / _ \/ _ \/ _` | || |_| | | |"
    print "| |_) | |_| |_   / /_   \ V  V /  __/  __/ (_| |__   _| |_| |"
    print "|_.__/ \__, (_) /____|   \_/\_/ \___|\___|\__,_|  |_|  \__,_|"
    print "       |___/                                                 "

    print "\n"
    username = raw_input("Username: ")
    print "Password: "
    password = passwordbox("Password: ")

    #password = getpass.getpass() #-> echos pass with IDLE
    #password = raw_input("Password: ") -> echos pass


    br.form['username'] = username
    br.form['password'] = password


    # Login
    br.submit()









    #Prints html of main page after login
    #print(br.open('https://mycourses.rit.edu/d2l/lp/ouHome/defaultHome.d2l').read()) 


    regex = '<a class="vui-link vui-outline d2l-link d2l-left" href="(.+?)" title="(.+?)">(.+?)</a>'
    pattern = re.compile(regex)


    regex2 = '<a class="vui-outline" onclick="EmailUser((.+?));;return false;" href="javascript://" title="(.+?)">(.+?)</a>'
    pattern2 = re.compile(regex2)



    ###USE IN WHILE LOOP TO PRINT OUT STR
    ###PROMPT USER FOR HOW MANY CLASSES&&LABS ARE TAKEN AND USE THAT AS COUNTER VAR RATHER THAN i

    htmltext = br.open('https://mycourses.rit.edu/d2l/lp/ouHome/defaultHome.d2l').read()
    classes = re.findall(pattern,htmltext)

    noClass = int(input("How Many Classes/Labs/Recitations are taken? "))
    print "\n"

    linkToList = []
    #urls = []
    i = 0
    while i < noClass:   # 9 = 9 classes/labs
        j = 0


        course = str(classes[i]).split("', '")[1]
        course = str(course).split("Enter ")[1]
        print course
        print "================================================"
        

        classLink = str(classes[i]).split("('")[1]
        classLink =  str(classLink).split("',")[0]
        #classLink = "https://mycourses.rit.edu"+str(classLink)
        #urls.append(classLink)   #populate urls array with links to each class
        classId =  str(classLink).split("=")[1]
        listLink = "https://mycourses.rit.edu/d2l/lms/classlist/classlist.d2l?ou="+str(classId)
        linkToList.append(listLink)



        #print "Class Roster Page: " + str(linkToList[i])+"\n"

        rosterPage = br.open(str(linkToList[i])).read()
        rosterNames = re.findall(pattern2,rosterPage)

        

        ###WHILE LOOP NEEDED TO GET LEN OF CLASSLIST AND PRINT EACH
        while j < len(rosterNames): # no of students
            name = str(rosterNames[j]).split("Compose email to ")[1]
            name = str(name).split("', ")[0]
            #print str(rosterNames)+"\n"
            print str(name) #+ "\n"
            j+=1

        print "\n" + "\n"
        i+=1
       


####### Instead of going here, use unique 6 digit number and append to url
        '''
        classtext = br.open(str(urls[i])).read()

        classList = re.findall(pattern2,classtext)

        #print classList[2]
        if i==8:        # Conditonal neede because not all classes have classlist tab in same area
            listLink = str(classList[0]).split("('")[1]
            listLink = str(listLink).split("',")[0]
        else:
            listLink = str(classList[2]).split("('")[1]
            listLink = str(listLink).split("',")[0]
        listLink = "https://mycourses.rit.edu"+str(listLink)
        linkToList.append(listLink)

        print linkToList[i]
'''

        




except:
    print "~~~Exception Thrown! Most likely incorrect login credentials.~~~"

