import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]

product_per_supplier = {}

print("Max Rows:", product_list.max_row)
print("Max Columns:", product_list.max_column)

for product_row in range(2, product_list.max_row + 1):
    supplier_name = product_list.cell(product_row, 4).value  # Column 4 = Supplier
    #print(f"Row {product_row}, Supplier: {supplier_name}")  # Debugging

    if supplier_name is None:
        continue  # Skip rows with empty supplier names

    if supplier_name in product_per_supplier:
        current_num_products = product_per_supplier.get(supplier_name)
        product_per_supplier[supplier_name] = current_num_products + 1
    else:
        print("Adding a new supplier:", supplier_name)
        product_per_supplier[supplier_name] = 1

#print("Final Product Per Supplier Dictionary:")
print(product_per_supplier)

# product_per_supplier = {}
# print(product_list.max_row)
# print(product_list.max_column)
#
# for product_row in range(2, product_list.max_row +1):
#     supplier_name = product_list.cell(product_row, 4).value
#     #print(supplier_name)
#
#     if supplier_name in product_per_supplier:
#         current_num_products = product_per_supplier[supplier_name]
#         product_per_supplier[supplier_name] = current_num_products + 1
#     else:
#         print("adding a new supplier")
#         product_per_supplier[supplier_name] = 1
#
# print(product_per_supplier)