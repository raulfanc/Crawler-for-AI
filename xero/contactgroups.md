# Contact Groups

[Try in API Explorer](https://api-explorer.xero.com/accounting/contactgroups)

## Overview

[](/documentation/api/accounting/contactgroups#overview)

|   
---|---  
URL| <https://api.xero.com/api.xro/2.0/ContactGroups>  
Methods Supported| [GET](/documentation/api/accounting/contactgroups#get-contactgroups), [PUT](/documentation/api/accounting/contactgroups#put-contactgroups), [POST](/documentation/api/accounting/contactgroups#post-contactgroups), [DELETE](/documentation/api/accounting/contactgroups#delete-contactgroups)  
Description| Allows you to retrieve the ContactID and Name of all the contacts in a contact group   
Allows you to create contact groups   
Allows you to rename contact groups   
Allows you to update the status (delete) contact groups   
Allows you to add contacts to a contact group   
Allows you to remove a contact from a contact group   
Allows you to remove all contacts from a contact group  
  
## GET ContactGroups

[](/documentation/api/accounting/contactgroups#get-contactgroups)

The following elements are returned in a ContactGroups response

|   
---|---  
Name| The Name of the contact group. Required when creating a new contact group  
Status| The Status of a contact group. Only contact groups with a status of ACTIVE are returned on GETs.  
ContactGroupID| The Xero generated identifier for contact groups (unique within organisations)  
Contacts| The ContactID and Name of [Contacts](/documentation/api/accounting/contacts) in a contact group. Returned on GETs when the ContactGroupID is supplied in the URL.  
  
### Optional parameters for GET ContactGroups

|   
---|---  
ContactGroupID| The Xero identifier for an contact group  
Where| Filter by an any element ( _see[Filters](/documentation/api/accounting/requests-and-responses#retrieving-modified-resources)_ )  
order| Order by any element returned ( _see[Order By](/documentation/api/accounting/requests-and-responses#ordering-of-results)_ )  
  
Example response for GET ContactGroups
    
    
    GET https://api.xero.com/api.xro/2.0/ContactGroups

copy code
    
    
    {
      "ContactGroups": [
        {
          "ContactGroupID": "97bbd0e6-ab4d-4117-9304-d90dd4779199",
          "Name": "VIP Customers",
          "Status": "ACTIVE"
        },{
          "ContactGroupID": "d0c68f1a-e5dd-4a45-aa02-27d8fdbfd562",
          "Name": "Preferred Suppliers",
          "Status": "ACTIVE"
        }
      ]
    }
    
    

copy code

Example response for retrieving a single ContactGroup
    
    
    GET https://api.xero.com/api.xro/2.0/ContactGroups/97bbd0e6-ab4d-4117-9304-d90dd4779199

copy code
    
    
    {
      "ContactGroups": [
        {
          "ContactGroupID": "97bbd0e6-ab4d-4117-9304-d90dd4779199",
          "Name": "Adam's Contacts",
          "Status": "ACTIVE",
          "Contacts": [
            {
              "ContactID": "9ce626d2-14ea-463c-9fff-6785ab5f9bfb",
              "Name": "Boom FM"
            },{
              "ContactID": "b9d4332a-26a3-4577-8db2-6e830d4b07cd",
              "Name": "Berry Brew"
            },{
              "ContactID": "2dc0ef7c-582f-4542-963b-dbdc069e4819",
              "Name": "Bayside Wholesale"
            }
          ]
        }
      ]
    }
    
    

copy code

## POST ContactGroups

[](/documentation/api/accounting/contactgroups#post-contactgroups)

Use this method to create or update contact groups.

**Note:** You can't create more than 100 contact groups. Trying to create a group when the limit of 100 has been reached will result in a validation error being returned.

The following elements can be supplied in a POST request

|   
---|---  
Name| The Name of the contact group. Required when creating a new contact group  
Status| The Status of a contact group. To delete a contact group update the status to DELETED.  
Contacts| The ContactID and Name of [Contacts](/documentation/api/accounting/contacts) in a contact group. Add Contacts to a ContactGroup using the [PUT](/documentation/api/accounting/contactgroups#put-contactgroups) method.  
  
Example request to create a new contact group
    
    
    POST https://api.xero.com/api.xro/2.0/ContactGroups

copy code
    
    
    {
      "Name": "VIP Customers"
    }
    
    

copy code

Example request to rename a contact group
    
    
    POST https://api.xero.com/api.xro/2.0/ContactGroups/679382fd-7a71-4281-b013-0ff811ca87ab

copy code
    
    
    {
      "ContactGroupID": "679382fd-7a71-4281-b013-0ff811ca87ab",
      "Name": "New Name Here"
    }
    
    

copy code

Example request to delete a contact group
    
    
    POST https://api.xero.com/api.xro/2.0/ContactGroups/679382fd-7a71-4281-b013-0ff811ca87ab

copy code
    
    
    {
      "ContactGroupID": "679382fd-7a71-4281-b013-0ff811ca87ab",
      "Status": "DELETED"
    }
    
    

copy code

## PUT ContactGroups

[](/documentation/api/accounting/contactgroups#put-contactgroups)

The PUT method is similar to the POST method however you can only create new contact groups. You can also use the PUT method to add contacts to a contact group.

To add contacts to a contact group use the following url /ContactGroups/_ContactGroupID_ /Contacts

Example request to add contacts to a contact group
    
    
    PUT https://api.xero.com/api.xro/2.0/ContactGroups/b05466c8-dc54-4ff8-8f17-9d7008a2e44b/Contacts

copy code
    
    
    {
      "Contacts": [
        {
          "ContactID": "7f01ac80-bd2a-4aad-acaa-80b4b606ae49"
        },{
          "ContactID": "4bfd2f5b-f211-4240-ac6f-635543fb68e6"
        }
      ]
    }
    
    

copy code

## DELETE ContactGroups

[](/documentation/api/accounting/contactgroups#delete-contactgroups)

The DELETE method is used to remove a contact from a contact group or remove all contacts from a contact group.

Remove a contact from a contact group
    
    
    DELETE https://api.xero.com/api.xro/2.0/ContactGroups/b05466c8-dc54-4ff8-8f17-9d7008a2e44b/Contacts/c7500d1a-7ff3-4099-bae3-8ecc45240a29

copy code

Remove all contacts from a contact group
    
    
    DELETE https://api.xero.com/api.xro/2.0/ContactGroups/b05466c8-dc54-4ff8-8f17-9d7008a2e44b/Contacts

copy code

## On this page

  * [Overview](/documentation/api/accounting/contactgroups/#overview)
  * [GET ContactGroups](/documentation/api/accounting/contactgroups/#get-contactgroups)
  * [POST ContactGroups](/documentation/api/accounting/contactgroups/#post-contactgroups)
  * [PUT ContactGroups](/documentation/api/accounting/contactgroups/#put-contactgroups)
  * [DELETE ContactGroups](/documentation/api/accounting/contactgroups/#delete-contactgroups)


