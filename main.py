#Shahd Shwekeyeh -1222105 sec#1
#Ghada Sawalha -1220064 sec#1

#---------------Needed Libraries------------------#
from pathlib import Path
#--------------printing all invoices--------------#

i=1
while True:
  file=Path("invoices")/f"invoice{i}.txt"
  if file.exists():
    content=file.read_text()
    print(f"Invoice Number {i}:")
    print(content)
    print()
    i+=1
  else:
    break
  
#--------------Calculating the Number of Orders--------------#

def totalOrders(folderName):
 folder=Path(folderName)
 count=0
 i=1
 while True:
  file=folder/f"invoice{i}.txt"
  if file.exists():
   count+=1
   i+=1
  else:
   break
 return count
total_orders=totalOrders("invoices")

#--------------Calculating the Number of Orders In Restaurant --------------#

def DineInOrders(folderName):
 folder=Path(folderName)
 count=0
 i=1
 while True:
  file=folder/f"invoice{i}.txt"
  if not file.exists():
   break
  with open(file,"r") as f:
   lines=f.readlines()
   for line in lines:
    if line.replace("\n","").lower()=="order type: in":
     count+=1
     break
  i+=1
 return count
inOrders=DineInOrders("invoices")
#print("Number of In-Restaurant orders:",inOrders)

#--------------Calculating the Number of Take Away Orders--------------#

def TakeAway(folderName):
 folder=Path(folderName)
 count=0
 i=1
 while True:
  file=folder/f"invoice{i}.txt"
  if not file.exists():
   break
  with open(file,"r") as f:
   lines=f.readlines()
   for line in lines:
    if line.replace("\n","").lower()=="order type: out":
     count+=1
     break
  i+=1
 return count
OutOrders=TakeAway("invoices")
#print("Number of Take Away Orders:",OutOrders)

#--------------Calculating the Number of items--------------#

def itemsCount(folderName):
 folder=Path(folderName)
 inItems={}
 outItems={}
 i=1
 while True:
  file=folder/f"invoice{i}.txt"
  if not file.exists():
   break
  with open(file,"r") as f:
   lines=f.readlines()
  orderType=""
  current=""
  for line in lines:
   line=line.replace("\n","").replace("\r","")
   if "order type: in" in line.lower():
    orderType="in"
   elif "order type: out" in line.lower():
    orderType="out"
   elif "item:" in line.lower():
    index=line.lower().find("item:")
    current=line[index+5:].strip().capitalize()
   elif "quantity:" in line.lower() and current:
    q=line.lower().find("quantity:")
    strQuantity=line[q+9:].replace(" ", "")
    if strQuantity.isdigit():
     quantity=int(strQuantity)
     if orderType=="in":
      if current not in inItems:
        inItems[current]=0
      inItems[current]+=quantity
     elif orderType=="out":
      if current not in outItems:
        outItems[current]=0
      outItems[current]+=quantity
  i+=1
 return inItems, outItems
inItems,outItems=itemsCount("invoices")
#print(inItems,outItems)

#--------------Displays a sales summary--------------#


labels = {
    "Hummous": "dishes",
    "Fool": "dishes",
    "Falafel": "portions",
    "Tea": "cups",
    "Cola": "cans",
    "Water": "bottles"
}

def generateSummary():
   
    lines = []
    lines.append("Daily Sales Summary: ")
    lines.append("--------------------------------")
    lines.append(f"Total orders: {total_orders}\n")  
    
    lines.append(f"Orders In-Restaurant: {inOrders}")
    for item, quantity in sorted(inItems.items(), key=lambda x: x[0]):
        lines.append(f"{item} ({labels.get(item, '')}): {quantity}")
    lines.append("")  
    #Empty line
    
    lines.append(f"Orders Takeaway: {OutOrders}")
    for item, quantity in sorted(outItems.items(), key=lambda x: x[0]):
        lines.append(f"{item} ({labels.get(item, '')}): {quantity}")
    
    return "\n".join(lines)

summary_text = generateSummary()
print(summary_text)


with open("output.txt", "w") as f:
    f.write(summary_text)




