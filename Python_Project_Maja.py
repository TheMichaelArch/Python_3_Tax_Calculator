import time

seconds = time.time()
local_time = time.ctime(seconds)
print (local_time)

z = 0

Monthly_Earnings = int()
Yearly_Estimate = int()

Average_Tax = 30
Average_Over_Tax = 34
Crypto_Tax = 34
Yearly_Tax = 0
Monthly_Tax = 0

Crypto_Income = 0
Crypto_Investment = 0
Crypto_Profit = 0


Over_Mark_Income = 30000
Income_After_Over_Mark = 0
Tax_Amount_Of_Over_Income = 0
Income_Before_Over_Income = 0
Monthly_Over_Income_Tax = 0
Over_Income_True = 0

c = str()
i = str()
Mode = str()
CR = 0
INC = 0



Income_Calculation = int(0)
Crypto_Calculation = int(0)
Exit_Program = int(0)


while (Income_Calculation == 0 and Crypto_Calculation == 0 and Exit_Program == 0):
    print ("Made By Maja Markus Mikael","\u2122")
    print ("Income Tax or Crypto Tax?", "\n", "Or type \'Exit\' to Quit.")
    Mode = str(input("Type Here Crypto/Income: "))

    if (Mode == str("Income") or Mode == str("income")):
        Income_Calculation = 1
        INC = 1
    if (Mode == str("Crypto") or Mode == str("crypto")):
        Crypto_Calculation = 1
        CR = 1
    if (Mode == str("Exit") or Mode == str("exit")):
        Exit_Program = 1



    if(INC == 1):   #Income Tax Calculator
        while Income_Calculation != 0:
    
            Over_Income_True = 0
            Average_Tax = 30
            Average_Over_Tax = 34
            Income_After_Over_Mark = 0
            Tax_Amount_Of_Over_Income = 0
            Income_Before_Over_Income = 0
            Monthly_Over_Income_Tax = 0
            Yearly_Tax = 0
            Monthly_Tax = 0
            print ("Income related Tax Calculation Mode")
            print ("Your estimation on Monthly INCOME?")
            Monthly_Earnings = int(input("Type Here: "))

            Yearly_Estimate = Monthly_Earnings * 12

            print ("Your YEARLY Income: ", Yearly_Estimate, "€")
            if (Yearly_Estimate > Over_Mark_Income):
                Average_Over_Tax = 34
            else:
                Average_Tax = 30

        #Alternative Tax Calculator
            if (Yearly_Estimate > Over_Mark_Income):
                Income_After_Over_Mark = Yearly_Estimate - Over_Mark_Income
                Tax_Amount_Of_Over_Income = Income_After_Over_Mark / 100 * Average_Over_Tax
                Income_Before_Over_Income = Over_Mark_Income / 100 * Average_Tax
                Average_Tax = (Average_Tax + Average_Over_Tax) / 2
                Yearly_Tax = Tax_Amount_Of_Over_Income + Income_Before_Over_Income
                Monthly_Tax = Income_Before_Over_Income / 12
                Monthly_Over_Income_Tax = Tax_Amount_Of_Over_Income / 12
                Over_Income_True = 1
            else:
                Yearly_Tax = Yearly_Estimate / 100 * Average_Tax
                Monthly_Tax = Monthly_Earnings / 100 * Average_Tax



            print (" Average Tax: ", Average_Tax,"%","\n","Estimated Monthly Tax: ", Monthly_Tax,"€","\n","Estimated Yearly Tax: ", Yearly_Tax,"€")
            if (Over_Income_True == 1):
                print (" Estimated Monthly Tax Over 30K €", Monthly_Over_Income_Tax,"€", "\n", "Income Tax Before 30K €: ", Income_Before_Over_Income,"€","\n","Entire Tax Amount After 30K €: ", Tax_Amount_Of_Over_Income,"€")
    
            i = str(input("Calculate again? yes/no: "))
            if (i == str("no") or i == str("n") or i == str("N") or i == str("NO")):
                Income_Calculation = 0
                INC = 0
            else:
                Income_Calculation = 1
    if(CR == 1):
        #Crypto Tax Calculator
        while Crypto_Calculation != 0:

            Crypto_Income = 0
            Crypto_Investment = 0
            Crypto_Profit = 0    
            print ("Crypto related Tax Calculation Mode")
            print ("Your estimation of sale amount of Crypto (€)?")
            Crypto_Income = int(input("Type Here: "))
    
            print ("Your investment AMOUNT (€)?")
            Crypto_Investment = int(input("Type Here: "))

            if (Crypto_Investment > Crypto_Income):
                print ("No tax if investment is of \'Negative\' profit...")

                continue

            if (Crypto_Investment < Crypto_Income):
                Crypto_Profit = Crypto_Income - Crypto_Investment
                Tax_Amount_Crypto = Crypto_Profit / 100 * Crypto_Tax
                Crypto_Profit_After_Tax = Crypto_Profit - Tax_Amount_Crypto

            print (" Your tax amount: ", Tax_Amount_Crypto, "€", "\n", "Profit After Taxes: ", Crypto_Profit_After_Tax, "€", "\n", "Tax Percentage: ", Crypto_Tax, "%")
    
            c = str(input("Calculate again? yes/no: "))
            if (c == str("no") or c == str("n") or c == str("N") or c == str("NO")):
                Crypto_Calculation = 0
                CR = 0
            else:
                Crypto_Calculation = 1

    if (Exit_Program == 1):
        
        print ("Goodbye, have a pleasent day.")
        time.sleep(2)
        exit
        