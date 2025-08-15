#bll
print("Welcome to Customer managment service " \
"What can I help ")
#creating list
cus_id_list=[]
cus_name_list=[]
cus_age_list=[]
cus_mob_list=[]
cus_city_list=[]
while True:

    ch=input("1.Add customer \n  2.Search customer \n 3.Modify customer \n 4.Dlete Customer \n 5.Display all Customer  : \n 6. Exit: \n :   ")
    if ch=="1":
        #Add customer
        while True :
            try:
                id=input("Enter the customer id ").strip()
                if not id.isdecimal() or int(id) <= 0:
                    
                    raise Exception("Id must contain only in digit")
                break
            except Exception as err :
                print("Please enter again",err)
        while True:
            
            try:
                name=input("Enter the customer Name").strip().capitalize().title() 
                if not name.replace(" ","").isalpha():
                    raise Exception("Id must contain only in alphet and space Between first and middle name")
                break
            except Exception as error:
                print("Please enter custumer name carefully",error)
                
            #Enter age
            
        while True:
                try:
                    age=input("Enter an Age of Customer").strip()
                    if not age.isdecimal() or int(age) <= 0 :
                        raise Exception ("Age must contain only in inters ")
                    break
                except Exception as  TypeError:
                    print(f"Please Enter customer age only in interger",TypeError)
            #Enter mob
        while True:
                try:
                    mob=input("Enther the customer Mobile Number ").strip()
                    if not mob.isdecimal() or len(mob) != 10:
                        raise Exception ("Mobile number must contain only integer ")
                    break
                except Exception:
                    print("Please enter carefully ")
        while True:
                try:
                    city=input("Enter the city of customer ").strip().title()
                    if not     city .replace(" ","").isalpha():
                        raise Exception ("City is always in Alphaphet ")
                    break
                except Exception as  TypeError:
                    print(f" Please Enter carefully {city}",TypeError)
                    #Append 
        cus_id_list.append(id)
        cus_name_list.append(name)
        cus_age_list.append(age)
        cus_mob_list.append(mob)
        cus_city_list.append(city)

                #2.search customer
    if ch == "2":
        while True :
            id = input("Enter an Id where you Search : ").strip()
            try :
                if not id.isdecimal() or int(id) <= 0 :
                    raise Exception("Id only in integer :")
                break
            except Exception as err :
                print("Please write carefully and correct  ",err)
        i = cus_id_list.index(id)
        print(f"""Your search Id is : {cus_id_list[i]}
Your search Name : {cus_name_list[i]}
Your search age is : {cus_age_list[i]}
Your search customer mobile number is :{cus_mob_list[i]}
Your search customer city is  {cus_city_list[i]} """)

 # Modify customer 
    if ch=="3":
        while True :
            while True :
                id=input("Enter the Modify customer Id").strip() #  new id input
                try:
                    if not id.isdecimal(): # condition Where id is not decimal
                        raise Exception("Input Id only in Integer ")
                    break
                except Exception as  ValueError :
                    print("Enter modify Id carefully :",ValueError)
            while True :
                name = input("Enter the Modify customer Name is : ").strip().capitalize() #new name input
                try:
                    if not name.replace(" ","") .isalpha() :# condition Where name is not Alphabhet 
                        raise Exception ("Input name is only in Alphabhet ")
                    break
                except Exception as Error:
                    print("Enter a Modify Name carefully ",Error)
            while True :# condition Where age is not decimal 
                age = input("Enter the Modify Customer Age is :").strip() #new Age input
                try :
                    if not age.isdecimal() or int(age) <= 0 :
                        raise Exception ("Input Age only in  postive Integer")
                    break
                except Exception as Error:
                    print("Please Enter a modify AGe carefully ",Error)
            
            while True :
                try :
                    mob = input("Enter a Mobile Number you Modify :").strip()
                    if not mob.isdecimal() or len(mob) != 10 :
                        raise Exception("Input Mobile Number is only Integer and Gives 10 Digit only ")
                    break
                except Exception as err :
                    print("Please Enter Mobile Number Carefully : ",err)
                print("This is you Modify Mobile Number :",mob)
            while True : # condition Where  City is not Alphabet
                city = input("Enter the Modify Customer city is :").strip().capitalize() #new city input

                try:
                    if not city.replace(" ","").isalpha():
                        raise Exception ("Input City is only in Alphabhet")
                    break
                except Exception as InputError:
                    print("Please Enter a modify City carefully ",InputError)
            i=cus_id_list.index(id) 
            cus_name_list[i]=name 
            print(f"Your Modify name is : {cus_name_list}")
            cus_age_list[i]=age
            print(f"Your Modify age is : {cus_age_list}")
            cus_mob_list[i]=mob
            print(f"Your Modify Mobile num. is : {cus_mob_list}")
            cus_city_list[i]=city
            print(f"Your Modify City is : {cus_city_list}")
            break

    #4. Delete customer
    if ch == "4" :
        while True :
                
                while True :
                    id = input("Enter ID Where you want to Delete is : ").strip()# Deleted input Id
                    try:
                        if not id.isdecimal() or int(id) <= 0  :
                            raise Exception ("Input Id always positive Integer :")
                        break
                    except Exception as ValueError :
                        print("Please Enter Id carefully  ",ValueError)
                i = cus_id_list.index(id)
                cus_name_list.pop(i) 
                print(f"Your Deleted customer is : {cus_name_list}")
                cus_age_list.pop(i)
                print(f"Your Deleted Age is : {cus_age_list}")
                cus_mob_list.pop(i)
                print(f"Your Deleted Mobile number is : {cus_mob_list}")
                cus_city_list.pop(i)
                print(f"Your Deleted city  is : {cus_city_list}")
                print("Deleted sucessfully  :") 

    if ch == "5":# Display all customer  
        while True :
            print(f"Your customer Id is : {cus_id_list}")
            print(f"Your Customer Name  is : {cus_id_list}")
            print(f"Your customer Age is : {cus_id_list}")
            print(f"Your customer Mobile Number is: {cus_id_list}")
            print(f"Your customer City is: {cus_id_list}")
    if ch == "6":# Exit Cms
         print("Thankyou for using Customer Mnagment System Nitin Tellycomm")
        
    else:
        print("Incorrect Choice :  ")        





        
    
    


    









            


                   
        
                
            
                    
            
            



                            


        

                
    

                


            

