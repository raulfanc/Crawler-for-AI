Skip to contentSkip to navigationSkip to topbar

[Go to the Twilio SendGrid Docs home page](/docs/sendgrid)

Twilio SendGrid Docs

[Twilio SendGrid LogoTwilio SendGrid Docs](/docs)

Search```K`

Search```K`

Search```K`

On this page

# Setting Up The Inbound Parse Webhook

Positive FeedbackNegative Feedback

* * *

As you're probably aware, SendGrid is great at sending your email, but SendGrid can also help you process email using the Inbound Parse Webhook. The Inbound Parse Webhook processes all incoming email for a domain or subdomain, parses the contents and attachments then `POSTs` multipart/form-data to a URL that you choose.

(information)

## Info

XML is only available in v2.

What your application does with this parsed data is up to you. For some ideas of what the Inbound Parse Webhook can do, check out this [blog post(link takes you to an external page)](https://sendgrid.com/blog/parse-api-oh-what-you-can-do/ "blog post"), and see this [blog post about how to create a microservice for handling SendGrid inbound parse(link takes you to an external page)](https://www.twilio.com/en-us/blog/microservice-template-handle-sendgrid-inbound-parse "blog post about how to create a microservice for handling SendGrid inbound parse").

(information)

## Info

Check out some pre-made integrations for the SendGrid Inbound Parse Webhook in the [Library Index](/docs/sendgrid/for-developers/sending-email/libraries#web-api-libraries "Library Index").

To begin processing email using SendGrid's Inbound Parse Webhook, you will have to setup MX Records, choose the hostname (or receiving domain) that will be receiving the emails you want to parse, and define the URL where you want to `POST` your parsed emails.

* * *

## Set up an MX Record

set-up-an-mx-record page anchor

Positive FeedbackNegative Feedback

  1. Navigate to the MX Records page on your hosting provider's website. If you're unsure who your hosting or DNS provider is, please contact your website administrator.
  2. Create a new MX record for the subdomain (e.g. parse.yourdomain.com) you want to process incoming email.



(information)

## Info

This hostname should be used exclusively to parse your incoming email.

(warning)

## Warning

Do not change the MX record for your domain. If you do, you will no longer receive email.

  1. Assign the MX record a priority of 10, and point it to the address: mx.sendgrid.net.



It should look something like this:

![Inbound_Parse_01_MX_Record.](/_next/image?url=https%3A%2F%2Fdocs-resources.prod.twilio.com%2F79c1299a8ecce3e9988b8ec5ea010c215ca423081b033507386746f8115a04b5.png&w=1920&q=75&dpl=dpl_8VggtwwJsGcMi5ddXk2jMuWz5Sm2)Expand image

(information)

## Info

If there is no field for priority, type 10 before the address. e.g. `10 mx.sendgrid.net.`

* * *

## Point to a Hostname and URL

point-to-a-hostname-and-url page anchor

Positive FeedbackNegative Feedback

  1. From your SendGrid Dashboard click **Settings** , and then click **Inbound Parse**. You are now on the Inbound Parse page.
  2. Click **Add Host & URL**.



Here you will specify the subdomain and root domain of the receiving domain (or hostname). All emails sent to this receiving domain will be parsed.

If you use the same return path (subdomain) as your authenticated domain, you must have Automatic Security disabled on the authenticated domain. Otherwise, those messages will bounce due to an infinite CNAME>MX loop.

(information)

## Info

The URL must be accessible from the public web.

  1. Enter the subdomain (for example, "parse") and select the authenticated root domain for your receiving domain. Enter the public URL where you would like the parsed data to be `POST`ed.



![Setting up inbound parse.](/_next/image?url=https%3A%2F%2Fdocs-resources.prod.twilio.com%2Fe37c2f0171d3bfade682c5e8ceea12702c9c5f578c4496ecaee5a4e4d5d26e51.png&w=1920&q=75&dpl=dpl_8VggtwwJsGcMi5ddXk2jMuWz5Sm2)Expand image

  1. (Optional) Check **Spam Check** if you want Inbound Parse to check incoming email 2.5MB and under for spam. Checking this box will also include the spam report and spam score in the payload. Mail over 2.5MB is highly unlikely to be spam and will receive a SendGrid generated report indicating it's not spam.
  2. (Optional) Check **Send Raw** if you would prefer to receive the full MIME message URL encoded in multipart/form-data.



(warning)

## Warning

If you do not check **Send Raw** , the post will be multipart/form-data with the email content URL encoded, but the attachments will be in multipart/form-data. If your code is only set up to read URL encoding, attachments could be dropped.

  1. Click Save.



You have just finished configuring Inbound Parse!

* * *

## Testing

testing page anchor

Positive FeedbackNegative Feedback

To test if everything is working, send an email from your email account to [example@example.com](mailto:example@example.com "example@example.com").

(information)

## Info

The local-part (i.e. anything before @) can be any* word or combination (except "abuse", "postmaster" and "unsubscribe") because all email for the domain or subdomain will be processed.

*There are three reserved local-parts that must **not** be used: "abuse", "postmaster", and "unsubscribe" (e.g. [abuse@subdomain.domain.com](mailto:abuse@subdomain.domain.com "abuse@subdomain.domain.com"), [postmaster@subdomain.domain.com](mailto:postmaster@subdomain.domain.com "postmaster@subdomain.domain.com"), and [unsubscribe@subdomain.domain.com](mailto:unsubscribe@subdomain.domain.com "unsubscribe@subdomain.domain.com") are **not** allowed.)

(warning)

## Warning

Remember to direct your incoming email to your hostname (for example, [example@example.com](mailto:example@example.com "example@example.com")). If you do not, your incoming email will not be parsed.

* * *

## Default Parameters

default-parameters page anchor

Positive FeedbackNegative Feedback

Parameter| Description  
---|---  
headers| The raw headers of the email.  
dkim| A string containing the verification results of any DKIM and domain keys signatures in the message.  
content-ids| A string containing the number of attachments.  
to| Email recipient field, as taken from the message headers.  
text| Email body in plaintext formatting.  
html| HTML body of email. If not set, email did not have an HTML body.  
from| Email sender, as taken from the message headers.  
sender_ip| A string of the sender's ip address.  
spam_report| Spam Assassin's spam report.  
envelope| A string containing the SMTP envelope. This will have 2 variables: `to`, which is a single-element array containing the address that we received the email to, and `from`, which is the return path for the message.  
attachments| Number of attachments included in email.  
subject| Email Subject.  
spam_score| Spam Assassin's rating for whether or not this is spam.  
attachment-info| A JSON map where the keys are named attachment{X}. Each attachment key points to a JSON object containing three fields, `filename`, `type`, and `content-id`. The `filename` field is the name of the file (if it was provided). The `type` field is the [media type(link takes you to an external page)](http://en.wikipedia.org/wiki/Internet_media_type "media type") of the file. `X` is the total number of attachments. For example, if the number of attachments is 0, there will be no attachment files. If the number of attachments is 3, parameters attachment1, attachment2, and attachment3 will have file uploads.  
charsets| A string containing the character sets of the fields extracted from the message.  
SPF| The results of the Sender Policy Framework verification of the message sender and receiving IP address.  
  
* * *

## Example Default Payload

example-default-payload page anchor

Positive FeedbackNegative Feedback

Copy code block
    
    
    1
    
    [Date] array(16) {
    
    
    2
    
      ["headers"]=>
    
    
    3
    
      string(1970) "Received: by mx0047p1mdw1.sendgrid.net with SMTP id 6WCVv7KAWn Wed, 27 Jul 2016 20:53:06 +0000 (UTC)
    
    
    4
    
    Received: from mail-io0-f169.google.com (mail-io0-f169.google.com [209.85.223.169]) by mx0047p1mdw1.sendgrid.net (Postfix) with ESMTPS id AA9FFA817F2 for <example@example.com>; Wed, 27 Jul 2016 20:53:06 +0000 (UTC)
    
    
    5
    
    Received: by mail-io0-f169.google.com with SMTP id b62so81593819iod.3 for <example@example.com>; Wed, 27 Jul 2016 13:53:06 -0700 (PDT)
    
    
    6
    
    DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=sendgrid.com; s=ga1; h=mime-version:from:date:message-id:subject:to; bh=DpB1CYYeumytcPF3q0Upvx3Sq/oF4ZblEwnuVzFwqGI=; b=GH5YTxjt6r4HoTa+94w6ZGQszFQSgegF+Jlv69YV76OLycJI4Gxdwfh6Wlqfez5yID 5dsWuqaVJZQyMq/Dy/c2gHSqVo60BKG56YrynYeSrMPy8abE/6/muPilYxDoPoEyIr/c UXH5rhOKjmJ7nICKu1o99Tfl0cXyCskE7ERW0=
    
    
    7
    
    X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=1e100.net; s=20130820; h=x-gm-message-state:mime-version:from:date:message-id:subject:to; bh=DpB1CYYeumytcPF3q0Upvx3Sq/oF4ZblEwnuVzFwqGI=; b=Sq6LVHbmywBdt3sTBn19U8VOmelfoJltz8IcnvcETZsYwk96RBxN+RKMN5fOZSKw4j 15HrgdIFfyDmp67YK0ygvOITlTvZ6XY5I0PtnvDtAQt79kS3tKjI3QKJoEp/ZjIjSzlL KG7agl6cxFgBbIN0yHWBOvy3O+ZXY8tZdom1yOvULjmjW1U9JkdOs+aJ6zq4qhZX/RM/ tIgLB461eJ5V95iQDDc5Ibj9Cvy4vJfXLQRO0nLVQAT2Yz58tkEO1bDZpWOPAyUNneIL yhIWp+SpbuqhMA68mq0krG1PjmWalUbpVcGJIGuOKB9mQFFo/MqdrUCjvYnyo1jPLPeX psdQ==
    
    
    8
    
    X-Gm-Message-State: AEkoousvdxmDoxLlTUYJ1AOmCGJv77xRBBlfKv6YrthH0M2NueMwlOxUD6t8nidE9uonXbdJ/DQy/chmHUnN//a4
    
    
    9
    
    X-Received: by 10.107.6.101 with SMTP id 98mr38024553iog.41.1469652785829; Wed, 27 Jul 2016 13:53:05 -0700 (PDT)
    
    
    10
    
    MIME-Version: 1.0
    
    
    11
    
    Received: by 10.107.48.17 with HTTP; Wed, 27 Jul 2016 13:53:05 -0700 (PDT)
    
    
    12
    
    From: Sender Name <example@example.com>
    
    
    13
    
    Date: Wed, 27 Jul 2016 14:53:05 -0600
    
    
    14
    
    Message-ID: <CAN_P_JMvV7ZpAQhOnDienypLrJmuhN=LQWweu4yScw4jQyXY2w@mail.gmail.com>
    
    
    15
    
    Subject: Different File Types
    
    
    16
    
    To: example@example.com
    
    
    17
    
    Content-Type: multipart/mixed; boundary=001a113f8ad03e85160538a4343c
    
    
    18
    
    "
    
    
    19
    
      ["dkim"]=>
    
    
    20
    
      string(22) "{@sendgrid.com : pass}"
    
    
    21
    
      ["content-ids"]=>
    
    
    22
    
      string(37) "{"ii_1562e2169c132d83":"attachment1"}"
    
    
    23
    
      ["to"]=>
    
    
    24
    
      string(26) "example@example.com"
    
    
    25
    
      ["html"]=>
    
    
    26
    
      string(479) "<div dir="ltr">Here&#39;s an email with multiple attachments<div> </div><div><img src="cid:ii_1562e2169c132d83" alt="Inline image 1" width="455" height="544"><br clear="all"><div></div>--  <div class="gmail_signature" data-smartmail="gmail_signature"><div dir="ltr"><img src="https://sendgrid.com/brand/sg-logo-email.png" width="96" height="17"><div></div></div></div></div></div>"
    
    
    27
    
      ["from"]=>
    
    
    28
    
      string(33) "Sender Name example@example.com"
    
    
    29
    
      ["text"]=>
    
    
    30
    
      string(139) "Here's an email with multiple attachments"
    
    
    31
    
      ["sender_ip"]=>
    
    
    32
    
      string(14) "209.85.223.169"
    
    
    33
    
      ["spam_report"]=>
    
    
    34
    
      string(844) "Spam detection software, running on the system "mx0047p1mdw1.sendgrid.net", has
    
    
    35
    
    identified this incoming email as possible spam. The original message
    
    
    36
    
    has been attached to this so you can view it (if it isn't spam) or label
    
    
    37
    
    similar future email. If you have any questions, see
    
    
    38
    
    @@CONTACT_ADDRESS@@ for details.
    
    
    39
    
    
    
    
    40
    
    Content preview:  Here's an email with multiple attachments [image: Inline image1] -- [...]
    
    
    41
    
    
    
    
    42
    
    Content analysis details:   (2.6 points, 5.0 required)
    
    
    43
    
    
    
    
    44
    
     pts rule name              description
    
    
    45
    
    ---- ---------------------- --------------------------------------------------
    
    
    46
    
     0.8 HTML_IMAGE_RATIO_02    BODY: HTML has a low ratio of text to image area
    
    
    47
    
     0.0 HTML_MESSAGE           BODY: HTML included in message
    
    
    48
    
     1.8 HTML_IMAGE_ONLY_08     BODY: HTML: images with 400-800 bytes of words
    
    
    49
    
     0.0 T_MIME_NO_TEXT         No text body parts
    
    
    50
    
    
    
    
    51
    
    "
    
    
    52
    
      ["envelope"]=>
    
    
    53
    
      string(66) "{"to":["example@example.com"],"from":"example@example.com"}"
    
    
    54
    
      ["attachments"]=>
    
    
    55
    
      string(1) "2"
    
    
    56
    
      ["subject"]=>
    
    
    57
    
      string(20) "Different File Types"
    
    
    58
    
      ["spam_score"]=>
    
    
    59
    
      string(5) "2.597"
    
    
    60
    
      ["attachment-info"]=>
    
    
    61
    
      string(287) "{"attachment2":{"filename":"DockMcWordface.docx","name":"DockMcWordface.docx","type":"application/vnd.openxmlformats-officedocument.wordprocessingml.document"},"attachment1":{"filename":"MG_2359.jpg","name":"_MG_2359.jpg","type":"image/jpeg","content-id":"ii_1562e2169c132d83"}}"
    
    
    62
    
      ["charsets"]=>
    
    
    63
    
      string(77) "{"to":"UTF-8","html":"UTF-8","subject":"UTF-8","from":"UTF-8","text":"UTF-8"}"
    
    
    64
    
      ["SPF"]=>
    
    
    65
    
      string(4) "pass"
    
    
    66
    
    }
    
    
    67
    
    
    
    
    68

* * *

## Raw Parameters

raw-parameters page anchor

Positive FeedbackNegative Feedback

Parameter| Description  
---|---  
dkim| A string containing the verification results of any DKIM and domain keys signatures in the message.  
Email| A string containing the email headers, date, body, and attachments  
To| Email recipient field as taken from the message headers.  
cc| Email cc field, as taken from the message headers.  
From| Email sender, as taken from the message headers.  
Text| Email body in plaintext formatting.  
html| HTML body of email. If not set, email did not have an HTML body.  
Sender IP| Email sender IP address.  
Spam Report| Spam Assassin's spam report.  
Envelope| A string containing the SMTP envelope. This will have 2 variables: `to`, which is an single-element array containing the addresses that received the email, and `from`, which is the return path for the message.  
Subject| Email subject.  
Spam_Score| Spam Assassin's rating for whether or not this is spam.  
Charsets| A string containing the character sets of the fields extracted from the message.  
SPF| The results of the Sender Policy Framework verification of the message sender and receiving IP address.  
  
(information)

## Info

We recommend limiting the total size of your message, including the message itself and all attachments, to 30MB. Be aware that other mail handlers will have their own limitations, and some ISPs and companies may either dramatically limit the size and/or type of attachments, or even block them altogether.

* * *

## Example Raw Payload

example-raw-payload page anchor

Positive FeedbackNegative Feedback

Copy code block
    
    
    1
    
    array(11) {
    
    
    2
    
      ["dkim"]=>
    
    
    3
    
      string(22) "{@sendgrid.com : pass}"
    
    
    4
    
      ["email"]=>
    
    
    5
    
      string(8879) "Received: by mx0032p1mdw1.sendgrid.net with SMTP id rOkt2xLLKV Tue, 19 Jul 2016 15:06:29 +0000 (UTC)
    
    
    6
    
    Received: from mail-it0-f45.google.com (mail-it0-f45.google.com [209.85.214.45]) by mx0032p1mdw1.sendgrid.net (Postfix) with ESMTPS id 26D6080397 for <parse@parse.yourdomain>; Tue, 19 Jul 2016 15:06:22 +0000 (UTC)
    
    
    7
    
    Received: by mail-it0-f45.google.com with SMTP id f6so93587860ith.1 for <example@example.com>; Tue, 19 Jul 2016 08:06:22 -0700 (PDT)
    
    
    8
    
    DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=sendgrid.com; s=ga1; h=mime-version:from:date:message-id:subject:to; bh=UYWCIUKTVXyV9U41l+c9+qOlpoeQGcJkKpyOAatNr3Y=; b=c1I/LcqHEJklmAThWr9Z8NKlTPHUlE/8sDSpK382fJtIQcGdUtczG0pijnUHegrFVt FDr4NehtJDD9KFvXLXboLCtObsu5HTN99ckUCCZTibZseA+J8U3jjCqTdj1fmUage5C7 //Iwi0Ndioonzhm18J7KStap66yZ69ED7UxPk=
    
    
    9
    
    X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=1e100.net; s=20130820; h=x-gm-message-state:mime-version:from:date:message-id:subject:to; bh=UYWCIUKTVXyV9U41l+c9+qOlpoeQGcJkKpyOAatNr3Y=; b=lgmLXnmmpNcQMckjshsZsa2/8OjFZzntWYSG5XZo0fi32KHLuBLSHuNDFXn0V4ICp1 1xuT2fZCyhBSgNBiWNbjqFspdemzrBjaI1Tgm/Zz8Fv6wW2XdjpoANNQzJxfdhnecPd5 HvZ5P8+KTqjr4tAa9RmLthDc3UqhV9NRnCnhbW/AZaVQLB8eoJus92tD1GeXpBQml5XF m6vPUGrWGZWNugINkRKxIpk+2uECglAjNm4NpZIi9j7N94CxA18RC4NJ59WIsSybtIer hbCgT1Q13rvGEzvnp6FfFQVbE3DOibNqd0bh/EvZCagFVbnenNc/Q+qHtU9KqFlisSOp xh0w==
    
    
    10
    
    X-Gm-Message-State: ALyK8tINVaZIP8YCgQbpg5ya8EnqQo76uxkXUPpDnM+kAyAQQzehFU10EgyuAe2fAmWf/muBiFDy0JDU74Eclp1/
    
    
    11
    
    X-Received: by 10.36.76.16 with SMTP id a16mr4479786itb.77.1468940781988; Tue, 19 Jul 2016 08:06:21 -0700 (PDT)
    
    
    12
    
    MIME-Version: 1.0
    
    
    13
    
    Received: by 10.107.48.17 with HTTP; Tue, 19 Jul 2016 08:06:21 -0700 (PDT)
    
    
    14
    
    From: Sender Name <example@example.com>
    
    
    15
    
    Date: Tue, 19 Jul 2016 09:06:21 -0600
    
    
    16
    
    Message-ID: <CAN_P_JNa25--hzm5=-ES9cnxgWa+h+E49OOAS7sPpV0gsoXCOw@mail.gmail.com>
    
    
    17
    
    Subject: Hello
    
    
    18
    
    To: example@example.com
    
    
    19
    
    Content-Type: multipart/mixed; boundary=001a11447dc881e40f0537fe6d5a
    
    
    20
    
    
    
    
    21
    
    --001a11447dc881e40f0537fe6d5a
    
    
    22
    
    Content-Type: multipart/alternative; boundary=001a11447dc881e40b0537fe6d58
    
    
    23
    
    
    
    
    24
    
    --001a11447dc881e40b0537fe6d58
    
    
    25
    
    Content-Type: text/plain; charset=UTF-8
    
    
    26
    
    
    
    
    27
    
    This is a test email with 1 attachment.
    
    
    28
    
    
    
    
    29
    
    --001a11447dc881e40b0537fe6d58
    
    
    30
    
    Content-Type: text/html; charset=UTF-8
    
    
    31
    
    Content-Transfer-Encoding: quoted-printable
    
    
    32
    
    
    
    
    33
    
    <div dir=3D"ltr">This is a test email with 1 attachment.<br clear=3D"all"><=
    
    
    34
    
    div> </div>--  <div class=3D"gmail_signature" data-smartmail=3D"gmail=
    
    
    35
    
    _signature"><div dir=3D"ltr"><img src=3D"https://sendgrid.com/brand/sg-logo=
    
    
    36
    
    -email.png" width=3D"96" height=3D"17"> <div> </div></div></div>
    
    
    37
    
    </div>
    
    
    38
    
    
    
    
    39
    
    --001a11447dc881e40b0537fe6d58--
    
    
    40
    
    
    
    
    41
    
    --001a11447dc881e40f0537fe6d5a
    
    
    42
    
    Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document;
    
    
    43
    
        name="DockMcWordface.docx"
    
    
    44
    
    Content-Disposition: attachment; filename="DockMcWordface.docx"
    
    
    45
    
    Content-Transfer-Encoding: base64
    
    
    46
    
    X-Attachment-Id: f_iqtleujy0
    
    
    47
    
    
    
    
    48
    
    UEsDBBQACAgIAHc+80gAAAAAAAAAAAAAAAASAAAAd29yZC9udW1iZXJpbmcu
    
    
    49
    
    eG1spZJBboMwEEVP0Dsg7xNIF1WFQrNo1G66a3uAiTFgxfZYYwPN7euEAC2V
    
    
    50
    
    KkpXCMb//e/hb3cfWkWNICfRZGyzTlgkDMdcmjJj729Pq3sWOQ8mB4VGZOwk
    
    
    51
    
    HNs93Gzb1NT6ICiciwLCuFTzjFXe2zSOHa+EBrdGK0wYFkgafHilMtZAx9qu
    
    
    52
    
    OGoLXh6kkv4U3ybJHbtiMGM1mfSKWGnJCR0W/ixJsSgkF9dHr6A5vp1kj7zW
    
    
    53
    
    wviLY0xChQxoXCWt62l6KS0Mqx7S/HaJRqv+XGvnuOUEbdizVp1Ri5RbQi6c
    
    
    54
    
    C1/33XAgbpIZCzwjBsWcCN89+yQapBkw53ZMQIP3Onhfl3ZBjRcZd+HUnCDd
    
    
    55
    
    6EUeCOj0MwUs2OdXvZWzWjwhBJWvaSjkEgSvgHwPUEsICvlR5I9gGhjKnJez
    
    
    56
    
    6jwh5RJKAj2W1P3pz26SSV1eK7BipJX/oz0T1pbFD59QSwcIJ5yx3VgBAAC7
    
    
    57
    
    BAAAUEsDBBQACAgIAHc+80gAAAAAAAAAAAAAAAARAAAAd29yZC9zZXR0aW5n
    
    
    58
    
    cy54bWyllMFuozAQhp9g3wH5nkCqardCJZXaqnvZPaV9gIltwIrtscYGNm+/
    
    
    59
    
    JgTYZqWKpieMx/P94/GvuX/4Y3TSSvIKbcE264wl0nIUylYFe3t9Wd2xxAew
    
    
    60
    
    AjRaWbCj9Oxh++2+y70MIZ7ySSRYnxtesDoEl6ep57U04NfopI3BEslAiL9U
    
    
    61
    
    pQbo0LgVR+MgqL3SKhzTmyz7zs4YLFhDNj8jVkZxQo9l6FNyLEvF5fkzZtAS
    
    
    62
    
    3SHlGXljpA0nxZSkjjWg9bVyfqSZa2kxWI+Q9qNLtEaP5zq3RE0QdLHRRg9C
    
    
    63
    
    HZJwhFx6H3efh+BE3GQLGtgjpowlJbzXHCsxoOyE6c1xAZq011H73LQTar7I
    
    
    64
    
    3AuvlxQyhH6pPQEd/68Crujnv/lOLXLxBSFmhYYmQ16D4DVQGAH6GoJGfpDi
    
    
    65
    
    CWwLk5lFtcjOFyShoCIws0n9p152k13YZVeDkzOt+hrtJ2Hj2DYOIKG803B8
    
    
    66
    
    BH6o4qYVJ6Gky1uIXtqw9HRIltDo8Ar7XUA3Bn/cZEN4GETzajcMtQlyy+LS
    
    
    67
    
    gonmfjezfqOQfaghtfw6vWQ6a6bzDN3+BVBLBwiI6qJIqQEAAIgFAABQSwME
    
    
    68
    
    FAAICAgAdz7zSAAAAAAAAAAAAAAAABIAAAB3b3JkL2ZvbnRUYWJsZS54bWyl
    
    
    69
    
    lE1OwzAQhU/AHSLv26QsEIqaVogKNuyAA0wdJ7Fqe6yxk9Db4zZ/UCQUysqK
    
    
    70
    
    J+974/GT19sPraJGkJNoMrZaJiwShmMuTZmx97enxT2LnAeTg0IjMnYUjm03
    
    
    71
    
    N+s2LdB4FwW5canmGau8t2kcO14JDW6JVphQLJA0+PBJZayBDrVdcNQWvNxL
    
    
    72
    
    Jf0xvk2SO9ZjMGM1mbRHLLTkhA4Lf5KkWBSSi34ZFDTHt5PskNdaGH92jEmo
    
    
    73
    
    0AMaV0nrBpq+lhaK1QBpfjtEo9XwX2vnuOUEbbgLrTqjFim3hFw4F3Z3XXEk
    
    
    74
    
    rpIZAzwhRsWcFr57Dp1okGbEnJJxARq9l8G7H9oZNR1kmoVTcxrpSi9yT0DH
    
    
    75
    
    n13AFfP8qrdyVoovCEHlaxoDeQ2CV0B+AKhrCAr5QeSPYBoYw5yXs+J8Qcol
    
    
    76
    
    lAR6Cqn7082ukou4vFZgxUQr/0d7Jqwt2/SvT9SmBnSI3gNJUCzerOP+Wdp8
    
    
    77
    
    AlBLBwhpMWDsagEAANgEAABQSwMEFAAICAgAdz7zSAAAAAAAAAAAAAAAAA8A
    
    
    78
    
    AAB3b3JkL3N0eWxlcy54bWzdV+1u2jAUfYK9A8r/NiEEhlBphai6Taq6ae0e
    
    
    79
    
    wDgO8XBsy3ag7OlnJ04CCZkyoKMa/Eh8r++518fHH7m5e01Ib42ExIxOnf61
    
    
    80
    
    5/QQhSzEdDl1frw8XI2dnlSAhoAwiqbOFknn7vbDzWYi1ZYg2dPxVE4SOHVi
    
    
    81
    
    pfjEdSWMUQLkNeOIamfERAKUboqlmwCxSvkVZAkHCi8wwWrr+p43ciwMmzqp
    
    
    82
    
    oBMLcZVgKJhkkTIhExZFGCL7KCJEl7x5yD2DaYKoyjK6AhFdA6MyxlwWaMmx
    
    
    83
    
    aNoZFyDrPw1inZCi34Z3yRYKsNGTkZA80YaJkAsGkZTaep87S8S+14FAA1FG
    
    
    84
    
    dClhP2dRSQIwLWGMNGpAZe5rnduSlkFVA6m4kKRLIbnrES8EENtmFeAIPnfj
    
    
    85
    
    Oe6k4hqCjlKpKAV5DASMgVAFADkGgTC4QuEc0DUoxRwuO8m5hhRisBQgqUQq
    
    
    86
    
    /2pm+15NLs8x4KhCW56G9kmwlDu3evsJGbxHEUiJkqYpvgnbtK3s8cCokr3N
    
    
    87
    
    BEiI8dSZCQy05DYTKHcaCEg1kxjsmOIZlWV/10AttHUNtEq9vI1rbZkAQuaA
    
    
    88
    
    y7pdCbxCNSNkhInSlv1s71+F1fcLy1zWbWlhoHpLzk16B1czgpe0cC2ARATn
    
    
    89
    
    btcS4tZp4vWWeawQ4k/oVdVqNuZHDVgf4AaHbDPXPAtGClff1s4B1HNm+I8U
    
    
    90
    
    EiZEvy+QVh+yDVOiHtjHUdH4nhJtAKlilmcaGg+KlI0QeBkX7xEWUj1mELaa
    
    
    91
    
    n7CowYTYwXM7+N3hug0FZeeZjlZbrvE4EGYd8NjkyVxfwqnzZNZNppAwjzRj
    
    
    92
    
    NcEUJKialaxTnjsLbcIrsCBoD/rFWDrhZz17Tx2yHB7EZwTM8d4EjnNHz06f
    
    
    93
    
    kVD4tVRUlVBH7ehj194ioX6LhNp00vf3lBJ4Xps8oBaeTpQC8lyCVNBuWZHd
    
    
    94
    
    EKr1FXjN9ZXbdlbLMbT6rbT674zWwehctNY3x4rmwYFtLLedSPOglebBpWke
    
    
    95
    
    77PsvxXLe6dIMDD/xikyPnCKjM9Af9BKf/C+6PfH56J/j+5R9mvQHRygOzgD
    
    
    96
    
    3cNWuofvjO7gX9Ldekc6ke5RK92j/5VuXEt8EfpfsNK3osZ9J7NemPfR4bvr
    
    
    97
    
    2e4jwwNkDk8i8zldqIN8lo4LUzrw34TTM3701T/yOiyKwYF75aDlXlm8ydvf
    
    
    98
    
    UEsHCCJgqpxzAwAAhxMAAFBLAwQUAAgICAB3PvNIAAAAAAAAAAAAAAAAEQAA
    
    
    99
    
    AHdvcmQvZG9jdW1lbnQueG1spZXfbtsgFMafYO8QcZ/YibKpsur0YlF3s01R
    
    
    100
    
    2z0AAWyjAAcdcNLs6Qf+2yVV5WW+QZzD+X2f4QjuH161mh0FOgkmJ8tFSmbC
    
    
    101
    
    MODSlDn59fI4vyMz56nhVIEROTkLRx42n+5PGQdWa2H8LBCMyzTLSeW9zZLE
    
    
    102
    
    sUpo6hZghQnJAlBTH6ZYJpriobZzBtpSL/dSSX9OVmn6hXQYyEmNJusQcy0Z
    
    
    103
    
    goPCx5IMikIy0Q19BU7RbUu2neVGMUGhggcwrpLW9TR9Ky0kqx5y/Ognjlr1
    
    
    104
    
    6052ihpHegrHoVUrdALkFoEJ50J02yYH4jKdsIERMVRMsfC3Zu9EU2kGTGyO
    
    
    105
    
    C9CgvQja3aY1qPFHxr1waoqRNvVd7pHi+doFvWE/39ZbOamLLwihytc4NOQt
    
    
    106
    
    CFZR9D1A3UJQwA6Cf6XmSIdm5uWkdr4gcUlLpHpsUvdPJ7tML9rluaJWjLTy
    
    
    107
    
    /2jfEGpLNuEC2lN2KMPM8NkpY6Ag3ASPzUeSJg/8HEcb0uF+4085SbuPdKGt
    
    
    108
    
    UNfB3XXoaSsKWiv/TmaHb4KN3A7jwMB48eprqp4tZcF4KDjSKBfdJcM6/MjK
    
    
    109
    
    O5avBbEDeXUp0WTi2ArGVU4w36635fPvUFCFW//z3brhh7tguVqt03b/bPmD
    
    
    110
    
    Rnd78B5CIy3X7SoPdpwoUfhxhrKs+mnH+Fnrl7MVIRmeEYzJzlzvJOlPKhnf
    
    
    111
    
    lM0fUEsHCOH0LWYNAgAAmAYAAFBLAwQUAAgICAB3PvNIAAAAAAAAAAAAAAAA
    
    
    112
    
    HAAAAHdvcmQvX3JlbHMvZG9jdW1lbnQueG1sLnJlbHOtkktqAzEMhk/QOxjt
    
    
    113
    
    O54kpZQSTzYlkG2ZHsCZ0TyILRtLKZ3b1xTyghC6mKV+o0+fkNebH+/UNyYe
    
    
    114
    
    AxlYFCUopCa0I/UGvurt8xsoFkutdYHQwIQMm+pp/YnOSu7hYYysMoTYwCAS
    
    
    115
    
    37XmZkBvuQgRKb90IXkruUy9jrY52B71sixfdbpmQHXDVLvWQNq1C1D1FPE/
    
    
    116
    
    7NB1Y4MfoTl6JLkzQjOK5MU4M23qUQyckiKzQN9XWM6p0AWS2u4dXhzO0SOJ
    
    
    117
    
    1ZwSdPR7THnvi8Q5eiTxMusxZHJ4fYq/+jRe33yw6hdQSwcIY4WdHeEAAACo
    
    
    118
    
    AgAAUEsDBBQACAgIAHc+80gAAAAAAAAAAAAAAAALAAAAX3JlbHMvLnJlbHON
    
    
    119
    
    zzsOwjAMBuATcIfIO03LgBBq0gUhdUXlAFHiphHNQ0l49PZkYADEwGj792e5
    
    
    120
    
    7R52JjeMyXjHoKlqIOikV8ZpBufhuN4BSVk4JWbvkMGCCTq+ak84i1x20mRC
    
    
    121
    
    IgVxicGUc9hTmuSEVqTKB3RlMvpoRS5l1DQIeREa6aautzS+G8A/TNIrBrFX
    
    
    122
    
    DZBhCfiP7cfRSDx4ebXo8o8TX4kii6gxM7j7qKh6tavCAuUt/XiRPwFQSwcI
    
    
    123
    
    LWjPIrEAAAAqAQAAUEsDBBQACAgIAHc+80gAAAAAAAAAAAAAAAATAAAAW0Nv
    
    
    124
    
    bnRlbnRfVHlwZXNdLnhtbLWTTU7DMBCFT8AdIm9R4sICIdS0C36WwKIcYOpM
    
    
    125
    
    Wgv/yTMp7e2ZtCGLqkiwyM7jN/Pe55E8X+69K3aYycZQq5tqpgoMJjY2bGr1
    
    
    126
    
    sXop71VBDKEBFwPW6oCklour+eqQkAoZDlSrLXN60JrMFj1QFRMGUdqYPbCU
    
    
    127
    
    eaMTmE/YoL6dze60iYExcMm9h1rMn7CFznHxeLrvrWsFKTlrgIVLi5kqnvci
    
    
    128
    
    njD7Wv9hbheaM5hyAKkyumMPbW2i6/MAUalPeJPNZNvgvyJi21qDTTSdl5Hq
    
    
    129
    
    K+Ym5WiQSJbqXUXILKch9R0yv4IXW9136h+1Gh45DQIfHP4GcNQmjW/FawVr
    
    
    130
    
    h5cJRnlSiND5NWY5X4YY5UkhRsWDDZdBxpaBQx+/3uIbUEsHCAD+7s4fAQAA
    
    
    131
    
    ugMAAFBLAQIUABQACAgIAHc+80gnnLHdWAEAALsEAAASAAAAAAAAAAAAAAAA
    
    
    132
    
    AAAAAAB3b3JkL251bWJlcmluZy54bWxQSwECFAAUAAgICAB3PvNIiOqiSKkB
    
    
    133
    
    AACIBQAAEQAAAAAAAAAAAAAAAACYAQAAd29yZC9zZXR0aW5ncy54bWxQSwEC
    
    
    134
    
    FAAUAAgICAB3PvNIaTFg7GoBAADYBAAAEgAAAAAAAAAAAAAAAACAAwAAd29y
    
    
    135
    
    ZC9mb250VGFibGUueG1sUEsBAhQAFAAICAgAdz7zSCJgqpxzAwAAhxMAAA8A
    
    
    136
    
    AAAAAAAAAAAAAAAAKgUAAHdvcmQvc3R5bGVzLnhtbFBLAQIUABQACAgIAHc+
    
    
    137
    
    80jh9C1mDQIAAJgGAAARAAAAAAAAAAAAAAAAANoIAAB3b3JkL2RvY3VtZW50
    
    
    138
    
    LnhtbFBLAQIUABQACAgIAHc+80hjhZ0d4QAAAKgCAAAcAAAAAAAAAAAAAAAA
    
    
    139
    
    ACYLAAB3b3JkL19yZWxzL2RvY3VtZW50LnhtbC5yZWxzUEsBAhQAFAAICAgA
    
    
    140
    
    dz7zSC1ozyKxAAAAKgEAAAsAAAAAAAAAAAAAAAAAUQwAAF9yZWxzLy5yZWxz
    
    
    141
    
    UEsBAhQAFAAICAgAdz7zSAD+7s4fAQAAugMAABMAAAAAAAAAAAAAAAAAOw0A
    
    
    142
    
    AFtDb250ZW50X1R5cGVzXS54bWxQSwUGAAAAAAgACAD/AQAAmw4AAAAA
    
    
    143
    
    
    
    
    144
    
    --001a11447dc881e40f0537fe6d5a--
    
    
    145
    
    "
    
    
    146
    
      ["to"]=>
    
    
    147
    
      string(22) "example@example.com"
    
    
    148
    
      ["from"]=>
    
    
    149
    
      string(33) "Sender Name <example@example.com>"
    
    
    150
    
      ["sender_ip"]=>
    
    
    151
    
      string(13) "209.85.214.45"
    
    
    152
    
      ["spam_report"]=>
    
    
    153
    
      string(798) "Spam detection software, running on the system "mx0032p1mdw1.sendgrid.net", has
    
    
    154
    
    identified this incoming email as possible spam. The original message
    
    
    155
    
    has been attached to this so you can view it (if it isn't spam) or label
    
    
    156
    
    similar future email. If you have any questions, see
    
    
    157
    
    @@CONTACT_ADDRESS@@ for details.
    
    
    158
    
    
    
    
    159
    
    Content preview:  This is a test email with 1 attachment.
    
    
    160
    
    Content analysis details:   (0.4 points, 5.0 required)
    
    
    161
    
    
    
    
    162
    
     pts rule name              description
    
    
    163
    
    ---- ---------------------- --------------------------------------------------
    
    
    164
    
     0.0 HTML_MESSAGE           BODY: HTML included in message
    
    
    165
    
     0.3 HTML_IMAGE_ONLY_04     BODY: HTML: images with 0-400 bytes of words
    
    
    166
    
     0.0 T_MIME_NO_TEXT         No text body parts
    
    
    167
    
    
    
    
    168
    
    "
    
    
    169
    
      ["envelope"]=>
    
    
    170
    
      string(73) "{"to":["example@example.com"],"from":"example@example.com"}"
    
    
    171
    
      ["subject"]=>
    
    
    172
    
      string(5) "Hello"
    
    
    173
    
      ["spam_score"]=>
    
    
    174
    
      string(5) "0.353"
    
    
    175
    
      ["charsets"]=>
    
    
    176
    
      string(47) "{"to":"UTF-8","subject":"UTF-8","from":"UTF-8"}"
    
    
    177
    
      ["SPF"]=>
    
    
    178
    
      string(4) "pass"
    
    
    179
    
    }

* * *

## Additional Resources

additional-resources page anchor

Positive FeedbackNegative Feedback

  * [Parse API](/docs/sendgrid/api-reference/settings-inbound-parse/create-a-parse-setting "Parse API") \- Manage Inbound Parse Webhook settings using the Parse API (Web API v3).
  * [Parse Settings Subuser](/docs/sendgrid/v2-api/customer_subuser_api/parse_settings "Parse Settings Subuser") \- Get current Parse settings and create, edit, and delete entries using the Subuser API (Web API v2).
  * [Reseller API Parse Settings](/docs/sendgrid/v2-api "Reseller API Parse Settings") \- Get current Parse settings and create, edit, and delete entries using the Reseller API (Web API v2).
  * [Reseller Customer Subuser Parse Settings](/docs/sendgrid/v2-api "Reseller Customer Subuser Parse Settings") \- Get current Parse settings and create, edit, and delete entries using the Reseller Customer Subuser API (Web API v2).



### Statistics

statistics page anchor

Positive FeedbackNegative Feedback

SendGrid provides [statistics(link takes you to an external page)](https://app.sendgrid.com/statistics/parse_webhook "statistics") of how many emails are parsed over time. You can specify what is displayed on the graph by adjusting the statistics filters.

For more information, please see [Parse Webhook Stats](/docs/sendgrid/api-reference/webhooks/retrieves-inbound-parse-webhook-statistics "Parse Webhook Stats").
