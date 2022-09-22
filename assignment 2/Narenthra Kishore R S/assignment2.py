import random as r
temp = r.randrange(10,50)
humi = r.randrange(1,100)
if(temp>35 and humi>60):
    print("alert high temperature and humidity")
    print("temperature is"+temp+"humidity is"+humi)
elif(temp<20 and humi<40):
    print("alert low temperature and humidity")
    print("temperature is"+temp+"humidity is"+humi)
elif(temp>35 and humi<40):
    print("high temperature and low humidity")
    print("temperature is"+temp+"humidity is"+humi)
elif(temp<20 and humi>60):
    print("low temperature and high humidity")
    print("temperature is"+temp+"humidity is"+humi)
