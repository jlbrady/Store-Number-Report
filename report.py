#usr/bin/python

import csv

# TODO: Check for people with extra spaces in their name etc.
# All mistaken "No store number" outputs are from orders that Nick/Dan placed in the very beginning.


"""
################################ INSTRUCTIONS ################################
==============================================================================

Create / Enter directory containing:
	1) This file 
	2) Default template customers .csv export
		* Title this file customers.csv
	3) Peachtree accounting template orders .csv export
		* Title this file orders.csv

Run python application on a linux CLI: "$ python3 ./report.py" (Python 2 works too)
OR
Run this application by double clicking on the file in the folder containing
the above files.

Output should be a file titled "UPDATED_ORDERS.csv"

==============================================================================
"""


def add_col_names():
	"""Creates list containing column names to add to ln 1 of output .csv."""
	columns = []
	columns.append("Customer ID")
	columns.append("Invoice/CM #") 
	columns.append("Date")
	columns.append("Ship to Name")
	columns.append("Ship to City")
	columns.append("Ship to State")
	columns.append("Store ID")
	columns.append("Quantity")
	columns.append("Description")
	columns.append("Unit Price")
	columns.append("UPC/SKU")
	columns.append("Amount")

	return columns


def create_row(row, cust_dict):
	"""Turns individual "orders.csv" row dict obj into list for output .csv."""
	output = []
	output.append(row["Customer ID"])
	output.append(row["Invoice/CM #"]) 
	output.append(row["Date"])
	output.append(row["Ship to Name"])
	output.append(row["Ship to City"])
	output.append(row["Ship to State"])

	if row["Customer ID"] in cust_dict:
		if cust_dict[row["Customer ID"]] is not '':
			output.append(cust_dict[row["Customer ID"]])
		else:
			output.append("Account missing store number")
	else:
		output.append("Cust ID not in cust_dict(), acc likely deleted")

	output.append(row["Quantity"])
	output.append(row["Description"])
	output.append(row["Unit Price"])
	output.append(row["UPC/SKU"])
	output.append(row["Amount"])

	return output


def read_customer_csv(cust_dict):
	"""Opens and reads "customers.csv" file.

	Stores customer info in dictionary data structure for update_order_file().
	customer_dict[cust_id] == cust_store_num.
	"""
	with open('customers.csv') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',')
		line_count = 0

		for row in csv_reader:
			if line_count != 0:
				cust_dict[row["Customer ID"]] = row["Store Number"]
				line_count += 1
			else:
				line_count += 1

		return cust_dict


def update_order_file(cust_dict):
	"""Creates "UPDATED_ORDERS.csv".

	"UPDATED_ORDERS.csv" contains relevant franchisee store information
	including amount of each SKU purchased on a store by store basis.
	* One store ID number per bigcommerce account.
	* Corrects incorrect store_id data in older orders.
	"""
	with open('orders.csv') as csv_file:
		with open('UPDATED_ORDERS.csv', 'w', newline='') as out_file:

			csv_reader = csv.DictReader(csv_file, delimiter=',')
			csv_writer = csv.writer(out_file, delimiter=',')
			csv_writer.writerow(add_col_names())

			for row in csv_reader:
				output = create_row(row, cust_dict)			
				csv_writer.writerow(output)

		return


def main():
	cust_dict = dict()
	cust_dict = read_customer_csv(cust_dict)
	update_order_file(cust_dict)

	return 1

"""
==============================================================================

Function definitions above.
Application below.

==============================================================================
"""
main()