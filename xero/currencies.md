# Currencies

[Try in API Explorer](https://api-explorer.xero.com/accounting/currencies)

## Overview

[](/documentation/api/accounting/currencies#overview)

|   
---|---  
URL| <https://api.xero.com/api.xro/2.0/Currencies>  
Methods Supported| [GET](/documentation/api/accounting/currencies#get-currencies), [PUT](/documentation/api/accounting/currencies#put-currencies)  
Description| Retrieve currencies for your organisation   
Add currencies to your organisation  
  
## GET Currencies

[](/documentation/api/accounting/currencies#get-currencies)

The following elements are returned in a response for Currencies

|   
---|---  
Code| 3 letter alpha code for the currency – see list of [currency codes](http://www.xe.com/iso4217.php)  
Description| Name of Currency  
  
### Optional parameters for GET Currencies

|   
---|---  
Where| Filter by an any element ( _see[Filters](/documentation/api/accounting/requests-and-responses#retrieving-modified-resources)_ )  
order| Order by any element returned ( _see[Order By](/documentation/api/accounting/requests-and-responses#http-get)_ )  
  
Example response for GET Currencies
    
    
    GET https://api.xero.com/api.xro/2.0/Currencies

copy code
    
    
    {
      "Currencies": [
        {
          "Code": "NZD",
          "Description": "New Zealand Dollar"
        }
      ...
      ]
    }
    
    

copy code

## PUT Currencies

[](/documentation/api/accounting/currencies#put-currencies)

The following elements can be used when adding Currencies. It is not possible to remove currencies from an organisation once they've been added.

|   
---|---  
Code| 3 letter alpha code for the currency – see list of [currency codes](http://www.xe.com/iso4217.php)  
  
Example response for PUT Currencies
    
    
    PUT https://api.xero.com/api.xro/2.0/Currencies

copy code
    
    
    {
      "Currencies": [
        {
          "Code": "SGD",
          "Description": "Singapore Dollar"
        }
      ...
      ]
    }
    
    

copy code

## On this page

  * [Overview](/documentation/api/accounting/currencies/#overview)
  * [GET Currencies](/documentation/api/accounting/currencies/#get-currencies)
  * [PUT Currencies](/documentation/api/accounting/currencies/#put-currencies)


