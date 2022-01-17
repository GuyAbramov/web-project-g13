from utilities.db.db_manager import dbManager

# New Forms Class for interact with DB
class Forms:
    def __init__(self):
      pass

    # Login Page - Set - Registration New User
    def create_user(self, Email, First_Name, Last_Name, phone ,password):
            query = "INSERT INTO users (Email,First_Name,Last_Name,Phone,password) VALUES ('%s','%s','%s','%s','%s')" \
                    % (Email, First_Name, Last_Name, phone, password)
            dbManager.commit(query)
            return True

    # Login Page - Check User in DB
    def checkUser (self, email, password):
        return dbManager.fetch(f"Select * From users WHERE Email='{email}' AND password='{password}'")


    # Set - Update new password for user
    def changePassword(self, email, newpassword):
        query = "UPDATE users SET password = '%s' WHERE Email='%s'" % (newpassword, email)
        dbManager.commit(query)
        return True


    # Delete user from DB
    def deleteUser(self, email):
        query = "DELETE FROM users WHERE Email='%s'" % email
        dbManager.commit(query)
        return True



# Creates an instance for the forms class for export.
forms = Forms()


