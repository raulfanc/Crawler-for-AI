# Accounts

[Try in API Explorer](https://api-explorer.xero.com/accounting/accounts)

## Overview

[](/documentation/api/accounting/accounts#overview)

Property| Description  
---|---  
**URL**| <https://api.xero.com/api.xro/2.0/Accounts>  
**Methods Supported**| [GET](/documentation/api/accounting/accounts#get-accounts), [PUT](/documentation/api/accounting/accounts#put-accounts), [POST](/documentation/api/accounting/accounts#post-accounts), [DELETE](/documentation/api/accounting/accounts#delete-accounts)  
**Description**|  Allows you to create individual accounts in a Xero organisation   
Allows you to retrieve the full chart of accounts   
Allows you to attach files to an account   
Allows you to archive an account   
Allows you to update details on an account   
Allows you to delete an account  
  
## GET Accounts

[](/documentation/api/accounting/accounts#get-accounts)

The following elements are returned in the Accounts response

Field| Description  
---|---  
**Code**|  Customer defined alpha numeric account code e.g 200 or SALES  
**Name**|  Name of account  
**Type**|  See [Account Types](/documentation/api/accounting/types#accounts)  
**BankAccountNumber****|  For bank accounts only (Account Type BANK)  
**Status****|  Accounts with a status of ACTIVE can be updated to ARCHIVED. See [Account Status Codes](/documentation/api/accounting/types#accounts)  
**Description****|  Description of the Account. Valid for all types of accounts except bank accounts  
**BankAccountType****|  For bank accounts only. See [Bank Account types](/documentation/api/accounting/types#accounts)  
**CurrencyCode****|  For bank accounts only  
**TaxType****|  See [Tax Types](/documentation/api/accounting/types#tax-rates)  
**EnablePaymentsToAccount****|  Boolean – describes whether account can have payments applied to it  
**ShowInExpenseClaims****|  Boolean – describes whether account code is available for use with expense claims  
**AccountID**|  Xero identifier (unique within organisations)  
**Class**|  See [Account Class Types](/documentation/api/accounting/types#accounts)  
**SystemAccount**|  If this is a system account then this element is returned. See [System Account types](/documentation/api/accounting/types#accounts). Note that non-system accounts may have this element set as either "" or null.  
**ReportingCode**|  Shown if set  
**ReportingCodeName**|  Shown if set  
**HasAttachments**|  boolean to indicate if an account has an attachment  
**UpdatedDateUTC**|  Last modified date UTC format  
**AddToWatchlist**|  Boolean that determines if this account is shown in the Xero dashboard watchlist widget  
  
### Optional parameters for GET Accounts

Field| Description  
---|---  
**AccountID**|  The Xero identifier for an account – specified as a string following the endpoint name e.g. **/297c2dc5-cc47-4afd-8ec8-74990b8761e9**  
**Modified After**|  The ModifiedAfter filter is actually an HTTP header: '**If-Modified-Since** '. A UTC timestamp (yyyy-mm-ddThh:mm:ss) . Only accounts created or modified since this timestamp will be returned e.g. 2009-11-12T00:00:00  
**Where**|  Filter by an any element (see [Filters](/documentation/api/accounting/requests-and-responses#http-get) )  
**order**|  Order by any element returned (see [Order By](/documentation/api/accounting/requests-and-responses#http-get) )  
  
Example response for GET Accounts
    
    
    GET https://api.xero.com/api.xro/2.0/Accounts

copy code
    
    
    {
      "Accounts": [{
        "AccountID": "ebd06280-af70-4bed-97c6-7451a454ad85",
        "Code": "091",
        "Name": "Business Savings Account",
        "Type": "BANK",
        "TaxType": "NONE",
        "EnablePaymentsToAccount": false,
        "BankAccountNumber": "0209087654321050",
        "BankAccountType": "BANK",
        "CurrencyCode": "NZD"
      },{
        "AccountID": "7d05a53d-613d-4eb2-a2fc-dcb6adb80b80",
        "Code": "200",
        "Name": "Sales",
        "Type": "REVENUE",
        "TaxType": "OUTPUT2",
        "Description": "Income from any normal business activity",
        "EnablePaymentsToAccount": false
      }]
    }
    
    

copy code

Example response for an individual Account
    
    
    GET https://api.xero.com/api.xro/2.0/Accounts/297c2dc5-cc47-4afd-8ec8-74990b8761e9

copy code
    
    
    {
      "Accounts": [{
        "AccountID": "297c2dc5-cc47-4afd-8ec8-74990b8761e9",
        "Code": "300",
        "Name": "Purchases",
        "Type": "DIRECTCOSTS",
        "TaxType": "INPUT2",
        "Description": "Goods purchased with the intention of selling these to customers",
        "EnablePaymentsToAccount": false
      }]
    }
    
    

copy code

## PUT Accounts

[](/documentation/api/accounting/accounts#put-accounts)

Use this method to create new accounts

Limitations

  * You can only add accounts one at a time (i.e. you'll need to do multiple API calls to add many accounts)
  * Replacing the entire chart of accounts is not currently supported. See our guide for [conversion partners](/documentation/guides/how-to-guides/conversions).
  * Creating Paypal accounts is not currently supported



The following elements are **required** for creates and optional for updates

Field| Description  
---|---  
**Code**|  Customer defined alpha numeric account code e.g 200 or SALES (max length = 10)  
**Name**|  Name of account (max length = 150)  
**Type**|  See [Account Types](/documentation/api/accounting/types#accounts)  
**BankAccountNumber**|  For bank accounts only (Account Type BANK)  
  
The following elements are **optional** for creates and updates

Field| Description  
---|---  
**Status**|  Accounts with a status of ACTIVE can be updated to ARCHIVED. See [Account Status Codes](/documentation/api/accounting/types#accounts)  
**Description**|  Description of the Account. Valid for all types of accounts except bank accounts (max length = 4000)  
**BankAccountType**|  For bank accounts only. See [Bank Account types](/documentation/api/accounting/types#accounts)  
**CurrencyCode**|  For bank accounts only  
**TaxType**|  See [Tax Types](/documentation/api/accounting/types#tax-rates)  
**EnablePaymentsToAccount**|  Boolean – describes whether account can have payments applied to it  
**ShowInExpenseClaims**|  Boolean – describes whether account code is available for use with expense claims  
**AddToWatchlist**|  Boolean that determines if this account is shown in the Xero dashboard watchlist widget. Works only with POST and not PUT.  
  
Example of creating a new sales account with the minimum elements required
    
    
    PUT https://api.xero.com/api.xro/2.0/Accounts

copy code
    
    
    {
      "Code": "201",
      "Name": "Sales - clearance lines",
      "Type": "SALES"
    }
    
    

copy code

Below is an example of creating a new asset account with the minimum elements required
    
    
    PUT https://api.xero.com/api.xro/2.0/Accounts

copy code
    
    
    {
      "Code": "304",
      "Name": "Clearing - EFTPOS",
      "Type": "CURRENT"
    }
    
    

copy code

Below is an example of creating a new bank account with the minimum elements required. (Note the bank account below is an AU account.)
    
    
    PUT https://api.xero.com/api.xro/2.0/Accounts

copy code
    
    
    {
      "Name": "Cheque Account",
      "Type": "BANK",
      "BankAccountNumber": "121-121-1234567"
    }
    
    

copy code

### Uploading an Attachment

You can upload up to 10 attachments (each up to 25mb in size) per account, once the account has been created in Xero. To do this you'll need to know the ID of the account which you'll use to construct the URL when POST/PUTing a byte stream containing the attachment file. e.g. <https://api.xero.com/api.xro/2.0/Accounts/f0ec0d8c-6fce-4330-bb3b-8306278c6fd8/Attachments/image.png>. See the [Attachments](/documentation/api/accounting/attachments) page for more details.

Example of attaching a file to an account
    
    
    PUT https://api.xero.com/api.xro/2.0/Accounts/f0ec0d8c-6fce-4330-bb3b-8306278c6fd8/Attachments/image.png

copy code
    
    
    Headers:
    Authorization: Bearer...
    Content Type: image/png
    Content-Length: 10293
    Body:
    {RAW-IMAGE-CONTENT}
    
    

copy code

## POST Accounts

[](/documentation/api/accounting/accounts#post-accounts)

Use this method to update account details.

### Limitations

  * You can only update accounts one at a time (i.e. you’ll need to do multiple API calls to update many accounts)
  * You cannot update the status to archived (see below) when also updating other values



Example request for updating an Account
    
    
    POST https://api.xero.com/api.xro/2.0/Accounts/297c2dc5-cc47-4afd-8ec8-74990b8761e9

copy code
    
    
    {
      "AccountID": "297c2dc5-cc47-4afd-8ec8-74990b8761e9",
      "Code": "200",
      "Name": "Sales account",
      "Type": "REVENUE",
      "TaxType": "OUTPUT2",
      "Description": "Income from any normal business trading activity",
      "EnablePaymentsToAccount": "false",
      "ShowInExpenseClaims": "false"
    }
    
    

copy code

### Archive Accounts

Use the POST method and update the Status to ARCHIVED.

Example request for archiving an Account
    
    
    POST https://api.xero.com/api.xro/2.0/Accounts/297c2dc5-cc47-4afd-8ec8-74990b8761e9

copy code
    
    
    {
      "AccountID": "297c2dc5-cc47-4afd-8ec8-74990b8761e9",
      "Status": "ARCHIVED"
    }
    
    

copy code

## DELETE Accounts

[](/documentation/api/accounting/accounts#delete-accounts)

Non-system accounts and accounts not used on transactions can be deleted using the delete method. If an account is not able to be deleted you can [update](/documentation/api/accounting/accounts#post-accounts) the status to ARCHIVED

Example request for deleteing an Account
    
    
    DELETE https://api.xero.com/api.xro/2.0/Accounts/297c2dc5-cc47-4afd-8ec8-74990b8761e9

copy code

## On this page

  * [Overview](/documentation/api/accounting/accounts/#overview)
  * [GET Accounts](/documentation/api/accounting/accounts/#get-accounts)
  * [PUT Accounts](/documentation/api/accounting/accounts/#put-accounts)
  * [POST Accounts](/documentation/api/accounting/accounts/#post-accounts)
  * [DELETE Accounts](/documentation/api/accounting/accounts/#delete-accounts)


