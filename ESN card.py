import requests
base_url = "https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxx"
#(al posto delle x c'è il token del bot)

def read_msg(offset):
                    
 parameters = { "offset" : offset }

 resp = requests.get( base_url + "/getUpdates" , data = parameters)
 data = resp.json()

 for result in data["result"]:
  if "ESN Card" in result["message"]["text"]:
     send_msg()
  elif "esncard" in result["message"]["text"]:
     send_msg()
  elif "ESNCard" in result["message"]["text"]:
     send_msg()
  elif "ESNcard" in result["message"]["text"]:
     send_msg()  
  elif "ESN card" in result["message"]["text"]:
     send_msg()  
  elif "esn card" in result["message"]["text"]:
     send_msg()  
  elif "Esn card" in result["message"]["text"]:
     send_msg()  
  elif "Esn Card" in result["message"]["text"]:
     send_msg() 
  elif "ESN CARD" in result["message"]["text"]:
     send_msg() 
  if data ["result"]:
   return data["result"][-1]["update_id"]+1

    
def send_msg():

 parameters = {
     "chat_id":"-1591353291",
     "text":"Hi mate!!Hi I will provide you everything you need to know about the ESN Card!let s start!!!  wiiiii :D      so you basically can get your ESN card in the office, the office is open at every tandem event and in some other events, we will update you every week about this, stay in touch! http://www.esngent.org/sites/default/files/partners/HOW%20TO%20GET%20THE%20RYANAIR%20DEAL%20WITH%20YOUR%20ESNCARD.pdf"
 }
 resp = requests.get( base_url + "/sendMessage", data = parameters)
 print=(resp.text)

offset = 0

while True:
  offset = read_msg(offset)
