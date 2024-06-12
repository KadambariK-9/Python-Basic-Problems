import datetime

class VendorContractManagementSystem:
    def __init__(self):
        self.vendors = {}
        self.contracts = {}

    def create_vendor(self, vendor_id, vendor_name,vendor_contactno):
        if vendor_id not in self.vendors:
            self.vendors[vendor_id] = {
                'name': vendor_name,
                'vendor_id': vendor_id,
                'contact_number': vendor_contactno
            }
            print(f"Vendor {vendor_name} created successfully.")
        else:
            print(f"Vendor with ID {vendor_id} already exists.")

    def update_vendor(self, vendor_id, name, contact_person, contact_number):
        if vendor_id in self.vendors:
            self.vendors[vendor_id]['name'] = name
            self.vendors[vendor_id]['contact_person'] = contact_person
            self.vendors[vendor_id]['contact_number'] = contact_number
            print(f"Vendor {name} updated successfully.")
        else:
            print(f"Vendor with ID {vendor_id} not found.")

    def read_vendor(self, vendor_id):
        if vendor_id in self.vendors:
            print(f"Vendor ID: {vendor_id}")
            print(f"Name: {self.vendors[vendor_id]['name']}")
            print(f"Contact Person: {self.vendors[vendor_id]['contact_person']}")
            print(f"Contact Number: {self.vendors[vendor_id]['contact_number']}")
        else:
            print(f"Vendor with ID {vendor_id} not found.")

    def delete_vendor(self, vendor_id):
        if vendor_id in self.vendors:
            del self.vendors[vendor_id]
            print(f"Vendor deleted successfully.")
        else:
            print(f"Vendor with ID {vendor_id} not found.")

    def create_contract(self, contract_id, vendor_id, start_date, end_date, value):
        if contract_id not in self.contracts:
            self.contracts[contract_id] = {
                'vendor_id': vendor_id,
                'start_date': start_date,
                'end_date': end_date,
                'value': value
            }
            print(f"Contract {contract_id} created successfully.")
        else:
            print(f"Contract with ID {contract_id} already exists. Choose a different ID.")

    def update_contract(self, contract_id, start_date, end_date, value):
        if contract_id in self.contracts:
            self.contracts[contract_id]['start_date'] = start_date
            self.contracts[contract_id]['end_date'] = end_date
            self.contracts[contract_id]['value'] = value
            print(f"Contract {contract_id} updated successfully.")
        else:
            print(f"Contract with ID {contract_id} not found.")

    def read_contract(self, contract_id):
        if contract_id in self.contracts:
            print(f"Contract ID: {contract_id}")
            print(f"Vendor ID: {self.contracts[contract_id]['vendor_id']}")
            print(f"Start Date: {self.contracts[contract_id]['start_date']}")
            print(f"End Date: {self.contracts[contract_id]['end_date']}")
            print(f"Value: {self.contracts[contract_id]['value']}")
        else:
            print(f"Contract with ID {contract_id} not found.")

    def delete_contract(self, contract_id):
        if contract_id in self.contracts:
            del self.contracts[contract_id]
            print(f"Contract deleted successfully.")
        else:
            print(f"Contract with ID {contract_id} not found.")

    def alert_contract_expiry(self, contract_id):
        if contract_id in self.contracts:
            expiry_date = datetime.datetime.strptime(self.contracts[contract_id]['end_date'], "%Y-%m-%d").date()
            current_date = datetime.date.today()
            days_until_expiry = (expiry_date - current_date).days

            if days_until_expiry <= 30:
                print(f"Alert: Contract {contract_id} is nearing its expiry date. {days_until_expiry} days left.")
            else:
                print(f"Contract {contract_id} is not nearing its expiry date.")
        else:
            print(f"Contract with ID {contract_id} not found.")

    def evaluate_vendor_performance(self, vendor_id):
        if vendor_id in self.vendors:
            # Implement vendor performance evaluation logic here
            # You can use performance metrics and calculate a performance rating
            print(f"Evaluating performance for Vendor ID {vendor_id}...")
        else:
            print(f"Vendor with ID {vendor_id} not found.")
management_system = VendorContractManagementSystem()
while True:
    print('..........................................................')
    print('1. Create 2. Read 3. Update 4. Delete 5.Expiray 6.Performance of vendor')
    print('..........................................................')
    ch=int(input('Enter your choice'))
    if ch==1:
         vendor_id=int(input('Enter vendor id:'))
        vendor_name=input('Enter the vendor name:')
        vendor_contactno=int(input('Enter vendor contact number:'))
        management_system.create_vendor(vendor_id,vendor_name,vendor_contactno)
        management_system.create_contract()
    elif ch==2:
        management_system.read_vendor()
        management_system.read_contract()
    elif ch==3:
        break


.............................................................
#







Example Usage:
management_system = VendorContractManagementSystem()

# Create Vendors
management_system.create_vendor(1, "Vendor A", "John Doe", "123-456-7890")
management_system.create_vendor(2, "Vendor B", "Jane Smith", "987-654-3210")

# Create Contracts
management_system.create_contract(101, 1, "2023-01-01", "2023-12-31", 50000)
management_system.create_contract(102, 2, "2023-02-01", "2023-11-30", 70000)

# Update Vendor
management_system.update_vendor(1, "Vendor A Updated", "John Doe Jr.", "555-555-5555")

# Read Vendor
management_system.read_vendor(1)

# Delete Vendor
management_system.delete_vendor(2)

# Update Contract
management_system.update_contract(101, "2023-01-01", "2023-12-31", 60000)

# Read Contract
management_system.read_contract(101)

# Delete Contract
management_system.delete_contract(102)

# Alert Contract Expiry
management_system.alert_contract_expiry(101)

# Evaluate Vendor Performance
management_system.evaluate_vendor_performance(1)


















import datetime

# Vendor and Contract Management System

# Data storage
vendors = {}
contracts = {}

# Function to create a new vendor profile
def create_vendor(vendor_id, vendor_name):
    vendors[vendor_id] = {'name': vendor_name, 'contracts': []}
    print(f"Vendor '{vendor_name}' with ID '{vendor_id}' created successfully.")

# Function to read vendor details
def read_vendor(vendor_id):
    if vendor_id in vendors:
        return vendors[vendor_id]
    else:
        print(f"Vendor with ID '{vendor_id}' not found.")

# Function to update vendor details
def update_vendor(vendor_id, vendor_name):
    if vendor_id in vendors:
        vendors[vendor_id]['name'] = vendor_name
        print(f"Vendor '{vendor_name}' with ID '{vendor_id}' updated successfully.")
    else:
        print(f"Vendor with ID '{vendor_id}' not found.")

# Function to delete a vendor
def delete_vendor(vendor_id):
    if vendor_id in vendors:
        del vendors[vendor_id]
        print(f"Vendor with ID '{vendor_id}' deleted successfully.")
    else:
        print(f"Vendor with ID '{vendor_id}' not found.")

# Function to create a new contract
def create_contract(contract_id, vendor_id, expiry_date):
    if vendor_id in vendors:
        contracts[contract_id] = {'vendor_id': vendor_id, 'expiry_date': expiry_date}
        vendors[vendor_id]['contracts'].append(contract_id)
        print(f"Contract with ID '{contract_id}' created successfully.")
    else:
        print(f"Vendor with ID '{vendor_id}' not found.")

# Function to read contract details
def read_contract(contract_id):
    if contract_id in contracts:
        return contracts[contract_id]
    else:
        print(f"Contract with ID '{contract_id}' not found.")

# Function to update contract details
def update_contract(contract_id, expiry_date):
    if contract_id in contracts:
        contracts[contract_id]['expiry_date'] = expiry_date
        print(f"Contract with ID '{contract_id}' updated successfully.")
    else:
        print(f"Contract with ID '{contract_id}' not found.")

# Function to delete a contract
def delete_contract(contract_id):
    if contract_id in contracts:
        vendor_id = contracts[contract_id]['vendor_id']
        del contracts[contract_id]
        vendors[vendor_id]['contracts'].remove(contract_id)
        print(f"Contract with ID '{contract_id}' deleted successfully.")
    else:
        print(f"Contract with ID '{contract_id}' not found.")

# Function to alert when a contract is nearing its expiry date
def alert_contract_expiry(contract_id):
    if contract_id in contracts:
        = contracts[contract_id]['expiry_date']
        today = datetime.date.today()
        days_remaining = (expiry_date - today).days

        if days_remaining <= 30:
            print(f"Alert: Contract with ID '{contract_id}' is nearing its expiry date. {days_remaining} days remaining.")
        else:
            print(f"No alert: Contract with ID '{contract_id}' has {days_remaining} days remaining.")
    else:
        print(f"Contract with ID '{contract_id}' not found.")

# Function to evaluate and rate a vendor based on performance metrics
def evaluate_vendor_performance(vendor_id):
    if vendor_id in vendors:
        # Your evaluation logic goes here
        print(f"Vendor '{vendors[vendor_id]['name']}' with ID '{vendor_id}' evaluated successfully.")
    else:
        print(f"Vendor with ID '{vendor_id}' not found.")

# Example usage
create_vendor('V1', 'Vendor 1')
create_contract('C1', 'V1', datetime.date(2023, 12, 31))
alert_contract_expiry('C1')
evaluate_vendor_performance('V1')
update_contract('C1', datetime.date(2023, 11, 30))
alert_contract_expiry('C1')
delete_vendor('V1')
read_vendor('V1')









import datetime

class VendorContractManagementSystem:
    def __init__(self):
        self.vendors = {}
        self.contracts = {}

    def create_vendor(self):
        vendor_id=int(input('Enter vendor id:'))
        vendor_name=input('Enter the vendor name:')
        vendor_contactno=int(input('Enter vendor contact number:'))
        if vendor_id not in self.vendors:
            self.vendors[vendor_id] = {
                'name': vendor_name,
                'vendor_id': vendor_id,
                'contact_number': vendor_contactno
            }
            print(f"Vendor {vendor_name} created successfully.")
        else:
            print(f"Vendor with ID {vendor_id} already exists")

    def update_vendor(self):
        if self.vendor_id in self.vendors:
            self.vendors[vendor_id]['vendor_name'] =vendor_name
            self.vendors[vendor_id]['vendor_id'] = vendor_id
            self.vendors[vendor_id]['vendor_contactno'] = vendor_contactno
            print(f"Vendor {vendor_name} updated successfully.")
        else:
            print(f"Vendor with ID {vendor_id} not found.")

    def read_vendor(self):
        if self.vendor_id in self.vendors:
            print(f"Vendor ID: {self.vendor_id}")
            print(f"Vendor Name: {self.vendors[self.vendor_id]['self.vendor_name']}")
            print(f"Contact Number: {self.vendors[self.vendor_id]['self.vendor_contactno']}")
        else:
            print(f"Vendor with ID {self.vendor_id} not found.")

    def delete_vendor(self, vendor_id):
        if vendor_id in self.vendors:
            del self.vendors[vendor_id]
            print(f"Vendor deleted successfully.")
        else:
            print(f"Vendor with ID {vendor_id} not found.")

    def create_contract(self):#, contract_id, vendor_id, start_date, end_date, value):
        contract_id=int(input('Enter contract id:'))
        vendor_id=int(input('Enter vendor id:'))
        start_date=input('Enter start date :')
        end_date=input('Enter end date:')
        value=int(input('Enter value:'))
        if contract_id not in self.contracts:
            self.contracts[contract_id] = {
                'vendor_id': vendor_id,
                'start_date': start_date,
                'end_date': end_date,
                'value': value
            }
            print(f"Contract {contract_id} created successfully.")
        else:
            print(f"Contract with ID {contract_id} already exists. Choose a different ID.")

    def update_contract(self, contract_id, start_date, end_date, value):
        if contract_id in self.contracts:
            self.contracts[contract_id]['start_date'] = start_date
            self.contracts[contract_id]['end_date'] = end_date
            self.contracts[contract_id]['value'] = value
            print(f"Contract {contract_id} updated successfully.")
        else:
            print(f"Contract with ID {contract_id} not found.")

    def read_contract(self):
        if self.contract_id in self.contracts:
            print(f"Contract ID: {self.contract_id}")
            print(f"Vendor ID: {self.contracts[selfcontract_id]['self.vendor_id']}")
            print(f"Start Date: {self.contracts[contract_id]['start_date']}")
            print(f"End Date: {self.contracts[contract_id]['end_date']}")
            print(f"Value: {self.contracts[contract_id]['value']}")
        else:
            print(f"Contract with ID {contract_id} not found.")

    def delete_contract(self, contract_id):
        if contract_id in self.contracts:
            del self.contracts[contract_id]
            print(f"Contract deleted successfully.")
        else:
            print(f"Contract with ID {contract_id} not found.")

    def alert_contract_expiry(self, contract_id):
        if contract_id in self.contracts:
            expiry_date = datetime.datetime.strptime(self.contracts[contract_id]['end_date'], "%Y-%m-%d").date()
            current_date = datetime.date.today()
            days_until_expiry = (expiry_date - current_date).days

            if days_until_expiry <= 30:
                print(f"Alert: Contract {contract_id} is nearing its expiry date. {days_until_expiry} days left.")
            else:
                print(f"Contract {contract_id} is not nearing its expiry date.")
        else:
            print(f"Contract with ID {contract_id} not found.")

    def evaluate_vendor_performance(self, vendor_id):
        if vendor_id in self.vendors:
            # Implement vendor performance evaluation logic here
            # You can use performance metrics and calculate a performance rating
            print(f"Evaluating performance for Vendor ID {vendor_id}...")
        else:
            print(f"Vendor with ID {vendor_id} not found.")
management_system = VendorContractManagementSystem()
while True:
    print('..........................................................')
    print('1. Create 2. Read 3. Update 4. Delete 5.Expiray 6.Performance of vendor')
    print('..........................................................')
    ch=int(input('Enter your choice'))
    if ch==1:
        management_system.create_vendor()
        management_system.create_contract()
    elif ch==2:
        management_system.read_vendor()
        management_system.read_contract()
    elif ch==3:
        break
        
        
    






'''
# Example Usage:
management_system = VendorContractManagementSystem()

# Create Vendors
management_system.create_vendor(1, "Vendor A", "John Doe", "123-456-7890")
management_system.create_vendor(2, "Vendor B", "Jane Smith", "987-654-3210")

# Create Contracts
management_system.create_contract(101, 1, "2023-01-01", "2023-12-31", 50000)
management_system.create_contract(102, 2, "2023-02-01", "2023-11-30", 70000)

# Update Vendor
management_system.update_vendor(1, "Vendor A Updated", "John Doe Jr.", "555-555-5555")

# Read Vendor
management_system.read_vendor(1)

# Delete Vendor
management_system.delete_vendor(2)

# Update Contract
management_system.update_contract(101, "2023-01-01", "2023-12-31", 60000)

# Read Contract
management_system.read_contract(101)

# Delete Contract
management_system.delete_contract(102)

# Alert Contract Expiry
management_system.alert_contract_expiry(101)

# Evaluate Vendor Performance
management_system.evaluate_vendor_performance(1)









Vendor and Contract Management System
.CRUD:Vendor profiles and contracts
.alert_contract_expiry(contract_id):Alert when a contract is nearing its expiry date.
.evaluate_vendor_performance(vendor_id):Evaluate and rate a vendor based on performance metrics.
d={}
def create_vendor_profile(self):
    print('......OIL Contract......')
        
def read_vendor_profile(self):
    global finance
    print('.........VENDOR DETAILS..........')
    ven_name=input('Enter vendor Name')
    ven_phno=int(input('Enter vendor Contact no'))
    ven_age=int(input('Enter age of vendor'))
    ven_from=input('Enter vendor location')
    ven_id=int(input('Enter vendor ID'))
    print('..........CLIENT DETAILS............')
    clnt_id=int(input('Enter client ID'))
    clnt_name=input('Enter client name')
    clnt_phno=int(input('Enter client Contact no'))
    clnt_age=int(input('Enter age of client'))
    
def update_vendor_profile():
#after adding extra contracts need to update the details
def delete_vendor_profile():
#after end date delete the contract details and update again


def alert_contract_expiray(contract_id):
    #when a contract is nearing its expiray date
def evaluate_vendor_performanace(vendor_id):
    #eveluate the rate a vendor based on performance metrices


































class VendorContractManagementSystem:
    def __init__(self):
        self.vendors = {}
        self.contracts = {}

    def add_vendor(self, vendor_id, name, contact_person, email, phone):
        self.vendors[vendor_id] = {
            'name': name,
            'contact_person': contact_person,
            'email': email,
            'phone': phone,
            'contracts': []
        }

    def view_vendor(self, vendor_id):
        return self.vendors.get(vendor_id)

    def add_contract(self, contract_id, vendor_id, description, start_date, end_date):
        if vendor_id in self.vendors:
            contract = {
                'description': description,
                'start_date': start_date,
                'end_date': end_date
            }
            self.contracts[contract_id] = contract
            self.vendors[vendor_id]['contracts'].append(contract_id)
        else:
            print("Vendor not found.")

    def view_contract(self, contract_id):
        return self.contracts.get(contract_id)


# Example usage
vcms = VendorContractManagementSystem()

# Add vendors
vcms.add_vendor('V1', 'Vendor 1', 'John Doe', 'john@example.com', '123-456-7890')
vcms.add_vendor('V2', 'Vendor 2', 'Jane Smith', 'jane@example.com', '987-654-3210')

# View vendor details
print(vcms.view_vendor('V1'))

# Add contracts
vcms.add_contract('C1', 'V1', 'Contract 1', '2023-01-01', '2023-12-31')
vcms.add_contract('C2', 'V2', 'Contract 2', '2023-02-01', '2023-11-30')

# View contract details
print(vcms.view_contract('C1'))





























Vendor and Contract Management System
.CURD:Vendor profiles and contracts
.alert_contract_expiry(contract_id):Alert when a contract is nearing its expiry date.
.evaluate_vendor_performance(vendor_id):Evaluate and rate a vendor based on performance metrics.

class CURD:
    def create_vendor_profile(self):
        print('......OIL Contract......')
        
    def read_vendor_profile(self):
        global finance
        print('.........VENDOR DETAILS..........')
        ven_name=input('Enter vendor Name')
        ven_phno=int(input('Enter vendor Contact no'))
        ven_age=int(input('Enter age of vendor'))
        ven_from=input('Enter vendor location')
        ven_id=int(input('Enter vendor ID'))
        print('..........CLIENT DETAILS............')
        clnt_id=int(input('Enter client ID'))
        clnt_name=input('Enter client name')
        clnt_phno=int(input('Enter client Contact no'))
        clnt_age=int(input('Enter age of client'))
    
def update_vendor_profile():
    
   ''' 
