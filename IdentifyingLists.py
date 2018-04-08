#Identifies asset items that should be classified as 'Cash'
#Cash at bank is classified as 'Cash' too
cashIdentify = ["cash","bank","checking","savings","saving"]

#Identifies asset items that should be classified as 'Inventory'
inventoryIdentify = ["inventory"]

#Identifies asset items that should be classified as 'Accounts Receivable'
arIdentify = ["owe","owes","loan","loans","receivable","receivables","borrow","borrowed","lend","lent"]

#Identifies asset items that are prepaid
prepaidIdentify = ["prepay","pre-pay","prepaid","pre-paid","advance","advanced"]

#Identifies asset items that should be subject to depreciation
depAssetIdentify = ["bicycle","bicycles","motorbike","motorbikes","moto","motos","building","buildings","machine","machines","computer","computers","car","cars","truck","trucks","lorry","lorries","factory","factories"]



#Identifies liability items that should be classified as 'loans'
shortLoanIdentify = ["bank","loan","loans"]

#Identifies liability items that should be classified as 'Accounts Payable'
apIdentify = ["borrow","borrowed","lend","lent","payable","payables","owe","owes","invoice","invoiced"]

#Identifies liability items that should be classified as unearned revenue
unearnRevIdentify = ["unearned","revenue","advance","advanced","prepaid","pre-paid","prepay","pre-pay"]


#Identify program expenses
pExpenseIdentify = ["program","project","operation","operations"]
#For teaching industry
teachPExpenseIdentify = ["teacher","teachers","librarian","book","books","counselor"]


#Identify donation gains
dGainIdentify = ["donations","donation","cash gift","cash gifts"]

#Identify revenues from activities
revenueIdentify = ["revenue","income","fee"]

#Identify admin expenses
aExpenseIdentify = ["admin","administrative","staff","head office"]

#Identifies expense items that should be classified as financing cost
fExpenseIdentify = ["interest","bank"]
