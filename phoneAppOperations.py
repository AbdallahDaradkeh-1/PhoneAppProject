import shelve # This is store data in a file in the harddisk so They don't go once terminal session if over


class PhoneApp:

  def __init__(self):
    self.contactsList = []
    self.favouriteList = []


  def start(self):
    try:
      
      with shelve.open("my_local_storage") as db:
        self.loadedContacts = db.get("contacts_list", [])
        self.loadedFavouriteContacts = db.get("favourite_List", [])
        self.contactsList = self.loadedContacts
        self.favouriteList = self.loadedFavouriteContacts
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
      print("Choose Number Of Contact Such as '1' you wanna call")
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
          print("Has Been Saved And Added To Favouraite List")
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
    for contact in self.contactsList:
            print(i, contact.name, contact.phone)
            i += 1
    return i
  
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