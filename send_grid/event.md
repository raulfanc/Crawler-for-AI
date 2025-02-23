Skip to contentSkip to navigationSkip to topbar

[Go to the Twilio SendGrid Docs home page](/docs/sendgrid)

Twilio SendGrid Docs

[Twilio SendGrid LogoTwilio SendGrid Docs](/docs)

Search```K`

Search```K`

Search```K`

On this page

# Event Webhook Reference

Positive FeedbackNegative Feedback

* * *

* * *

## Security Features

security-features page anchor

Positive FeedbackNegative Feedback

We recommend securing the Event Webhook data using our Signed Event Webhook, OAuth 2.0, or both. For more information about Event Webhook security, see [**Getting Started with the Event Webhook Security Features**](/docs/sendgrid/for-developers/tracking-events/getting-started-event-webhook-security-features).

Security features are not required for setup, but they are highly recommended for any use of the Event Webhook beyond initial testing.

(warning)

## Warning

Categories and Unique Arguments will be stored as a "Not PII" field and may be used for counting or other operations as SendGrid runs its systems. These fields generally cannot be redacted or removed. You should take care not to place PII in this field. SendGrid does not treat this data as PII, and its value may be visible to SendGrid employees, stored long-term, and may continue to be stored after you have left SendGrid's platform.

* * *

## Events

events page anchor

Positive FeedbackNegative Feedback

Events are generated when email is processed by SendGrid and email service providers. There are three types of events - delivery, engagement and account events. Delivery events indicate the status of email delivery to the recipient. Engagement events indicate how the recipient is interacting with the email. Account events indicate changes and impacts to your account.

Here is an event response that includes an example of each type of event:

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "email": "example@test.com",
    
    
    4
    
        "timestamp": 1513299569,
    
    
    5
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    6
    
        "event": "processed",
    
    
    7
    
        "category": "cat facts",
    
    
    8
    
        "sg_event_id": "sg_event_id",
    
    
    9
    
        "sg_message_id": "sg_message_id"
    
    
    10
    
      },
    
    
    11
    
      {
    
    
    12
    
        "email": "example@test.com",
    
    
    13
    
        "timestamp": 1513299569,
    
    
    14
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    15
    
        "event": "deferred",
    
    
    16
    
        "ip": "168.1.1.1",
    
    
    17
    
        "category": "cat facts",
    
    
    18
    
        "sg_event_id": "sg_event_id",
    
    
    19
    
        "sg_message_id": "sg_message_id",
    
    
    20
    
        "response": "400 try again later",
    
    
    21
    
        "attempt": "5"
    
    
    22
    
      },
    
    
    23
    
      {
    
    
    24
    
        "email": "example@test.com",
    
    
    25
    
        "timestamp": 1513299569,
    
    
    26
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    27
    
        "event": "delivered",
    
    
    28
    
        "ip": "168.1.1.1",
    
    
    29
    
        "category": "cat facts",
    
    
    30
    
        "sg_event_id": "sg_event_id",
    
    
    31
    
        "sg_message_id": "sg_message_id",
    
    
    32
    
        "response": "250 OK"
    
    
    33
    
      },
    
    
    34
    
      {
    
    
    35
    
        "email": "example@test.com",
    
    
    36
    
        "timestamp": 1513299569,
    
    
    37
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    38
    
        "event": "open",
    
    
    39
    
        "sg_machine_open": false,
    
    
    40
    
        "category": "cat facts",
    
    
    41
    
        "sg_event_id": "sg_event_id",
    
    
    42
    
        "sg_message_id": "sg_message_id",
    
    
    43
    
        "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    
    
    44
    
        "ip": "255.255.255.255"
    
    
    45
    
      },
    
    
    46
    
      {
    
    
    47
    
        "email": "example@test.com",
    
    
    48
    
        "timestamp": 1513299569,
    
    
    49
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    50
    
        "event": "click",
    
    
    51
    
        "category": "cat facts",
    
    
    52
    
        "sg_event_id": "sg_event_id",
    
    
    53
    
        "sg_message_id": "sg_message_id",
    
    
    54
    
        "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    
    
    55
    
        "ip": "255.255.255.255",
    
    
    56
    
        "url": "http://www.sendgrid.com/"
    
    
    57
    
      },
    
    
    58
    
      {
    
    
    59
    
        "email": "example@test.com",
    
    
    60
    
        "timestamp": 1513299569,
    
    
    61
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    62
    
        "bounce_classification": "Invalid Address",
    
    
    63
    
        "event": "bounce",
    
    
    64
    
        "ip": "168.1.1.1",
    
    
    65
    
        "category": "cat facts",
    
    
    66
    
        "sg_event_id": "sg_event_id",
    
    
    67
    
        "sg_message_id": "sg_message_id",
    
    
    68
    
        "reason": "500 unknown recipient",
    
    
    69
    
        "status": "5.0.0"
    
    
    70
    
      },
    
    
    71
    
      {
    
    
    72
    
        "email": "example@test.com",
    
    
    73
    
        "timestamp": 1513299569,
    
    
    74
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    75
    
        "event": "dropped",
    
    
    76
    
        "category": "cat facts",
    
    
    77
    
        "sg_event_id": "sg_event_id",
    
    
    78
    
        "sg_message_id": "sg_message_id",
    
    
    79
    
        "reason": "Bounced Address",
    
    
    80
    
        "status": "5.0.0"
    
    
    81
    
      },
    
    
    82
    
      {
    
    
    83
    
        "email": "example@test.com",
    
    
    84
    
        "timestamp": 1513299569,
    
    
    85
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    86
    
        "event": "spamreport",
    
    
    87
    
        "sg_event_id": "sg_event_id",
    
    
    88
    
        "sg_message_id": "sg_message_id"
    
    
    89
    
      },
    
    
    90
    
      {
    
    
    91
    
        "email": "example@test.com",
    
    
    92
    
        "timestamp": 1513299569,
    
    
    93
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    94
    
        "event": "unsubscribe",
    
    
    95
    
        "category": "cat facts",
    
    
    96
    
        "sg_event_id": "sg_event_id",
    
    
    97
    
        "sg_message_id": "sg_message_id"
    
    
    98
    
      },
    
    
    99
    
      {
    
    
    100
    
        "email": "example@test.com",
    
    
    101
    
        "timestamp": 1513299569,
    
    
    102
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    103
    
        "event": "group_unsubscribe",
    
    
    104
    
        "category": "cat facts",
    
    
    105
    
        "sg_event_id": "sg_event_id",
    
    
    106
    
        "sg_message_id": "sg_message_id",
    
    
    107
    
        "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    
    
    108
    
        "ip": "255.255.255.255",
    
    
    109
    
        "url": "http://www.sendgrid.com/",
    
    
    110
    
        "asm_group_id": 10
    
    
    111
    
      },
    
    
    112
    
      {
    
    
    113
    
        "email": "example@test.com",
    
    
    114
    
        "timestamp": 1513299569,
    
    
    115
    
        "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    116
    
        "event": "group_resubscribe",
    
    
    117
    
        "category": "cat facts",
    
    
    118
    
        "sg_event_id": "sg_event_id",
    
    
    119
    
        "sg_message_id": "sg_message_id",
    
    
    120
    
        "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    
    
    121
    
        "ip": "000.000.000.000",
    
    
    122
    
        "url": "http://www.sendgrid.com/",
    
    
    123
    
        "asm_group_id": 10
    
    
    124
    
      },
    
    
    125
    
      {
    
    
    126
    
       "event":"account_status_change", 
    
    
    127
    
       "sg_event_id":"MjEzNTg5OTcyOC10ZXJtaW5hdGUtMTcwNzg1MTUzMQ",
    
    
    128
    
       "timestamp":1709142428,
    
    
    129
    
       "type":"compliance_suspend"
    
    
    130
    
      }
    
    
    131
    
    ]

### Delivery events

delivery-events page anchor

Positive FeedbackNegative Feedback

Delivery events include processed, dropped, delivered, deferred, and bounce.

#### Processed

processed page anchor

Message has been received and is ready to be delivered.

##### Example webhook response

example-webhook-response page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "pool": {
    
    
    6
    
                "name": "new_MY_test",
    
    
    7
    
                "id": 210
    
    
    8
    
          },
    
    
    9
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    10
    
          "event": "processed",
    
    
    11
    
          "category": "cat facts",
    
    
    12
    
          "sg_event_id": "rbtnWrG1DVDGGGFHFyun0A==",
    
    
    13
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.000000000000000000000"
    
    
    14
    
      }
    
    
    15
    
    ]

#### Dropped

dropped page anchor

You may see the following drop reasons: Invalid SMTPAPI header, Spam Content (if Spam Checker app is enabled), Unsubscribed Address, Bounced Address, Spam Reporting Address, Invalid Address, Recipient List over Package Quota

##### Example webhook response

example-webhook-response-2 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    6
    
          "event": "dropped",
    
    
    7
    
          "category": "cat facts",
    
    
    8
    
          "sg_event_id": "zmzJhfJgAfUSOW80yEbPyw==",
    
    
    9
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    10
    
          "reason": "Bounced Address",
    
    
    11
    
          "status": "5.0.0"
    
    
    12
    
      }
    
    
    13
    
    ]

#### Delivered

delivered page anchor

Message has been successfully delivered to the receiving server.

##### Example webhook response

example-webhook-response-3 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    6
    
          "event": "delivered",
    
    
    7
    
          "category": "cat facts",
    
    
    8
    
          "sg_event_id": "rWVYmVk90MjZJ9iohOBa3w==",
    
    
    9
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    10
    
          "response": "250 OK"
    
    
    11
    
       }
    
    
    12
    
    ]

#### Deferred

deferred page anchor

Receiving server temporarily rejected the message.

##### Example webhook response

example-webhook-response-4 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@example.com",
    
    
    4
    
          "domain": "example.com",
    
    
    5
    
          "from": "test@test.com",
    
    
    6
    
          "timestamp": 1513299569,
    
    
    7
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    8
    
          "event": "deferred",
    
    
    9
    
          "category": "cat facts",
    
    
    10
    
          "sg_event_id": "t7LEShmowp86DTdUW8M-GQ==",
    
    
    11
    
          "sg_message_id": " 14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    12
    
          "response": "400 try again later",
    
    
    13
    
          "attempt": "5"
    
    
    14
    
       }
    
    
    15
    
    ]

#### Bounce

bounce page anchor

Receiving server could not or would not accept mail to this recipient permanently. If a recipient has previously unsubscribed from your emails, the message is dropped.

##### Example webhook response

example-webhook-response-5 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    6
    
          "bounce_classification": "Invalid Address",
    
    
    7
    
          "event": "bounce",
    
    
    8
    
          "category": "cat facts",
    
    
    9
    
          "sg_event_id": "6g4ZI7SA-xmRDv57GoPIPw==",
    
    
    10
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    11
    
          "reason": "500 unknown recipient",
    
    
    12
    
          "status": "5.0.0",
    
    
    13
    
          "type": "bounce"
    
    
    14
    
       }
    
    
    15
    
    ]

#### Blocked

blocked page anchor

Receiving server could not or would not accept the message temporarily. If a recipient has previously unsubscribed from your emails, the message is dropped.

##### Example webhook response

example-webhook-response-6 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    6
    
          "bounce_classification": "Invalid Address",
    
    
    7
    
          "event": "bounce",
    
    
    8
    
          "category": "cat facts",
    
    
    9
    
          "sg_event_id": "6g4ZI7SA-xmRDv57GoPIPw==",
    
    
    10
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    11
    
          "reason": "500 unknown recipient",
    
    
    12
    
          "status": "5.0.0",
    
    
    13
    
          "type": "blocked"
    
    
    14
    
       }
    
    
    15
    
    ]

NOTE: bounce_classification can have the following values: Content, Frequency or Volume Too High, Invalid Address, Mailbox Unavailable, Reputation, Technical Failure, Unclassified. Please see [this reference](/docs/sendgrid/ui/analytics-and-reporting/bounce-and-block-classifications "this reference") for more information on each of these.

### Engagement events

engagement-events page anchor

Positive FeedbackNegative Feedback

Engagement events include open, click, spam report, unsubscribe, group unsubscribe, and group resubscribe.

#### Open

open page anchor

Recipient has opened the HTML message. Open Tracking needs to be enabled for this type of event.

##### Example webhook response

example-webhook-response-7 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "event": "open",
    
    
    6
    
          "sg_machine_open": false,
    
    
    7
    
          "category": "cat facts",
    
    
    8
    
          "sg_event_id": "FOTFFO0ecsBE-zxFXfs6WA==",
    
    
    9
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    10
    
          "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    
    
    11
    
          "ip": "255.255.255.255"
    
    
    12
    
       }
    
    
    13
    
    ]

#### Click

click page anchor

Recipient clicked on a link within the message. Click Tracking needs to be enabled for this type of event.

##### Example webhook response

example-webhook-response-8 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "event": "click",
    
    
    6
    
          "category": "cat facts",
    
    
    7
    
          "sg_event_id": "kCAi1KttyQdEKHhdC-nuEA==",
    
    
    8
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    9
    
          "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    
    
    10
    
          "ip": "255.255.255.255",
    
    
    11
    
          "url": "http://www.sendgrid.com/"
    
    
    12
    
       }
    
    
    13
    
    ]

#### Spam Report

spam-report page anchor

Recipient marked message as spam.

##### Example webhook response

example-webhook-response-9 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    6
    
          "event": "spamreport",
    
    
    7
    
          "sg_event_id": "37nvH5QBz858KGVYCM4uOA==",
    
    
    8
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0"
    
    
    9
    
       }
    
    
    10
    
    ]

#### Unsubscribe

unsubscribe page anchor

Recipient clicked on the 'Opt Out of All Emails' link (available after clicking the message's subscription management link). Subscription Tracking needs to be enabled for this type of event.

##### Example webhook response

example-webhook-response-10 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "event": "unsubscribe",
    
    
    6
    
          "category": "cat facts",
    
    
    7
    
          "sg_event_id": "zz_BjPgU_5pS-J8vlfB1sg==",
    
    
    8
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0"
    
    
    9
    
       }
    
    
    10
    
    ]

#### Group Unsubscribe

group-unsubscribe page anchor

Recipient unsubscribed from a specific group either by clicking the link directly or updating their preferences. Subscription Tracking needs to be enabled for this type of event.

##### Example webhook response

example-webhook-response-11 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    6
    
          "event": "group_unsubscribe",
    
    
    7
    
          "category": "cat facts",
    
    
    8
    
          "sg_event_id": "ahSCB7xYcXFb-hEaawsPRw==",
    
    
    9
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    10
    
          "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    
    
    11
    
          "ip": "255.255.255.255",
    
    
    12
    
          "url": "http://www.sendgrid.com/",
    
    
    13
    
          "asm_group_id": 10
    
    
    14
    
       }
    
    
    15
    
    ]

#### Group Resubscribe

group-resubscribe page anchor

Recipient resubscribed to a specific group by updating their preferences. Subscription Tracking needs to be enabled for this type of event.

##### Example webhook response

example-webhook-response-12 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "email": "example@test.com",
    
    
    4
    
          "timestamp": 1513299569,
    
    
    5
    
          "smtp-id": "<14c5d75ce93.dfd.64b469@ismtpd-555>",
    
    
    6
    
          "event": "group_resubscribe",
    
    
    7
    
          "category": "cat facts",
    
    
    8
    
          "sg_event_id": "w_u0vJhLT-OFfprar5N93g==",
    
    
    9
    
          "sg_message_id": "14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
    
    
    10
    
          "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    
    
    11
    
          "ip": "255.255.255.255",
    
    
    12
    
          "url": "http://www.sendgrid.com/",
    
    
    13
    
          "asm_group_id": 10
    
    
    14
    
       }
    
    
    15
    
    ]

#### Account Status Change

account-status-change page anchor

Your account status changed because of issues related to compliance with SendGrid's terms of service. This can happen when SendGrid identifies abnormal activity such as phishing, elevated spam rates or other potentially bad behavior. For more information on account statuses and what to do, refer to SendGrid's [Account Under Review documentation](/docs/sendgrid/ui/account-and-settings/account-under-review "Account Under Review documentation")

##### Example webhook response

example-webhook-response-13 page anchor

Copy code block
    
    
    1
    
    [
    
    
    2
    
       {
    
    
    3
    
          "event":"account_status_change", 
    
    
    4
    
          "sg_event_id":"MjEzNTg5OTcyOC10ZXJtaW5hdGUtMTcwNzg1MTUzMQ",
    
    
    5
    
          "timestamp":1709142428,
    
    
    6
    
          "type":"compliance_suspend"
    
    
    7
    
       }
    
    
    8
    
    ]

(warning)

## Warning

Events such as **deferrals** and **bounces** may or may not have an IP included in their post. For example, an internal deferral occurs when we have already determined an issue at a specific MX record and are waiting for that issue to clear before trying to deliver more mail. Because no action is taken during an internal deferral, no IP can be logged taking an action. A delayed bounce occurs when mail is initially accepted for delivery but then rejected after the SMTP conversation is over. Because the SMTP conversation is no longer happening, a new conversation is started where much of the previous context is lost. This results in delayed bounces not having an IP and other information.

In the following table, IP is not included as part of the json return for a deferral or bounce.

* * *

## Event objects

event-objects page anchor

Positive FeedbackNegative Feedback

For a definition of each JSON object, please see the [list](/docs/sendgrid/for-developers/tracking-events/event#json-objects "list") below this table.

| [Processed](/docs/sendgrid/for-developers/tracking-events/event#processed "Processed")| [Dropped](/docs/sendgrid/for-developers/tracking-events/event#dropped "Dropped")| [Delivered](/docs/sendgrid/for-developers/tracking-events/event#delivered "Delivered")| [Deferred](/docs/sendgrid/for-developers/tracking-events/event#deferred "Deferred")| [Bounce](/docs/sendgrid/for-developers/tracking-events/event#bounce "Bounce")| [Opened](/docs/sendgrid/for-developers/tracking-events/event#open "Opened")| [Clicked](/docs/sendgrid/for-developers/tracking-events/event#click "Clicked")| [Spam Report](/docs/sendgrid/for-developers/tracking-events/event#spam-report "Spam Report")| [Unsubscribe](/docs/sendgrid/for-developers/tracking-events/event#unsubscribe "Unsubscribe")| [Group Unsubscribe](/docs/sendgrid/for-developers/tracking-events/event#group-unsubscribe "Group Unsubscribe")| [Group Resubscribe](/docs/sendgrid/for-developers/tracking-events/event#group-resubscribe "Group Resubscribe")| [Account Status Change](/docs/sendgrid/for-developers/tracking-events/event#account-status-change "Account Status Change")  
---|---|---|---|---|---|---|---|---|---|---|---|---  
email| X| X| X| X| X| X| X| X| X| X| X|   
timestamp| X| X| X| X| X| X| X| X| X| X| X| X  
event| X| X| X| X| X| X| X| X| X| X| X| X  
smtp-id| X| X| X| X| X| | | | | | |   
useragent| | | | | | X| X| | | X| X|   
ip| | | X| | | X| X| | | X| X|   
sg_event_id| X| X| X| X| X| X| X| X| X| X| X| X  
sg_message_id| X| X| X| X| X*| X| X| X| X| X| X|   
reason| | X| | X| X| | | | | | |   
status| | | | | X| | | | | | |   
response| | | X| | | | | | | | |   
tls| | | X| | X| | | | | | |   
url| | | | | | | X| | | | |   
category| X| X| X| X| X| X| X| X| X| | |   
asm_group_id| X| X| X| X| X| X| X| | | X| X|   
unique_args| X| X| X| X| X| X| X| X| X| X| X|   
marketing_campaign_id| X| X| X| X| X| X| X| X| X| X| X|   
marketing_campaign_name| X| X| X| X| X| X| X| X| X| X| X|   
attempt| | | | X| | | | | | | |   
pool| X| | | | | | | | | | |   
sg_machine_open| | | | | | X| | | | | |   
bounce_classification| | | | | X| | | | | | |   
type| | | | | | | | | | | | X  
  
* In the case of a delayed or [asynchronous bounce](/docs/sendgrid/ui/sending-email/bounces#asynchronous-bounces "asynchronous bounce"), the message ID will be unavailable.

### JSON objects

json-objects page anchor

Positive FeedbackNegative Feedback

  * `email` \- the email address of the recipient
  * `timestamp` \- the [UNIX timestamp(link takes you to an external page)](https://en.wikipedia.org/wiki/Unix_time "UNIX timestamp") of the exact time the associated event occurred.
  * `event` \- the event type. Possible values are processed, dropped, delivered, deferred, bounce, open, click, spam report, unsubscribe, group unsubscribe, and group resubscribe.
  * `smtp-id` \- a unique ID attached to the message by the originating system.
  * `useragent` \- the user agent responsible for the event. This is usually a web browser. For example, "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36".
  * `ip` \- the IP address used to send the email. For `open` and `click` events, it is the IP address of the recipient who engaged with the email. The IP address will not be available in the response json for certain events such as `deferral` and `bounce`.
  * `sg_event_id` \- a unique ID to this event that you can use for deduplication purposes. These IDs are up to 100 characters long and are URL safe.
  * `sg_message_id` \- a unique, internal SendGrid ID for the message. The first half of this ID is pulled from the `smtp-id`. The message ID will be included in most cases. In the event of an [asynchronous bounce](/docs/sendgrid/ui/sending-email/bounces#asynchronous-bounces "asynchronous bounce"),, the message ID will not be available. An asynchronous bounce occurs when a message is first accepted by the receiving mail server and then bounced at a later time. When this happens, there is less information available about the bounce.
  * `reason` \- any sort of error response returned by the receiving server that describes the reason this event type was triggered.
  * `status` \- status code string. Corresponds to HTTP status code - for example, a JSON response of 5.0.0 is the same as a 500 error response.
  * `response` \- the full text of the HTTP response error returned from the receiving server.
  * `tls` \- indicates whether TLS encryption was used in sending this message. For more information about TLS, see the [TLS Glossary page](/docs/sendgrid/glossary/tls "TLS Glossary page").
  * `url` \- the URL where the event originates. For click events, this is the URL clicked on by the recipient.
  * `url_offset` \- Indicates the location of a link in the email's HTML code. Indices are set starting from top to bottom in the HTML, meaning the first link read from top to bottom will be at index 0. The `url_offset` is provided so that you may identify a link when reviewing metrics such as clicks. For example, if the same link appears twice in your email, once in the intro copy and once at the bottom in a call to action, you can identify which link was clicked by its index. The first link, appearing earlier in the HTML, will have a lower index.  
The indices are assigned consecutively and determined entirely by the link's location in the HTML and not by the link URL itself. For example, if the links in your email appear in the following order: `example.com`, `example2.com`, `example.com`, `example3.com`, `example.com`, each link will have an index relative to the links appearing before and after it regardless of the link URL. This means the indices for `example.com` will be 0, 2, and 4 in the previous example list. The index for `example2.com` will be 1, and the index for `example3.com` will be 3.



Link URL| Index  
---|---  
example.com| 0  
example2.com| 1  
example.com| 2  
example3.com| 3  
example.com| 4  
  
  * `attempt` \- the number of times SendGrid has attempted to deliver this message.
  * `category` \- [Categories](/docs/sendgrid/glossary/categories "Categories") are custom tags that you set for the purpose of organizing your emails. If you send single categories as an array, they will be returned by the webhook as an array. If you send single categories as a string, they will be returned by the webhook as a string.
  * `type`
  * **Bounce event** : indicates whether the bounce event was a hard bounce (type=bounce) or block (type=blocked).
  * **Account status change event** : The status a user has been switched to for compliance reasons
    * _compliance_suspend_ : This user's mail is blocked from being delivered. Incoming mail will still be queued, but will bounce at the scheduled delivery time if this state has not been resolved.
    * _compliance_deactivate_ : In addition to the events in a suspension, a deactivated user will see incoming mail queues rejected and current queued mail deleted. The user will be banned after 48 hours.
    * _compliance_ban_ : In addition to the events in a deactivation, website access is removed, billing is canceled, and all assigned IPs are removed.
    * _reactivate_ : The user's account has returned to normal active status.
  * `sg_machine_open` \- A new Boolean field that indicates whether or not an open event has been generated by Apple Mail Privacy Protection (MPP). When this field is set to `true`, it means that SendGrid has received signals indicating that a recipient with MPP enabled has triggered an open event. When this field is `false`, it indicates that the event was triggered by a conventional open. This field was added as a response to the anonymization of some open event tracking caused by [Apple Mail Privacy Protection(link takes you to an external page)](https://sendgrid.com/blog/apple-mail-privacy-protection "Apple Mail Privacy Protection").
  * `bounce_classification` \- Twilio SendGrid conveniently buckets SMTP failure messages into classifications by mapping each unique response to one of seven groups: Invalid Address, Technical, Content, Reputation, Frequency/Volume, Mailbox Unavailable, or Unclassified. See our [Bounce Classifications documentation](/docs/sendgrid/ui/analytics-and-reporting/bounce-and-block-classifications "Bounce Classifications documentation") to understand each classification.
  * `type` \- Used in the account status change event, the current account status type for the user.



String categories:

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "email": "john.doe@sendgrid.com",
    
    
    4
    
        "timestamp": 1337966815,
    
    
    5
    
        "category": "newuser",
    
    
    6
    
        "event": "open"
    
    
    7
    
      },
    
    
    8
    
      {
    
    
    9
    
        "email": "jane.doe@sendgrid.com",
    
    
    10
    
        "timestamp": 1337966815,
    
    
    11
    
        "category": "olduser",
    
    
    12
    
        "event": "open"
    
    
    13
    
      }
    
    
    14
    
    ]

Array:

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "email": "john.doe@sendgrid.com",
    
    
    4
    
        "timestamp": 1337966815,
    
    
    5
    
        "category": ["newuser", "transactional"],
    
    
    6
    
        "event": "open"
    
    
    7
    
      },
    
    
    8
    
      {
    
    
    9
    
        "email": "jane.doe@sendgrid.com",
    
    
    10
    
        "timestamp": 1337966815,
    
    
    11
    
        "category": "olduser",
    
    
    12
    
        "event": "open"
    
    
    13
    
      }
    
    
    14
    
    ]

  * `asm_group_id` \- The ID of the unsubscribe group the recipient's email address is included in. ASM IDs correspond to the ID that is returned when you create an unsubscribe group.
  * `unique_args` or `custom_args`



* * *

## Unique Arguments and Custom Arguments

unique-arguments-and-custom-arguments page anchor

Positive FeedbackNegative Feedback

Events generated by SendGrid can include [unique arguments](/docs/sendgrid/for-developers/sending-email/unique-arguments "unique arguments") or custom arguments.

(information)

## Info

Unique arguments and custom arguments essentially have the same function. However, unique arguments are used in the SMTP API or V2 Mail Send, and custom arguments are used in the V3 Mail Send.

### Unique Arguments

unique-arguments page anchor

Positive FeedbackNegative Feedback

To define and receive unique arguments when sending email with the [SMTP API](/docs/sendgrid/for-developers/sending-email/building-an-x-smtpapi-header "SMTP API") or the [v2 Mail Send endpoint](/docs/sendgrid/v2-api/mail "v2 Mail Send endpoint"), use the `unique_args` parameter in the X-SMTPAPI header. For example, if you have an application and want to receive custom parameters such as the `userid` and the email `template`, you would submit them with the X-SMTPAPI header, as described [here](/docs/sendgrid/for-developers/sending-email/unique-arguments "here").

For example, if you include the following unique arguments in your x-smtpapi header for an email sent via the v2 Mail Send endpoint:

Copy code block
    
    
    1
    
    {
    
    
    2
    
      "unique_args": {
    
    
    3
    
        "userid": "1123",
    
    
    4
    
        "template": "welcome"
    
    
    5
    
      }
    
    
    6
    
    }

You will receive the same unique argument included with the data posted to your Event Webhook:

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "sg_message_id": "sendgrid_internal_message_id",
    
    
    4
    
        "email": "john.doe@sendgrid.com",
    
    
    5
    
        "timestamp": 1337966815,
    
    
    6
    
        "event": "click",
    
    
    7
    
        "url": "https://sendgrid.com",
    
    
    8
    
        "userid": "1123",
    
    
    9
    
        "template": "welcome"
    
    
    10
    
      }
    
    
    11
    
    ]

(warning)

## Warning

You can create unique arguments with the same words as reserved keys, such as "event" or "email". However, SendGrid will default to the reserved key and NOT your unique argument for events that contain a reserved key as an object. See the example below.

### Reserved Keys in Unique Arguments

reserved-keys-in-unique-arguments page anchor

Positive FeedbackNegative Feedback

Copy code block
    
    
    1
    
    //for this example, assume we're sending to john.doe@sendgrid.com
    
    
    2
    
    {
    
    
    3
    
      "unique_args": {
    
    
    4
    
        "customerAccountNumber": "55555",
    
    
    5
    
        "activationAttempt": "1",
    
    
    6
    
        "New Argument 1": "New Value 1",
    
    
    7
    
        "email": "jane.doe@sendgrid.com",
    
    
    8
    
        "event": "SendEmail"
    
    
    9
    
      }
    
    
    10
    
    }

### The resulting webhook call

the-resulting-webhook-call page anchor

Positive FeedbackNegative Feedback

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "event": "Processed",
    
    
    4
    
        "timestamp": "123456789",
    
    
    5
    
        "customerAccountNumber": "55555",
    
    
    6
    
        "activationAttempt": "1",
    
    
    7
    
        "New Argument 1": "New Value 1",
    
    
    8
    
        "email": "john.doe@sendgrid.com"
    
    
    9
    
      }
    
    
    10
    
    ]

(information)

## Info

You will notice that the unique arguments, "event" and "email", were overwritten because they are reserved keys for SendGrid's values.

### Custom Arguments

custom-arguments page anchor

Positive FeedbackNegative Feedback

Any custom arguments that you include with an email sent through [v3 Mail Send](/docs/sendgrid/api-reference/mail-send/mail-send "v3 Mail Send") gets added to your Event Webhook response.

For example, if you were to include the following custom arguments in a personalization in your payload to the v3 Mail Send endpoint:

Copy code block
    
    
    1
    
    {
    
    
    2
    
      "personalizations": [
    
    
    3
    
        {
    
    
    4
    
          "to": [
    
    
    5
    
            {
    
    
    6
    
              "email": "example@example.com"
    
    
    7
    
            }
    
    
    8
    
          ],
    
    
    9
    
          "subject": "Hello, World!",
    
    
    10
    
          "custom_args": {
    
    
    11
    
            "userid": "1123"
    
    
    12
    
          }
    
    
    13
    
        }
    
    
    14
    
      ],
    
    
    15
    
      "from": {
    
    
    16
    
        "email": "from_address@example.com"
    
    
    17
    
      },
    
    
    18
    
      "content": [
    
    
    19
    
        {
    
    
    20
    
          "type": "text/plain",
    
    
    21
    
          "value": "Hello, World!"
    
    
    22
    
        }
    
    
    23
    
      ]
    
    
    24
    
    }

The Event Webhook response:

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "userid": "1123"
    
    
    4
    
      }
    
    
    5
    
    ]

For emails sent through our Marketing Campaigns feature, we add Marketing Campaigns specific parameters to the Event Webhook.

  * `singlesend_id`
  * `singlesend_name`



### Example event from a Single Send

example-event-from-a-single-send page anchor

Positive FeedbackNegative Feedback

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "category": [],
    
    
    4
    
        "email": "email@example.com",
    
    
    5
    
        "event": "open",
    
    
    6
    
        "ip": "127.0.0.1",
    
    
    7
    
        "mc_stats": "singlesend",
    
    
    8
    
        "phase_id": "send",
    
    
    9
    
        "send_at": "1591726752372",
    
    
    10
    
        "sg_content_type": "html",
    
    
    11
    
        "sg_event_id": "sendgrid_internal_event_id",
    
    
    12
    
        "sg_message_id": "sendgrid_internal_message_id",
    
    
    13
    
        "sg_template_id": "sendgrid_template_id",
    
    
    14
    
        "sg_template_name": "sendgrid_template_name",
    
    
    15
    
        "singlesend_id": "sendgrid_singlesend_id",
    
    
    16
    
        "singlesend_name": "Example Single Send",
    
    
    17
    
        "template_hash": "sendgrid_template_hash",
    
    
    18
    
        "template_id": "sendgrid_template_id",
    
    
    19
    
        "template_version_id": "sendgrid_template_version_id",
    
    
    20
    
        "timestamp": 1591726752372,
    
    
    21
    
        "useragent": "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
    
    
    22
    
      }
    
    
    23
    
    ]

  * `marketing_campaign_id`
  * `marketing_campaign_name`



### Example event from a standard (non-A/B test) campaign send

example-event-from-a-standard-non-ab-test-campaign-send page anchor

Positive FeedbackNegative Feedback

Copy code block
    
    
    1
    
    {
    
    
    2
    
      "category": [],
    
    
    3
    
      "email": "email@example.com",
    
    
    4
    
      "event": "processed",
    
    
    5
    
      "marketing_campaign_id": 12345,
    
    
    6
    
      "marketing_campaign_name": "campaign name",
    
    
    7
    
      "post_type": "event",
    
    
    8
    
      "sg_event_id": "sendgrid_internal_event_id",
    
    
    9
    
      "sg_message_id": "sendgrid_internal_message_id",
    
    
    10
    
      "sg_user_id": 12345,
    
    
    11
    
      "smtp-id": "",
    
    
    12
    
      "timestamp": 1442349428
    
    
    13
    
    }

### Example event from an A/B Test

example-event-from-an-ab-test page anchor

Positive FeedbackNegative Feedback

`marketing_campaign_version` is displayed in the event data for emails sent as part of an A/B Test. The value for `marketing_campaign_version` are returned as `A`, `B`, `C`, etc.

Copy code block
    
    
    1
    
    {
    
    
    2
    
      "category": [],
    
    
    3
    
      "email": "tadpole_0010@stbase-018.sjc1.sendgrid.net",
    
    
    4
    
      "event": "processed",
    
    
    5
    
      "marketing_campaign_id": 23314,
    
    
    6
    
      "marketing_campaign_name": "unique args ab",
    
    
    7
    
      "marketing_campaign_version": "B",
    
    
    8
    
      "marketing_campaign_split_id": 13471,
    
    
    9
    
      "post_type": "event",
    
    
    10
    
      "sg_event_id": "qNOzbkTuTNCdxa1eXEpnXg",
    
    
    11
    
      "sg_message_id": "5lFl7Fr1Rjme_EyzNNB_5A.stfilter-015.5185.55F883172.0",
    
    
    12
    
      "sg_user_id": 939115,
    
    
    13
    
      "smtp-id": "<5lFl7Fr1Rjme_EyzNNB_5A@stismtpd-006.sjc1.sendgrid.net>",
    
    
    14
    
      "timestamp": 1442349848
    
    
    15
    
    }

### Example event from the winning phase of an A/B Test

example-event-from-the-winning-phase-of-an-ab-test page anchor

Positive FeedbackNegative Feedback

Copy code block
    
    
    1
    
    {
    
    
    2
    
      "category": [],
    
    
    3
    
      "email": "tadpole_0001@stbase-018.sjc1.sendgrid.net",
    
    
    4
    
      "event": "delivered",
    
    
    5
    
      "marketing_campaign_id": 23314,
    
    
    6
    
      "marketing_campaign_name": "unique args ab",
    
    
    7
    
      "post_type": "event",
    
    
    8
    
      "response": "250 Ok ",
    
    
    9
    
      "sg_event_id": "X2M1IUfMRhuAhWM0CbmFqQ",
    
    
    10
    
      "sg_message_id": "fPJrJPIRTxC_obpgfTy74w.stfilter-015.5185.55F883564.0",
    
    
    11
    
      "sg_user_id": 12345,
    
    
    12
    
      "smtp-id": "",
    
    
    13
    
      "timestamp": 1442349911
    
    
    14
    
    }

### Legacy Marketing Email Unsubscribes

legacy-marketing-email-unsubscribes page anchor

Positive FeedbackNegative Feedback

For emails sent through our Legacy Marketing Email tool, unsubscribes look like the following example:

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "email": "nick@sendgrid.com",
    
    
    4
    
        "timestamp": 1380822437,
    
    
    5
    
        "newsletter": {
    
    
    6
    
          "newsletter_user_list_id": "10557865",
    
    
    7
    
          "newsletter_id": "1943530",
    
    
    8
    
          "newsletter_send_id": "2308608"
    
    
    9
    
        },
    
    
    10
    
        "category": ["Tests", "Newsletter"],
    
    
    11
    
        "event": "unsubscribe"
    
    
    12
    
      }
    
    
    13
    
    ]

### Pool

pool page anchor

Positive FeedbackNegative Feedback

`pool` \- For emails sent with a specified IP Pool, you can view the IP Pool in the event data for a processed event.

Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "email": "john.doe@sendgrid.com",
    
    
    4
    
        "smtp-id": "<14c583da911.2c36.1c804d@ismtpd-073>",
    
    
    5
    
        "timestamp": 1427409578,
    
    
    6
    
        "pool": {
    
    
    7
    
          "name": "new_MY_test",
    
    
    8
    
          "id": 210
    
    
    9
    
        },
    
    
    10
    
        "sg_event_id": "RHFZB1IrTD2Y9Q7bUdZxUw",
    
    
    11
    
        "sg_message_id": "14c583da911.2c36.1c804d.filter-406.22375.55148AA99.0",
    
    
    12
    
        "event": "processed"
    
    
    13
    
      }
    
    
    14
    
    ]

### Click

click-2 page anchor

Positive FeedbackNegative Feedback

event| email| url| category  
---|---|---|---  
click| Message recipient| URL Clicked| The category you assigned  
  
Copy code block
    
    
    1
    
    [
    
    
    2
    
      {
    
    
    3
    
        "sg_event_id": "sendgrid_internal_event_id",
    
    
    4
    
        "sg_message_id": "sendgrid_internal_message_id",
    
    
    5
    
        "ip": "255.255.255.255",
    
    
    6
    
        "useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
    
    
    7
    
        "event": "click",
    
    
    8
    
        "email": "email@example.com",
    
    
    9
    
        "timestamp": 1249948800,
    
    
    10
    
        "url": "http://yourdomain.com/blog/news.html",
    
    
    11
    
        "url_offset": {
    
    
    12
    
          "index": 0,
    
    
    13
    
          "type": "html"
    
    
    14
    
        },
    
    
    15
    
        "unique_arg_key": "unique_arg_value",
    
    
    16
    
        "category": ["category1", "category2"],
    
    
    17
    
        "newsletter": {
    
    
    18
    
          "newsletter_user_list_id": "10557865",
    
    
    19
    
          "newsletter_id": "1943530",
    
    
    20
    
          "newsletter_send_id": "2308608"
    
    
    21
    
        },
    
    
    22
    
        "asm_group_id": 1
    
    
    23
    
      }
    
    
    24
    
    ]

* * *

## Additional Resources

additional-resources page anchor

Positive FeedbackNegative Feedback

  * [Getting started with the Event Webhook](/docs/sendgrid/for-developers/tracking-events/getting-started-event-webhook "Getting started with the Event Webhook")
  * [Troubleshooting the event webhook](/docs/sendgrid/for-developers/tracking-events/twilio-sendgrid-event-webhook-overview "Troubleshooting the event webhook")
  * [An Event Webhook case study(link takes you to an external page)](https://sendgrid.com/blog/leveraging-sendgrids-event-api "An Event Webhook case study")
  * [Webhook web libraries](/docs/sendgrid/for-developers/sending-email/libraries "Webhook web libraries")
  * [Analyze, Visualize, and Store SendGrid Event Data with Keen](/docs/sendgrid/for-developers/tracking-events/tracking-data-with-keen-io "Analyze, Visualize, and Store SendGrid Event Data with Keen")
  * [Email Event Data with Keen](/docs/sendgrid/for-developers/tracking-events/tracking-data-with-keen-io "Email Event Data with Keen")


