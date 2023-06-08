progress=0
trailer=0
retriever=0
Exclude=0
    
while True:  #this is infinite loop or endless loop
 try:
   
    passs=int(input('Enter your pass marks  : '))
    defer=int(input('Enter your defer marks : '))
    fail=int(input('Enter your fail marks  : '))




    if((passs %20!=0 or defer%20!=0 or fail%20!=0) or ((0>passs or passs>120) or (0>defer or defer>120) or (0>fail or fail>120))): 
       print('Out of range')
       continue
    elif(passs+defer+fail !=120):
       print('Total incorrect')
       continue
      
    
    elif((passs==120) and (defer==0) and (fail==0)):
              progress+=1
              print('Progress')
    elif((passs==100) and (defer==20 or defer==0) and (fail==20 or fail==0)):
              trailer+=1
              print('Progress (Module trailer)')
    elif((passs==80 or passs==60 or passs==40 or passs==20 or passs==0) and (defer==120 or defer==100 or defer==80 or defer==60 or defer==40 or defer==20 or defer==0) and (fail==60 or fail==40 or fail==20 or fail==0)):
              retriever+=1
              print('Do not progess - module retriever')
    elif((passs==40 or passs==20 or passs==0) and (defer==40 or defer==20 or defer==0) and (fail==120 or fail==100 or fail==80)):
              Exclude+=1
              print('Exclude')
    
    
     
 except ValueError:
     print('Integer Required')
     continue

  
