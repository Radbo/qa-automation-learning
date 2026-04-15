user_shopping_list_items = "milk, bread, eggs, cheese, fruits"

shopping_list = user_shopping_list_items.split(", ")
shopping_list[0] = shopping_list[0].strip()
shopping_list[1] = shopping_list[1].strip()
shopping_list[2] = shopping_list[2].strip()
shopping_list[3] = shopping_list[3].strip()
shopping_list[4] = shopping_list[4].strip()

user_shopping_list_items_delete = input("Enter the name of the product you want to delete from the shopping list: ")
if user_shopping_list_items_delete in shopping_list:
    shopping_list.remove(user_shopping_list_items_delete)
    print(f"{user_shopping_list_items_delete} has been removed from your shopping list.")
else:    print(f"{user_shopping_list_items_delete} is not in your shopping list.")
user_shopping_list_add = input("Enter the name of the product you want to add to the shopping list: ")
shopping_list.append(user_shopping_list_add)
shopping_list.sort()
print(joined_shopping_list := ", ".join(shopping_list))
