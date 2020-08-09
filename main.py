#Nishanth
#using dictionary datastructure
monthcode={1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}
centurycode={1500:0,1600:6,1700:4,1800:2,1900:0,2000:6,2100:4,2200:2}
weekcodec={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
dd,mm,yyyy=[int(x) for x in input("Enter Date in dd/mm/yyyy format: ").split('/')]
century= centurycode[yyyy-(yyyy%100)]
year=yyyy%100
leap=year//4
month=monthcode[mm]
rem=(century+year+leap+month+dd)%7
print('Week Day is ',weekcode[rem])
