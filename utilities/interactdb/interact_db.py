from utilities.db.db_manager import dbManager

# New Class for interact with DB
class interact_db:
    def __init__(self):
      pass

    # Get - All products details
    def get_products(self):
        products_query = "Select * From product"
        return dbManager.fetch(products_query)

        # Get - All users details
    def get_users(self):
            users_query = "Select * From users"
            return dbManager.fetch(users_query)

        # Get - All open orders
    def get_orders(self):
            orders_query = "Select order_id From orders  where status=open"
            return dbManager.fetch(orders_query)
    #Need to add status to table




# Creates an instance for the interactDB class for export.
interactDb = interactDB()bManager.fetch(products_query)

