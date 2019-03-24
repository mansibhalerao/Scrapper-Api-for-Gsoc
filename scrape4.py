from selenium import webdriver
import time
import re
def GetList():
    URL = "https://summerofcode.withgoogle.com/organizations/"

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(URL)
    urlstringlist = []
    infostringlist = []
    urlnumstringlist = []

    k=0;
    while True:
            k+=1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            if(k==8): break

    orglist = driver.find_elements_by_class_name('organization-card__container')
    driver.execute_script("window.scrollTo(0,0);")


    regex = r"page=\d#(\d+)"
    orglength = len(orglist)
    #############################################
    #orglength = 20
    #############################################
    print(orglength)
    time.sleep(2)
    for i in range(0,orglength):
            orglist[i].click()
            time.sleep(0.2)
            teststring = str(driver.current_url)
            print(teststring)
            Result = (re.search(regex, teststring, flags=0))
            if(Result):
                    excode = Result.group(1)
            else: excode = "X"
            urlnumstringlist.append(excode)

    print(urlnumstringlist)

    urlfirstpart = 'https://summerofcode.withgoogle.com/organizations/'

    OrgInfoComplete = []
    for i in range(0,orglength):
            driver.get(urlfirstpart+urlnumstringlist[i]+'/')
            nm = driver.find_element_by_class_name('banner__title').text
            wm = driver.find_element_by_class_name('page-organizations__org-url').text
            #tm = driver.find_elements_by_class_name('org__tag-container layout-wrap layout-row')
            tm = driver.find_elements_by_class_name('org__tag-container')
            em = driver.find_elements_by_class_name('md-primary')
            dm = driver.find_element_by_xpath('/html/body/div/div/div[1]/ui-view/div/ui-view/ui-view/div[2]/section[2]/div/div/div[1]/div/p').text
            try: dm+= " " + driver.find_element_by_xpath('/html/body/div/div/div[1]/ui-view/div/ui-view/ui-view/div[2]/section[2]/div/div/div[1]/div/p[2]').text
            except: pass
            tmx = (tm[0].text.split('\n'))
            emx = "-"
            try:
                    emp = (em[-2].get_attribute("href"))
                    if(emp[0:7]=='mailto:'): emx = emp[7:]
            except: pass
            OrgInfoComplete.append([nm,wm,dm,emx,tmx])
            #time.sleep(10)


    Finstr = ''

    for i in range(0,len(OrgInfoComplete)):
            ApiStr = '<br>{<br>organization:' + str(OrgInfoComplete[i][0]) +'<br>link:' + str(OrgInfoComplete[i][1])
            ApiStr +='<br>description:'+ str(OrgInfoComplete[i][2]) +'<br>technologies:'+ str(','.join(OrgInfoComplete[i][4]))
            ApiStr +='<br>contact:'+ str(OrgInfoComplete[i][3]) + '<br>}'
            print(ApiStr)
            Finstr += ApiStr
    Tim = str(int(time.time()))
    OrgFile = open("GDG.txt","w")
    OrgFile.write(Tim + Finstr.strip())
    OrgFile.close()
    driver.close()

