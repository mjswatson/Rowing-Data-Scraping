import requests
import time
import csv
base_string="https://www.britishrowing.org/rowing-activity-finder/club/?clubid="
z=0
saved_names=[]
saved_emails=[]
saved_regions=[]
start_value=929
end_value=2477
for i in range(start_value,end_value):
    i_string=str(i)
    use_string=base_string+i_string
    payload = {}
    headers = {
      'Cookie': '__cfduid=d2895bbcb0f7ea4862c925f84817bb63e1588933519; PHPSESSID=e235l22e8ocejp7m0ulqdfofj1'
    }

    response = requests.request("GET", use_string, headers=headers, data = payload)
    response_list=response.text.encode('utf8')
    response_str=str(response_list)
    length=len(response_str)
   # while length<69500:
    #    time.sleep(300)
    #    payload = {}
    #    headers = {
     #     'Cookie': '__cfduid=d2895bbcb0f7ea4862c925f84817bb63e1588933519; PHPSESSID=e235l22e8ocejp7m0ulqdfofj1'
     #   }

   #     response = requests.request("GET", use_string, headers=headers, data = payload)
   #     response_list=response.text.encode('utf8')
    #    response_str=str(response_list)
    #    length=len(response_str)
   # break

    email_start=response_str.find('[clubEmailaddress] => ')
    email_end=response_str.find('\\n    [clubPostcode]')
    if email_end-email_start>=23:
        email=response_str[email_start+22:email_end]
        Name_start=response_str.find('[clubName] => ')
        Name_end=response_str.find('\\n    [clubPhoneNumber] ')
        name=response_str[Name_start+14:Name_end]
        region_Start=response_str.find('[clubRegion] => ')
        region_end=response_str.find('\\n    [clubTown] => ')
        region=response_str[region_Start+16:region_end]
        site=use_string
        saved_names.append(name)
        saved_emails.append(email)
        saved_regions.append(region)
        z=z+1
        
    print('Emails Collected:'+str(z))
    print('Checked:'+str(i-start_value)+'/'+str(end_value-start_value))
        


#save data to csv
if z>0:
    with open('rowing_clubs.csv', 'w', newline='') as myfile:
         writer = csv.writer(myfile)
         writer.writerow(saved_names)
         writer.writerow(saved_emails)
         writer.writerow(saved_regions)
print('Done it!')
