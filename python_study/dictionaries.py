# Dictionaries
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# looks like the key has to be strings
print(customer["name"])
    # case sensitive when looking for keys
    # this throws an error if the key does not exist
print(customer.get("name"))
    # dictionary.get(key) does not throw an error
print(customer.get("birthdate", "07-07-1996")) 
    # dictionary.get(key, value) can be used to assign a default value to a new key so that this 
    # value appears if there is no value associated with the given key, but does not add it to the dictionary
customer["birthdate"] = "07-07-1996" 
    # you can add new key value pairs to a dictionary like this 
print(customer)
