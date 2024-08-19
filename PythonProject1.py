# -----------------------------------------------------------------
# Assignment Name:      Project 1
# Name:                 Mariah
# -----------------------------------------------------------------


# -----------------------------------------------------------------
# Function Name:        Validate String Input Name
# Function Purpose:     Validate any String data
# -----------------------------------------------------------------
def Validate_String_Input1( str_Input ):
    
   if(str_Input == '') :
      
      strValidated = False
   else:
      strValidated = True
      print("Employee Name is", str_Input)
   
   return strValidated 

# -----------------------------------------------------------------
# Function Name:        Validate String Input Employee Type
# Function Purpose:     Validate any String data
# -----------------------------------------------------------------
def Validate_String_Input2( str_Input ):
    
   if(str_Input == 'M') or (str_Input == 'H'):
      
      strValidated = True
   else:
      strValidated = False
      print("Employee must be 'M' or 'H'")
   
   return strValidated 

# -----------------------------------------------------------------
# Function Name:        Validate Another Employee Input
# Function Purpose:     Validate input for Y or N
# -----------------------------------------------------------------
def Validate_AnotherEmployee_Input (str_Input):
    
   if(str_Input == 'Y') or (str_Input == 'N'):
      strValidated = True
   else:
      print("Response must be 'Y' or 'N'")
      strValidated = False
   return strValidated

# -----------------------------------------------------------------
# Function Name:        Validate Integer Input
# Function Purpose:     Validate any integer data
# -----------------------------------------------------------------
def Validate_Integer_Input( int_Input ):
   try:
        int_Input = int(int_Input)
        if(int_Input >= 0):
            strValidated = True
        else:
            strValidated = False
            print("Input Must Be 0 or More")
   except ValueError:
        strValidated = False
        print("Input Must be Numeric")
   return strValidated

# -----------------------------------------------------------------
# Function Name:        Validate Float Input
# Function Purpose:     Validate any Float data
# -----------------------------------------------------------------
def Validate_Float_Input( flt_Input ):
   try:
        flt_Input = float(flt_Input)
        if(flt_Input >= 0):
            
            strValidated = True
        else:
            strValidated = False
            print("Input Must Be 0 or More")
   except ValueError:
        strValidated = False
        print("Input Must be Numeric")
   return strValidated


# -----------------------------------------------------------------
# Function Name:        Calc Employee discount
# Function Purpose:     
# -----------------------------------------------------------------
def Calculate_Hourly_Discount(intYearsEmployed):
   
     intDiscountPercentage = float(0)
   
     if intYearsEmployed > 15:
       intDiscountPercentage  = .30
     elif intYearsEmployed > 11 and intYearsEmployed  < 15 :
       intDiscountPercentage  = .25
     elif intYearsEmployed > 7 and intYearsEmployed  < 10 :
       intDiscountPercentage  = .20
     elif intYearsEmployed > 4 and intYearsEmployed  < 6 :
       intDiscountPercentage  = .14
     elif intYearsEmployed  < 3 :
       intDiscountPercentage  = .10

     return intDiscountPercentage


 
# -----------------------------------------------------------------
# Function Name:        Calc Manager discount
# Function Purpose:     
# -----------------------------------------------------------------
def Calculate_Management_Discount(intYearsEmployed):
   
  
   
     if intYearsEmployed > 15:
       intDiscountPercentage  = .40
     elif intYearsEmployed > 11 and intYearsEmployed  < 15 :
       intDiscountPercentage  = .35
     elif intYearsEmployed > 7 and intYearsEmployed  < 10 :
       intDiscountPercentage  = .30
     elif intYearsEmployed > 4 and intYearsEmployed  < 6 :
       intDiscountPercentage  = .24
     elif intYearsEmployed  < 3 :
       intDiscountPercentage  = .20

     return intDiscountPercentage


 
# -----------------------------------------------------------------
# Function Name:        Calc  YTD discount
# Function Purpose:     
# -----------------------------------------------------------------
def Determine_YTD_Discount(intDiscountPercentage,intYTDPurchases) :
    intYTDAmountofdiscount = float(0)

    intYTDAmountofdiscount = intYTDPurchases * intDiscountPercentage
    
    return intYTDAmountofdiscount



 
# -----------------------------------------------------------------
# Function Name:        Today purchase amount
# Function Purpose:     
# -----------------------------------------------------------------
def Determine_Total(intTodayPurchase):
   
   intYTDAmountofdiscount = float(0)

   intTodayPurchasebeforeDiscount = intTodayPurchase
    
   return intTodayPurchasebeforeDiscount



# -----------------------------------------------------------------
# Function Name:        Calc  Employee Discount today
# Function Purpose:     
# -----------------------------------------------------------------

def Determine_Employee_Discount(intYTDAmountofdiscount,intTodayPurchasebeforeDiscount,intDiscountPercentage):
    
    
    if intYTDAmountofdiscount >= 200:
       intEmployeeDiscountthispurchase  = 0
    elif  intYTDAmountofdiscount + (intTodayPurchasebeforeDiscount * intDiscountPercentage) <200:
       intEmployeeDiscountthispurchase  =  (intTodayPurchasebeforeDiscount * intDiscountPercentage)

    elif intYTDAmountofdiscount + (intTodayPurchasebeforeDiscount * intDiscountPercentage) > 200:
       intEmployeeDiscountthispurchase = 200 - intYTDAmountofdiscount

     
    return intEmployeeDiscountthispurchase




# -----------------------------------------------------------------
# Function Name:        Calc  Total with discount
# Function Purpose:     
# -----------------------------------------------------------------
def Determine_Total_with_Discount(intTodayPurchasebeforeDiscount,intEmployeeDiscountthispurchase):
         
    intTotalwithDiscount = float(0)

    intTotalwithDiscount = intTodayPurchasebeforeDiscount - intEmployeeDiscountthispurchase
    
    return intTotalwithDiscount

# -----------------------------------------------------------------
# Function Name:        Display Totals
# Function Purpose:     Will display totals
# -----------------------------------------------------------------
def Display_Totals(intYTDAmountofdiscount,intDiscountPercentage,intTodayPurchasebeforeDiscount, intEmployeeDiscountthispurchase, intTotalwithDiscount):
   
    strintYTDAmountofdiscount = "${:,.2f}".format(intYTDAmountofdiscount)
    strintDiscountPercentage = "${:,.2f}".format(intDiscountPercentage)
    strintTodayPurchasebeforeDiscount = "${:,.2f}".format(intTodayPurchasebeforeDiscount)
    strintEmployeeDiscountthispurchase = "${:,.2f}".format(intEmployeeDiscountthispurchase)
    strintTotalwithDiscount = "${:,.2f}".format(intTotalwithDiscount)
   
    print ("YTD amount of  Discounts  ", strintYTDAmountofdiscount)
    print ("Discount Percantage is  ", strintDiscountPercentage)
    print (" Total before discount  ", strintTodayPurchasebeforeDiscount)
    print ("Employee discount this purchase  ", strintEmployeeDiscountthispurchase)
    print ("The Total  cost with the discount  ", strintTotalwithDiscount)
    return

# -----------------------------------------------------------------
# Function Name:       Accumulate total purchase without discount
# Function Purpose:    
# -----------------------------------------------------------------
def Accumulate_Purchases(intTotalPurchasesBeforeDiscount):
    
        intTotalPurchasesBeforeDiscount += intTotalPurchasesBeforeDiscount 

        return intTotalPurchasesBeforeDiscount
    
# -----------------------------------------------------------------
# Function Name:        Display Employment without disocunt
# Function Purpose:     Will display the accumulated employee total
# -----------------------------------------------------------------
def Display_Purchases(intTotalPurchasesBeforeDiscount):
    
    print ("The Employee Purchases before discount is  ", intTotalPurchasesBeforeDiscount)
    return



  
# -----------------------------------------------------------------
# Function Name:       Accumulate total purchase with discount
# Function Purpose:    
# -----------------------------------------------------------------
def Accumulate_Purchases_Discount(intTotalAfterDiscountApplied):
    
        intTotalAfterDiscountApplied +=  intTotalAfterDiscountApplied 

        return intTotalAfterDiscountApplied
    
# -----------------------------------------------------------------
# Function Name:        Display Employment Count
# Function Purpose:     Will display the accumulated employee total
# -----------------------------------------------------------------
def Display_Purchases_Discount(intTotalAfterDiscountApplied):
    
    print ("The Employee Purchases ith discount is  ", intTotalAfterDiscountApplied)
    return

# -----------------------------------------------------------------
# Name:                 Controlling Main Code for Applications
# Purpose:              Controls the flow for Pennies for Pay
# -----------------------------------------------------------------
def Main():
    
#input values

    strName = str("")
    intYearsEmployed = int(0)	
    intYTDPurchases = float(0)
    strEmployee = str("")
    intTodayPurchase = float(0)

#output  values
    intDiscountPercentage = float(0)
    intYTDAmountofdiscount = float(0)
    intTodayPurchasebeforeDiscount	= float(0)
    intEmployeeDiscountthispurchase	= float(0)
    intTotalwithDiscount = float(0)
    intTotalPurchasesBeforeDiscount = float(0)
    intTotalAfterDiscountApplied =float(0)

   

    intEmployeeCount = int(0)
 
    strNewEmployee = str("Y")

    while strNewEmployee == "Y":

        strValidated = bool(False)

    # loop until input is valid
        while strValidated is False:
            strName = input("Enter Employee Name ")
            strValidated = Validate_String_Input1 (strName) 
        strValidated = bool(False)


        
    # loop until input is valid
        while strValidated is False:
            strEmployee = input("Type of Employee 'M' or 'H' ")
            strValidated = Validate_String_Input2( strEmployee )
        strValidated = bool(False)


       # loop until input is valid
        while strValidated is False:
           intYearsEmployed = input("Enter number of years Employed: ")
           strValidated = Validate_Integer_Input (intYearsEmployed) 
        intYearsEmployed = int(intYearsEmployed)
        strValidated = bool(False)



        while strValidated is False:
           intYTDPurchases = input("Enter YTD previous purchases before discount: ")
           strValidated = Validate_Float_Input (intYTDPurchases) 
        intYTDPurchases = float(intYTDPurchases)
        strValidated = bool(False)



        while strValidated is False:
           intTodayPurchase = input("Enter Amount of today Purchase: ")
           strValidated = Validate_Float_Input (intTodayPurchase) 
        intTodayPurchase = float(intTodayPurchase)
        strValidated = bool(False)

        
        
        

        # call function to calculate Total Travel Costs

        if strEmployee == 'H': 
            intDiscountPercentage = Calculate_Hourly_Discount(intYearsEmployed)
        else:
            intDiscountPercentage = Calculate_Management_Discount(intYearsEmployed)

    
        intTodayPurchasebeforeDiscount = Determine_Total(intTodayPurchase)
            
        intYTDAmountofdiscount = Determine_YTD_Discount(intDiscountPercentage,intYTDPurchases) 

        intEmployeeDiscountthispurchase= Determine_Employee_Discount(intYTDAmountofdiscount,intTodayPurchasebeforeDiscount,intDiscountPercentage)

            
        intTotalwithDiscount = Determine_Total_with_Discount(intTodayPurchasebeforeDiscount,intEmployeeDiscountthispurchase)
         
  
        # call function to format and display Totals
        Display_Totals(intYTDAmountofdiscount,intDiscountPercentage,intTodayPurchasebeforeDiscount, intEmployeeDiscountthispurchase, intTotalwithDiscount)
    
        # call function to accumulate totals overall
    
        intTotalPurchasesBeforeDiscount = Accumulate_Purchases(intTotalPurchasesBeforeDiscount)
        intTotalAfterDiscountApplied =  Accumulate_Purchases_Discount(intTotalAfterDiscountApplied)
      
    
#--------------------------------------------------------------------------
# Check for another employee
 #--------------------------------------------------------------------------
        strValidated = False
        while strValidated is False:
            strNewEmployee = input("Another Employee: Y/N?")
            strValidated = Validate_AnotherEmployee_Input (strNewEmployee) 

    Display_Purchases(intTotalPurchasesBeforeDiscount)

    Display_Purchases_Discount(intTotalAfterDiscountApplied)
       
  
Main()



