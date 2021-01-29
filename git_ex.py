

########## Function #############
def buyTicket( touristName, seat, hour ):
  ticket = { 
    'touristName':touristName,
    'seat':seat,
    'hour':hour    
  }
  place=['1A','2A','3A','1B','2B','3B','1C','2C','3C']

  if len(touristName)>=5 and seat=="1a" or seat=="2a" or seat=="3a" or seat=="1b" or seat=="2b" or seat=="3b" or seat=="1c" or seat=="2c" or seat=="3c"and hour=="11:00" or hour=="11:30" or hour=="12:00" :
    return ticket
  else:
    return
########## Function #############




############ Scripts ############

print("---------------------------------------------")
name=input("Tourist Name? (e.g: Lora Abams)>> ")
seat=input("Choose your place (e.g: 3b)>> ")
hour=input("Choose you flying time (e.g: 11:00)>> ")
print()
print (buyTicket(name,seat,hour))

############ Scripts ############




