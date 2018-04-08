Assets = {"Cash":{"Cash":10},"Inventory":{},"Accounts Receivable":{"John owes":20,"Katie owe":30},"PPE":{"Motorcycle":300,"Building":10000},"Prepaid":{"Prepaid rent":300},"Others":{"Grant":100}}
Liabilities = {"Loan":{"Bank loan":2000},"Accounts Payable":{"Owe government":300,"Invoiced audit":400},"Unearned revenue":{"Unearned revenue":100},"Other":{}} 
Equity = {"Retained Earnings":{"Retained Earnings":0}}

Revenue = {"School fee revenue":500,"Other revenue":200}
ProgramExpense = {"books":200,"uniform":400,"teacher salary":1500}
AdminExpense = {"Staff salary":3000,"Head office overhead":3500}

newAssets = Assets
newLiabilities = Liabilities
newEquity = Equity
#proper way to copy dictionaries
newRevenue = {}
for entry in Revenue:
    newRevenue[entry] = Revenue[entry]
newProgramExpense = ProgramExpense
newAdminExpense = AdminExpense

cashAccounting = True

def cashAccountingTransform():
    '''
    If cash accounting is true, the function will identify all items in revenue, program expense, and admin expense.
    It will then check with the user if the payment or good/service was delivered within this period.
    If payment or good/service was not delivered in this period, function will remove item from income statement.
    '''
    if cashAccounting == True:
        #running through each item in Revenue
        for key in Revenue:
            #forces yes or no answer to question if payment was made in this period
            while True:
                strPaymentInPeriod = input(f'Was payment received for {key} during this period? (Yes/No): ')
                if strPaymentInPeriod.lower() != 'yes' and strPaymentInPeriod.lower() != 'no':
                    print('Sorry, please input yes or no.')
                    continue
                else:
                    break
            paymentInPeriod = strPaymentInPeriod == 'yes'
            #forces yes or no answer to question if goods or service was delivered within this period
            while True:
                strGSInPeriod = input(f'Was {key} delivered within this period? (Yes/No): ')
                if strGSInPeriod.lower() != 'yes' and strGSInPeriod.lower() != 'no':
                    print('Sorry, please input yes or no.')
                    continue
                else:
                    break
            gsInPeriod = strGSInPeriod == 'yes'
            #if both paymentInPeriod and gsInPeriod are false, remove item from income statement
            if paymentInPeriod == False and gsInPeriod == False:
                del newRevenue[key]
            else:
                continue
        return newRevenue

print(cashAccountingTransform())
