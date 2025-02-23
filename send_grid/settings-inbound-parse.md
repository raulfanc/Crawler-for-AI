Skip to contentSkip to navigationSkip to topbar

[Go to the Twilio SendGrid Docs home page](/docs/sendgrid)

Twilio SendGrid Docs

[Twilio SendGrid LogoTwilio SendGrid Docs](/docs)

Search```K`

Search```K`

Search```K`

# Settings - Inbound Parse

Positive FeedbackNegative Feedback

* * *

Twilio SendGrid's Inbound Parse Webhook allows you to receive emails as multipart/form-data at a URL of your choosing. SendGrid will grab the content, attachments, and the headers from any email it receives for your specified hostname.

See "[Setting up the Inbound Parse Webhook](/docs/sendgrid/for-developers/parsing-email/setting-up-the-inbound-parse-webhook "Setting up the Inbound Parse Webhook")" for help configuring the Webhook. You can also manage the Inbound Parse Webhook in the [Twilio SendGrid App(link takes you to an external page)](https://app.sendgrid.com/settings/parse "Twilio SendGrid App").

To begin processing email using SendGrid's Inbound Parse Webhook, you will have to setup MX Records, choose the hostname (or receiving domain) that will be receiving the emails you want to parse, and define the URL where you want to `POST` your parsed emails. If you do not have access to your domain's DNS records, you must work with someone in your organization who does.
