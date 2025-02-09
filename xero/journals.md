# Journals

[Try in API Explorer](https://api-explorer.xero.com/accounting/journals)

## Overview

[](/documentation/api/accounting/journals#overview)

Property| Description  
---|---  
URL| <https://api.xero.com/api.xro/2.0/Journals>  
Methods Supported| [GET](/documentation/api/accounting/journals#get-journals)  
Description| Allows you to retrieve any journals.   
See [Manual Journals](/documentation/api/accounting/manualjournals) if you need to create journals in Xero  
  
## GET Journals

[](/documentation/api/accounting/journals#get-journals)

Use this method to retrieve either one or many journals. A maximum of 100 journals will be returned in any response. Use the offset or If-Modified-Since filters (see below) with multiple API calls to retrieve larger sets of journals. Journals are ordered oldest to newest.

Response elements returned for GET Journals:

Field| Description  
---|---  
JournalID| Xero identifier (unique within organisations)  
JournalDate| Date the journal was posted  
JournalNumber| Xero generated journal number  
CreatedDateUTC| Created date UTC format  
Reference|   
SourceID| The identifier for the source transaction (e.g. InvoiceID). Note: not returned when calling an individual journal by JournalID or JournalNumber.  
SourceType| The journal source type. The type of transaction that created the journal. Note: not returned when calling an individual journal by JournalID or JournalNumber.  
JournalLines| See JournalLines)  
  
Elements for Journal Lines

Field| Description  
---|---  
JournalLineID| Xero identifier  
AccountID| See [Accounts](/documentation/api/accounting/accounts)  
AccountCode| See [Accounts](/documentation/api/accounting/accounts)  
AccountType| See [Account Types](/documentation/api/accounting/types#account-types)  
AccountName| See AccountCodes  
Description| The description from the source transaction line item. Only returned if populated.  
NetAmount| Net amount of journal line. This will be a positive value for a debit and negative for a credit  
GrossAmount| Gross amount of journal line (NetAmount + TaxAmount).  
TaxAmount| Total tax on a journal line  
TaxType| see [TaxTypes](/documentation/api/accounting/types#tax-types)  
TaxName| see [TaxRates](/documentation/api/accounting/taxrates)  
TrackingCategories| see [Tracking](/documentation/api/accounting/trackingcategories)  
  
### Optional parameters

Field| Description  
---|---  
Record filter| You can specify an individual journal by appending the value to the endpoint, i.e.   
`GET https://.../Journals/{identifier}`   
**JournalID** – The Xero identifier for an Journal   
e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9   
**JournalNumber** – The JournalNumber   
e.g. 100  
Modified After| The ModifiedAfter filter is actually an HTTP header: ' **If-Modified-Since** '.   
A UTC timestamp (yyyy-MM-ddTHH:mm:ss). Only journals created or modified since this timestamp will be returned e.g. 2009-11-12T00:00:00  
offset| Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned.  
paymentsOnly| Set to true if you want to retrieve journals on a cash basis. Journals are returned on an accrual basis by default.  
  
An example response for GET Journals
    
    
    GET https://api.xero.com/api.xro/2.0/Journals

copy code
    
    
    {
      "Journals": [
        {
          "JournalID": "23ff0b88-a141-4770-8537-0dd505873b1e",
          "JournalDate": "\/Date(1475625600000+0000)\/",
          "JournalNumber": 281,
          "CreatedDateUTC": "\/Date(1510091180510+0000)\/",
          "JournalLines": [
            {
              "JournalLineID": "2e38d2d7-d2e4-4894-89e4-bb25737cb677",
              "AccountID": "dd517756-1b24-4db3-8aee-51d331039012",
              "AccountCode": "255",
              "AccountType": "CURRLIAB",
              "AccountName": "Historical Adjustment",
              "Description": "",
              "NetAmount": -4130.98,
              "GrossAmount": -4130.98,
              "TaxAmount": 0.00,
              "TaxType": "NONE",
              "TaxName": "Tax Exempt",
              "TrackingCategories": []
            },
            {
              "JournalLineID": "7be9db36-3598-4755-ba5c-c2dbc8c4a7a2",
              "AccountID": "ceef66a5-a545-413b-9312-78a53caadbc4",
              "AccountCode": "090",
              "AccountType": "BANK",
              "AccountName": "Checking Account",
              "Description": "",
              "NetAmount": 4130.98,
              "GrossAmount": 4130.98,
              "TaxAmount": 0.00,
              "TaxType": "NONE",
              "TaxName": "Tax Exempt",
              "TrackingCategories": []
            }
          ]
        }
      ...
      ]
    }
    

copy code

### High volume threshold limit

In order to make our platform more stable, we've added a high volume threshold limit for the GET Journals Endpoint.

The maximum journals being returned will be 100.

## On this page

  * [Overview](/documentation/api/accounting/journals/#overview)
  * [GET Journals](/documentation/api/accounting/journals/#get-journals)


