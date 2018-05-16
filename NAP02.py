# NAP_2 b1
# Uses 'expected' data rather than 'measured'
# Based originally on script from here:
# https://stackoverflow.com/questions/35371043/use-python-requests-to-download-csv
# Changed delimiter from ',' to ';'
# It looks like I can access what I need with this: my_list[28][4]

'''
This is the link to the info:
https://waterinfo.rws.nl/#!/details/publiek/waterhoogte-t-o-v-nap/Rotterdam(ROTT)/Waterhoogte___20Oppervlaktewater___20t.o.v.___20Normaal___20Amsterdams___20Peil___20in___20cm
  
This is the link to the .csv file:
https://waterinfo.rws.nl/api/Download/CSV?expertParameter=Waterhoogte___20Oppervlaktewater___20t.o.v.___20Normaal___20Amsterdams___20Peil___20in___20cm&locationSlug=Rotterdam(ROTT)&timehorizon=-6,3
'''

import csv
import requests
import time
#from microdotphat import write_string, clear, show

csv_url = 'https://waterinfo.rws.nl/api/Download/CSV?expertParameter=Waterhoogte___20Oppervlaktewater___20t.o.v.___20Normaal___20Amsterdams___20Peil___20in___20cm&locationSlug=Rotterdam(ROTT)&timehorizon=-6,3'


prevLevel = 0
nap_list = []
interval_List = (0,10,20,30,40,50)

def getNap():
  global nap_list
  try:
    with requests.Session() as s:
      download = s.get(csv_url)
      decoded_content = download.content.decode('utf-8')
      cr = csv.reader(decoded_content.splitlines(), delimiter=';')
      nap_list = list(cr)
      return nap_list
  except IndexError:
    print('Error')


def currTimeStr():
  global prevLevel
  while True:
    tijd = time.localtime() #create a struct_time object
    if tijd[4] in interval_List: #and check if the number of minutes is in the interval_List
      currTime = time.asctime()[11:16] #if yes create an hour and minute string using .asctime
      currTime = currTime +':00' #add the zeros
      print(currTime)
      
      getNap() #get and set current nap_list
      # walk through it searching match with currTime nap_list[i][1]
      # could also try for i in nap_list:
      for i in range(len(nap_list)):
        if nap_list[i][1] == currTime:
          currLevel = int(nap_list[i][5])
          print(currLevel)
          print(currLevel - prevLevel)
          prevLevel = currLevel
      time.sleep(65)
    time.sleep(5)

currTimeStr()

'''
while True:
  try:
    with requests.Session() as s:
      download = s.get(csv_url)
      decoded_content = download.content.decode('utf-8')
      cr = csv.reader(decoded_content.splitlines(), delimiter=';')
      my_list = list(cr)
    if my_list[29][1] != updatetime and my_list[29][4] != '': #test time changed and level not empty
      difflevel = int(my_list[29][4]) - prevlevel #new code to compare and show rise or fall of level
      display = (my_list[29][4] + str('%+d' % difflevel)) #+d formatting for positive and neg numbers 
      clear()
      write_string(display, kerning=False)
      show()
			updatetime = my_list[29][1]
			prevlevel = int(my_list[29][4]) #new code to compare and show rise or fall of level
		time.sleep(300) # waits 5 minutes
	except IndexError:
		clear()
		write_string('IndErr', kerning=False)
		show()
		time.sleep(300)
	#except ConnectionError:
		#clear()
		#write_string('ConErr', kerning=False)
		#show()
		#time.sleep(300)

'''