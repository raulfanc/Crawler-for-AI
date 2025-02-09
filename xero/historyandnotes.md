# History and Notes

## Overview

[](/documentation/api/accounting/historyandnotes#overview)

|   
---|---  
URL| [https://api.xero.com/api.xro/2.0/{Endpoint}/{Guid}/history](https://api.xero.com/api.xro/2.0/%7BEndpoint%7D/%7BGuid%7D/history)  
Methods Supported| [GET](/documentation/api/accounting/historyandnotes#get-history), [PUT](/documentation/api/accounting/historyandnotes#put-history), [POST](/documentation/api/accounting/historyandnotes#post-history)  
Description| Allows you to retrieve the history of changes to a single existing document   
Allows you add notes against a single existing document ([See supported document types](/documentation/api/accounting/historyandnotes#supported-document-types-for-adding-notes-and-retrieving-history))  
  
## GET History

[](/documentation/api/accounting/historyandnotes#get-history)

Response elements returned for GET History:

|   
---|---  
Changes| The type of change recorded against the document. See [here for a full list of possible changes](https://help.xero.com/Payments_HistoryNotes)  
DateUTC| UTC date that the history record was created  
User| The user responsible for the change ("System Generated" when the change happens via API)  
Details| Description of the change event or transaction  
  
Example response retrieving History
    
    
    GET https://api.xero.com/api.xro/2.0/{Endpoint}/{Guid}/history

copy code
    
    
    {
      "HistoryRecords": [
         {
          "Changes": "Approved",
          "DateUTCString": "2018-02-28T21:02:11",
          "DateUTC": "\/Date(1519851731990+0000)\/",
          "User": "System Generated",
          "Details": "Received through the Xero API from ABC Org"
        },
        {
          "Changes": "Edited",
          "DateUTCString": "2018-02-28T21:01:29",
          "DateUTC": "\/Date(1519851689297+0000)\/",
          "User": "Mac Haag",
          "Details": "INV-0041 to ABC Furniture for 100.00."
        }
        ...
      ]
    }
    
    

copy code

## PUT History

[](/documentation/api/accounting/historyandnotes#put-history)

Use this method to add notes to a document. Notes are the only type of Change that can be manually created. All other types of Change are created automatically when certain actions occur (e.g. an invoice is paid).

The note will be displayed in history & notes showing the date of creation and "System Generated" as the user that created it.

The following elements are used in a PUT request:

|   
---|---  
Details| The note to be recorded against a single document. Max Length 2500 characters.  
  
Example request to add notes
    
    
    PUT https://api.xero.com/api.xro/2.0/{Endpoint}/{Guid}/history

copy code
    
    
    {
      "HistoryRecords": [
        {
          "Details": "Previous payment failed"
        },
        {
          "Details": "Defer the payment"
        }
        ...
      ]
    }
    
    

copy code

## POST History

[](/documentation/api/accounting/historyandnotes#post-history)

In this case a POST is exactly the same as a PUT. It's not possible to update history and notes.

## Supported document types for adding notes and retrieving History

[](/documentation/api/accounting/historyandnotes#supported-document-types-for-adding-notes-and-retrieving-history)

  * BankTransactions
  * BatchPayments
  * BankTransfers (this can be accessed via the BankTransactions endpoint)
  * Contacts
  * Creditnotes
  * Invoices
  * Items
  * ManualJournals
  * Overpayments
  * Payments
  * Prepayments
  * Purchase Orders
  * Repeating Invoices
  * Quotes



## On this page

  * [Overview](/documentation/api/accounting/historyandnotes/#overview)
  * [GET History](/documentation/api/accounting/historyandnotes/#get-history)
  * [PUT History](/documentation/api/accounting/historyandnotes/#put-history)
  * [POST History](/documentation/api/accounting/historyandnotes/#post-history)
  * [Supported document types for adding notes and retrieving History](/documentation/api/accounting/historyandnotes/#supported-document-types-for-adding-notes-and-retrieving-history)


