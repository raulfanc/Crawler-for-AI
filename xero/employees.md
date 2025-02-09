# Employees

[Try in API Explorer](https://api-explorer.xero.com/accounting/employees)

This endpoint is used for an [employee type](https://help.xero.com/int/Contacts_EmployeeAdd) used exclusively by the global Payrun functionality in Xero core accounting. **This is NOT the endpoint to use for Xero's regional Payroll employee types.** Different endpoints are used for employees in the [Australian](/documentation/api/payrollau/overview/), [New Zealand](/documentation/api/payrollnz/overview) and [UK](/documentation/api/payrolluk/overview) Payroll APIs.

If you are trying to represent employees in Xero for the purposes of **allowing the payment of bills to employees** (i.e. reimbursing for expenses) please see the [contacts endpoint](/documentation/api/accounting/contacts) and use the "IsSupplier" flag to enable payment of bills to this contact. You can also create a [contact group](/documentation/api/accounting/contactgroups) called "employees" if you so choose.

## Overview

[](/documentation/api/accounting/employees#overview)

|   
---|---  
URL| <https://api.xero.com/api.xro/2.0/Employees>  
Methods Supported| [POST](/documentation/api/accounting/employees#post-employees), [PUT](/documentation/api/accounting/employees#put-employees), [GET](/documentation/api/accounting/employees#get-employees)  
Description| Allows you to retrieve, add and update employees used in Xero payrun functionality  
  
## GET Employees

[](/documentation/api/accounting/employees#get-employees)

User this method to retrieve one or many employees

|   
---|---  
EmployeeID| Xero identifier (unique within organisations)  
Status| Current status of an employee – see contact status types  
FirstName| First name of an employee  
LastName| Last name of an employee  
External Link| Link to an external resource, for example, an employee record in an external system. You can specify the URL element.   
The description of the link is auto-generated in the form `Go to <App name>`. `<App name>` refers to the [Xero application](https://api.xero.com/Application) name that is making the API call.  
  
### Optional parameters for GET Employees

|   
---|---  
Record filter| You can specify an individual record by appending the EmployeeID to the endpoint, i.e. `GET https://.../Employees/{EmployeeID}`  
Modified After| The ModifiedAfter filter is actually an HTTP header: `If-Modified-Since`. A UTC timestamp (yyyy-mm-ddThh:mm:ss) . Only employees created or modified since this timestamp will be returned e.g. `2009-11-12T00:00:00`  
Where| Filter by an any element ( _see[Filters](/documentation/api/accounting/requests-and-responses#retrieving-modified-resources)_ )  
order| Order by any element returned ( _see[Order By](/documentation/api/accounting/requests-and-responses/#retrieving-a-smaller-lightweight-response-using-the-summaryonly-parameter-of-results)_ )  
  
Example response for retrieving Employees
    
    
    GET https://api.xero.com/api.xro/2.0/Employees

copy code
    
    
    {
      "Employees": [
        {
          "EmployeeID": "6515d052-b3f7-4de4-b0a3-e4c12caba8b2",
          "Status": "ACTIVE",
          "FirstName": "Joey",
          "LastName": "Bloggs",
          "ExternalLink": {
            "Url": "http://twitter.com/#!/search/Joey+Bloggs",
            "Description": "Go to external link"
          },
          "UpdatedDateUTC": "\/Date(1519351730117+0000)\/"
        }
      ...
      ]
    }
    
    

copy code

## POST Employees

[](/documentation/api/accounting/employees#post-employees)

Use this method to create or update one or more employee records.

|   
---|---  
Status| Current status of an employee – see contact status types  
FirstName| First name of an employee (max length = 255)  
LastName| Last name of an employee (max length = 255)  
External Link| Link to an external resource, for example, an employee record in an external system. You can specify the URL element.   
The description of the link is auto-generated in the form `Go to <App name>`. `<App name>` refers to the [Xero application](https://api.xero.com/Application) name that is making the API call.  
  
When you are updating an employee you don’t need to specify every element. If you exclude an element then the existing value of that field will be preserved.

Example of minimum elements required to add a new employee
    
    
    POST https://api.xero.com/api.xro/2.0/Employees

copy code
    
    
    {
      "Employees": [
        {
          "FirstName": "Joey",
          "LastName": "Bloggs"
        }
      ]
    }
    
    

copy code

Example of the full set of elements you can specify for an employee
    
    
    POST https://api.xero.com/api.xro/2.0/Employees

copy code
    
    
    {
      "Employees": [
        {
          "FirstName": "Joey",
          "LastName": "Bloggs",
          "ExternalLink": {
            "Url": "http://twitter.com/#!/search/Joey+Bloggs"
          }
        }
      ]
    }
    
    

copy code

Example of minimum elements required to add many employees
    
    
    POST https://api.xero.com/api.xro/2.0/Employees

copy code
    
    
    {
      "Employees": [
        {
          "FirstName": "Joey",
          "LastName": "Bloggs"
        },
        {
          "FirstName": "Rachel",
          "LastName": "Redman"
        }
      ]
    }
    
    

copy code

## PUT Employees

[](/documentation/api/accounting/employees#put-employees)

Use this method to create one or more employee records. This method works very similar to POST Employees but if an existing employee matches your FirstName and LastName then you will receive an error.

## On this page

  * [Overview](/documentation/api/accounting/employees/#overview)
  * [GET Employees](/documentation/api/accounting/employees/#get-employees)
  * [POST Employees](/documentation/api/accounting/employees/#post-employees)
  * [PUT Employees](/documentation/api/accounting/employees/#put-employees)


