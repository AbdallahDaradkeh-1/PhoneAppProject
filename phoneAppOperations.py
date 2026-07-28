import shelve # This is store data in a file in the harddisk so They don't go once terminal session if over
import traceback


class PhoneApp:

  def __init__(self):
    self.contactsList = []
    self.favouriteList = []
    self.recentCalls = []

  def start(self):
    try:
      
      with shelve.open("my_local_storage") as db:
        self.loadedContacts = db.get("contacts_list", [])
        self.loadedFavouriteContacts = db.get("favourite_List", [])
        self.loadedRecentCalls = db.get("recent_call_list", [])
        self.contactsList = self.loadedContacts
        self.favouriteList = self.loadedFavouriteContacts
        self.recentCalls = self.loadedRecentCalls
        
        print("Data Have Been Loaded Successfully")
      while True:    
        print("Hello, Choose Number Of Operation You Would Like To Do:")
        print("1. Create A Contact")
        print("2. Print All Contacts Info")
        print("3. Print A Specific Contact Info")
        print("4. Exit")
        print("5. Do a Call To A Specific Person")
        print("6. Add A Contact To Favouratie List")
        print("7. Print All Favouratie Contacts")
        print("8. Print All Recent Calls")
        print("9. Delete A Contact")
        print("10. Change Contact Info")
        chosenOperation = int(input())
        
        if chosenOperation == 1:
          self.createContact()
        elif chosenOperation == 2:
          self.printContactsInfo()
        elif chosenOperation == 3:
          self.printContactInfo()
        elif chosenOperation == 4:
          print("Exiting Program...")
          return
        elif chosenOperation == 5:
          self.call()
        elif chosenOperation == 6:
          self.favouriteContacts()
        elif chosenOperation == 7:
          self.printFavouriteContacts()
        elif chosenOperation == 8:
          self.printRecentCallsList()
        elif chosenOperation == 9:
          self.deleteContacts()
        elif chosenOperation == 10:
          self.changeContactInfo()
        else:
          if chosenOperation < 1 or chosenOperation > 3:
                  print("Invalid Input!")
    except ValueError:
      print("Invalid Input Type!")
  
  def createContact(self):
    # Ask user to enter Contact details:
    #*
    # Right Now:
    # Name
    # Phone
    # *#
    try:
      print("Enter Contact Name")
      contactName = input()
      print("Enter Contact Phone")
      contactPhone = int(input())
      # Create a Contact Object and fill it with user info
      contact = Contact(contactName, contactPhone)
      self.contactsList.append(contact)
      print("Thank you, Contact has been created")
      with shelve.open("my_local_storage") as db:
          db['contacts_list'] = self.contactsList
          print("Contact Has been Saved Successfully")
    
    except ValueError:
       print("Invalid Input!")



  def printContactInfo(self):
    try:
      print("Enter Contact Name You search For:")
      contactName = input()

      if self.isEmpty():
              print("You don't Have any Contacts!")
      else:
        outcomes = 0
        # Show info for all contact that contain that name or something similar
        print("Available Contacts:")
        for contact in self.contactsList:
          if contactName.lower() in contact.name.lower():
            print(contact.name, contact.phone)
            outcomes += 1
        if outcomes == 0:
          print("No Such Contact exist")
    except ValueError:
      print("Invalid Input!")
    # شو لو كان ما فيه عنا ولا شخص ضايفينه على الإتصال

  def call(self):
    try:  
      # Show all available contacts
      print("Choose Number Of Contact you wanna call Such as '1'")
      print()
      
      i = self.shownAnOrderedContactsList()

      chosenContactNumber = int(input())
      if chosenContactNumber <= 0 or chosenContactNumber >= i:
        print("Invalid Input!")
      else:
        selectedContact = self.contactsList[chosenContactNumber - 1]
        print(selectedContact.name)
        print(selectedContact.phone)
        print("Calling...")
        print("Enter 1 To End The Call.")
        end = int(input())
        if end != 1:
          print("invalid Input")
        print("Call Has Been Ended!")
        self.recentCalls.append(selectedContact)
        with shelve.open("my_local_storage") as db:
          db["recent_call_list"] = self.recentCalls
          print("Call Has been added To Recent Calls Successfully!")
        return
    except ValueError:
      print("Invalid Input Type!")

  def favouriteContacts(self):
    try:
      # Show All Available Contacts To User
      print("Select Contacts Number You want to add to favourate list")
      # Let User choose Number of Contacts user want to add to favourate
      i = self.shownAnOrderedContactsList()
      chosenContactNumber = int(input())
      if chosenContactNumber <= 0 or chosenContactNumber >= i:
        print("Invalid Input!")
      else:
        self.favouriteList.append(self.contactsList[chosenContactNumber - 1])
        with shelve.open("my_local_storage") as db:
          db["favourite_List"] = self.favouriteList
          print("Contact Has Been Saved And Added To Favouraite List")
    except ValueError:
      print("InvalidInput")
  def printFavouriteContacts(self):
    
    for contact in self.favouriteList:
      print(contact.name, contact.phone)
      



  def isEmpty(self):
    if len(self.contactsList) == 0:
      return True
    else:
      return False
  def printContactsInfo(self):
    for contact in self.contactsList:
      print(contact.name, contact.phone)

  def shownAnOrderedContactsList(self):
    i = 1
    if self.isEmpty():
      print("Contacts List is Empty, You have not added any contact yet!")
      return
    for contact in self.contactsList:
            print(i, contact.name, contact.phone)
            i += 1
    
    return i
  def printRecentCallsList(self):
    for contact in self.recentCalls:
      print(contact.name, contact.phone)

  def deleteContacts(self):
    try:
      #Show All Contacts To User
      print("Choose Contact You want to delete such as '1':")
      i = self.shownAnOrderedContactsList()
      #User Choose From Contact using Contact Number Such as '1'
      selectedContactNumber = int(input())
      if selectedContactNumber <= 0 or selectedContactNumber >= i:
        print("Invalid Input, Out Of Range!")
        return
      #We check all other lists and delete related user info
      selectedContact = self.contactsList[selectedContactNumber - 1]
      self.deleteContactFromFavouriteList(selectedContact.name)
      self.deleteContactFromRecentCallsList(selectedContact.name)
      #We Delete User from Contact
      self.deleteUserFromContactsList(selectedContact.name)
      #Print Success Message
    except ValueError:
      print("Invalid Input Type!")
  def deleteContactFromFavouriteList(self, name):
    try:
      i = 0
      outcomes = 0
      if self.generalIsEmpty(self.favouriteList):
        print("Favourite List Is Empty")
      for contact in self.favouriteList:
        if name == contact.name:
          deletedContact = self.favouriteList.pop(i)
          print(deletedContact.name, "Has Been Deleted Sucessfully")
          with shelve.open("my_local_storage") as db:
            db["favourite_List"] = self.favouriteList
            print("Favourite List Has been Updated")
          return
          
        i += 1
      if outcomes == 0:
        print(name ,"There is no Such Contact in the Favourite List")
    except Exception as error:
      error_info = traceback.extract_tb(error.__traceback__)[-1]
      print("Error type:", type(error).__name__)
      print("Error message:", error)
      print("Line number:", error_info.lineno)
  def generalIsEmpty(self, list):
    if len(list) == 0:
      return True
    else:
      return False

  def deleteContactFromRecentCallsList(self, name):
        try:
          #Go Through All Contacts
          i = 0
          if self.generalIsEmpty(self.recentCalls):
            print("Recent Calls List is empty")
            return
          for contact in self.recentCalls:
            if name == contact.name:
              deletedContact = self.recentCalls.pop(i)
              print(deletedContact, "Has Been Deleted Successfully!")
              with shelve.open("my_local_storage") as db:
                  db["recent_call_list"] = self.favouriteList
                  print("recentCall List Has been Updated")
              return
              
            i += 0
          print(name, "No Such Contact in Recent Calls List")
          #Compare names
          #Delete Contact Using Pop
          #
        except Exception as error:
          error_info = traceback.extract_tb(error.__traceback__)[-1]
          print("Error type:", type(error).__name__)
          print("Error message:", error)
          print("Line number:", error_info.lineno)
  def deleteUserFromContactsList(self, name):
    i = 0
    if self.isEmpty():
      print("Contact List is Empty")
      return
    for contact in self.contactsList:
      if name == contact.name:
        deletedContact = self.contactsList.pop(i)
        print(deletedContact, "Contact Has Been Deleted Successfully")
        with shelve.open("my_local_storage") as db:
            db["contacts_list"] = self.favouriteList
            print("Contact List Has been Updated")
        return
      i+=1
    print(name,"No Such Contact Exist")

  def changeContactInfo(self):
    try:
      print("Choose Contact Number You want to change its info such as '1' ")
      i = self.shownAnOrderedContactsList()
      selectedNumber = int(input())
      if selectedNumber <= 0 or selectedNumber >= i:
        print("Invalid Input, Out Of Range!")
      print("Enter New Name")
      chosenName = input()
      print("Enter New Phone")
      chosenPhone = int(input())
      oldName = self.contactsList[selectedNumber - 1].name
      oldPhone = self.contactsList[selectedNumber - 1].phone

      self.contactsList[selectedNumber - 1].name = chosenName
      self.contactsList[selectedNumber - 1].phone = chosenPhone

      favouriteContactIndex =  self.generalListofContactsSearch(self.favouriteList, oldName)
      self.favouriteList[favouriteContactIndex].name = chosenName
      self.favouriteList[favouriteContactIndex].phone = chosenPhone
      recentCallsContactIndex = self.generalListofContactsSearch(self.recentCalls, oldName)
      self.recentCalls[recentCallsContactIndex].name = chosenName
      self.recentCalls[favouriteContactIndex].phone = chosenPhone
      
      with shelve.open("my_local_storage") as db:
        db["contacts_list"] = self.contactsList
        db["favourite_List"] = self.favouriteList
        db["recent_call_list"] = self.recentCalls
        print("Contact Has Been Updated", self.contactsList[selectedNumber - 1].name)
        print("Favourite Contact Has Been Updated", self.favouriteList[favouriteContactIndex].name)
        print("RecentCalls Has Been Updated", self.recentCalls[recentCallsContactIndex].name)


    except Exception as error:
              error_info = traceback.extract_tb(error.__traceback__)[-1]
              print("Error type:", type(error).__name__)
              print("Error message:", error)
              print("Line number:", error_info.lineno)
  def generalListofContactsSearch(self, contactsTypelist, name):
    # get list and name of contact
    i = 0
    
    for contact in contactsTypelist:
      if contact.name == name:
        print(contact.name, contact.phone)
        return i
      i += 1
    print("Contact is Not Exist In This List!")
    return -1


# بدي أطبع المعلومات هي
#بدي أعمل كلاس اسمه Contact
# يحتوي معلومات الإتصال

class Contact:
  def __init__(self, person_name, person_phone):
    # شو الأشياء اللي بنحتاجها للإتصال
    #الإسم
    self.name = person_name
    self.phone = person_phone
  
  
# أنا بقدر أعمل متغيرات عشان ألم المعلومات
# بس بما إنه عندي معلومات لشيء واحد واللي هي معلومات الإتصال
# بدي أعمل نموذج(كلاس) بحتوي على كل المعلومات ذات الصلة
# ملاحظة: أنا ما بعمل خطوات احترافية أنا بعمل التطبيق عشان أتعلم


# Test

phoneApp = PhoneApp()
phoneApp.start()