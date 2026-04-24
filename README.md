# Daily Sales Summary Project

## Students info
- Shahd Shwekeyeh - 1222105 sec#1
- Ghada Sawalha - 1220064 sec#1
---------------------------------------------------------------------------
## What This Program Does
This program reads invoice files from the "invoices" folder and calculates: 
- Total number of orders 
- Number of In-Restaurant (Dine-In) orders
- Number of Takeaway orders 
- Number of each item sold 

It shows the daily sales summary on the terminal and saves it in "output.txt".

----------------------------------------------------------------------------

## How to Use

1. Put all invoice files inside the "invoices" folder. 
invoice example:
Order Type: In
Item: Hummous
Quantity: 2
Price per item: 3.0
Total price: 6.0

2. Run the Python script:

```bash
python daily_sales_summary.py
----------------------------------------------------------------------------
#Output Emample:
Daily Sales Summary:
--------------------------------
Total orders: 4

Orders In-Restaurant: 2
Falafel (portions): 3
Fool (dishes): 3
Hummous (dishes): 2
Tea (cups): 9

Orders Takeaway: 2
Tea (cups): 3
Water (bottles): 3
-----------------------------------------------------------------------------
#Project Folder Structure
project2 --
           |    
           invoices
           |
           main.py
           |
           README.md
