import csv
import IdentifyingLists as lists

def main():
    try:
        inputReader = csv.reader(open('SampleBalanceSheet.csv', encoding='ISO-8859-1'), delimiter=',',quotechar='"')
    except IOError:
        pass
    allRows = []
    for row in inputReader:
        allRows.append(row)

    balanceDict = {}
    curDict =  {}
    curList = []

    generateBalanceSheet(generateBalanceDict(allRows, balanceDict, curDict, curList))

# Note: the map can be generated in a different order each time    
def generateBalanceDict(allRows, balanceDict, curDict, curList):
    count = 0
    while (count < len(allRows)):
        if (allRows[count][0] != '' or 'Total' not in allRows[count][0]):
            name = allRows[count][0]
            categoryList = []
            count = count + 1

            if (count + 1 >= len(allRows)):
                break
            else:
                while (allRows[count][0] == '' and allRows[count][len(allRows[count]) - 1] != ''):
                    resultList = []
                    for s in allRows[count]:
                        if (s != ''):
                            resultList.append(s)
                    categoryList.append(resultList)
                    count = count + 1
        balanceDict[name.lower()] = categoryList
        count = count + 1
    #print (balanceDict)
    return balanceDict     

def generateBalanceSheet(balanceDict):
    # dictionary:dictionary representing the assets divided up by their category
    assets = {}
    liabilities = {}
    equity = {}
    for key in balanceDict:
        if key == 'assets':
            cashDict={}
            inventoryDict = {}
            acctsReceivable = {}
            ppe = {}
            prepaidExp = {}
            other = {}
            for value in balanceDict[key]:
                for tword in lists.cashIdentify:
                    if (tword.lower() in value[0].lower()):
                        cashDict[value[0]] = float(value[1])
                for tword in lists.inventoryIdentify:
                    if (tword.lower() in value[0].lower()):
                        inventoryDict[value[0]] = float(value[1])
                for tword in lists.arIdentify:
                    if (tword.lower() in value[0].lower()):
                        acctsReceivable[value[0]] = float(value[1])
                for tword in lists.depAssetIdentify:
                    if (tword.lower() in value[0].lower()):
                        ppe[value[0]] = float(value[1])
                for tword in lists.prepaidIdentify:
                    if (tword.lower() in value[0].lower()):
                        prepaidExp[value[0]] = float(value[1])

            assets['Cash'] = cashDict
            assets['Inventory'] = inventoryDict
            assets['Accounts Receivable'] = acctsReceivable
            assets['PPE'] = ppe
            assets['Prepaid Expenses'] = prepaidExp
            assets['Other'] = other
        if key == 'liabilities':
            loanDict = {}
            acctsPayable = {}
            unearnedRev = {}
            others = {}
            for value in balanceDict[key]:
                for tword in lists.shortLoanIdentify:
                    if (tword.lower() in value[0].lower()):
                        loanDict[value[0]] = float(value[1])
                for tword in lists.apIdentify:
                    if (tword.lower() in value[0].lower()):
                        acctsPayable[value[0]] = float(value[1])
                for tword in lists.unearnRevIdentify:
                    if (tword.lower() in value[0].lower()):
                        unearnedRev[value[0]] = float(value[1])
            liabilities['Loans'] = loanDict
            liabilities['Accounts Payable'] = acctsPayable
            liabilities['Unearned Revenue'] = unearnedRev
            liabilities['Others'] = others
        if key == 'equity':
            retainedEarnings = {}
            for value in balanceDict[key]:
                    retainedEarnings[value[0]] = value[1]
            equity['Retained Earnings'] = retainedEarnings
    print ('assets: ', assets)
    print ('liabilities: ', liabilities)   
    print ('equity: ', equity)       
    return 0

main()




