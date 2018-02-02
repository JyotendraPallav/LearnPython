import win32com.client

items = []

#def encodeit(s):
  #  if isinstance(s, str):
    #    return unicode(s, 'utf-8')
#    else:
#        return s

def extract():
  
  outlook  = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
  inbox    = outlook.GetDefaultFolder(6)  # "6" refers to the inbox
  messages = inbox.Items
  message  = messages.GetFirst()
  
  
  while message:
      
      try:
          d = dict()
          d['Subject'] = message.subject
          d['SentOn']  = message.SentOn
          d['EntryID'] = message.EntryID
          d['Sender']  = message.sender
          d['Size']    = message.size
          d['Body']    = message.body
          d['To']      = message.To
          items.append(d)

      except Exception as inst:
          print("Error processing mail")
      subject=message.subject
      print(subject)

      message = messages.GetNext()
      
def showMessage():
  items.sort(key=lambda tup: tup['SentOn']) 
  
  for i in items:
    # print(i["SentOn"], i["To"])
    print(i)
    
extract()
showMessage()
