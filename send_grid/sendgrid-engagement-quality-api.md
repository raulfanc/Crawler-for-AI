Skip to contentSkip to navigationSkip to topbar

[Go to the Twilio SendGrid Docs home page](/docs/sendgrid)

Twilio SendGrid Docs

[Twilio SendGrid LogoTwilio SendGrid Docs](/docs)

Search```K`

Search```K`

Search```K`

On this page

# SendGrid Engagement Quality API

Positive FeedbackNegative Feedback

* * *

* * *

## API Overview

api-overview page anchor

Positive FeedbackNegative Feedback

The SendGrid Engagement Quality (SEQ) API allows you to retrieve metrics that define the quality of your email program.

An SEQ score is correlated with:

  * The quality of the data in a sender's program.
  * How "wanted" the sender's email is by their recipients.



Because "wanted" email and deliverability are closely related, a higher SEQ metric is correlated with greater deliverability. This means the higher your SEQ score, the more likely you are to land in your recipients' inboxes. See the SEQ Overview page to understand SEQ, how it's calculated, and how you can address your score. The SEQ endpoints allow you to retrieve your scores and scores for your Subusers.

(information)

## Info

SendGrid Engagement Quality (SEQ) scores are stored for a maximum of 90 days.

This document explains the SendGrid Engagement Quality (SEQ) metric and how to use it to make more informed decisions about your email program. Improving the quality of your email program increases the probability of making it to your recipients' inboxes.

Using the SEQ API, you can:

  * [Retrieve your Engagement Quality Scores](/docs/sendgrid/api-reference/sendgrid-engagement-quality-api/get-engagement-quality-scores "Retrieve your Engagement Quality Scores").
  * [Retrieve your Subusers Engagement Quality Scores](/docs/sendgrid/api-reference/sendgrid-engagement-quality-api/get-subusers-engagement-quality-scores "Retrieve your Subusers Engagement Quality Scores").



(information)

## Info

The SendGrid Engagement Quality API is available across all [SendGrid plans(link takes you to an external page)](https://sendgrid.com/pricing "SendGrid plans"), including the free tier. If the API does not return a score, it's likely that you have not enabled open tracking, or your account is not meeting the activity threshold required to generate a score.

To receive an SEQ score, the SendGrid account or Subuser must:

  * [Turn on open tracking](/docs/sendgrid/ui/account-and-settings/tracking#open-tracking "Turn on open tracking").
  * Send at least 1,000 messages during the previous 30 days.



* * *

## Base URL

base-url page anchor

Positive FeedbackNegative Feedback

All URLs referenced in the API documentation have the following base:

`https://api.sendgrid.com`

* * *

## What is SEQ?

what-is-seq page anchor

Positive FeedbackNegative Feedback

SEQ is Twilio SendGrid's engagement quality metric. We created it to help senders better understand the quality of their email programs.

An SEQ score is correlated with:

  * The quality of the data in a sender's program.
  * How "wanted" the sender's email is by their recipients.



Because "wanted" email and deliverability are closely related, a higher SEQ metric is correlated with greater deliverability. This means the higher your SEQ score, the more likely you are to land in your recipients' inboxes. SEQ measures the quality of a sender's mail based on the grading of their performance statistics as described in the following sections.

### How does SEQ use performance metrics?

how-does-seq-use-performance-metrics page anchor

Positive FeedbackNegative Feedback

SEQ looks at the following key email performance metrics:

  * Engagement recency
  * Unique open rates
  * Bounce rates
  * Bounce classification
  * Spam rate



Each metric determines a part of your overall SEQ score, which will range between 1 and 5—the higher the score the better your overall engagement. From there, you can get a breakdown of the performance of each key metric, also ranking from 1 to 5, with 1 being the worst and 5 being the best.  
For example, a sender may have an overall SEQ score of a 4 with the following breakdown of scores for each key metric:

  * Engagement recency: 4
  * Unique open rate: 5
  * Bounce rate: 5
  * Bounce classification: 5
  * Spam rate: 5



In this example, the sender will want to focus on improving their engagement recency, the only 4 in their key metrics. They can do this by ensuring that they focus on sending to those recipients who have recently engaged with their emails and removing those recipients who have not engaged in a long time. See the rest of this page for more tips on how to improve your score for each key metric.

There are a few things to keep in mind when using SEQ. If you do not have open tracking turned on or have not sent at least 1,000 messages in the last 30 days, SendGrid cannot calculate your SEQ score, and no score will be returned. Your goal should not be to have perfect rankings across all metrics but to have the best possible score for your email program as a whole. SEQ is unique to each single Twilio SendGrid account, meaning each Subuser also has its own SEQ score. The 1 through 5 ranking correlates with the performance of your weighted score that is correlated with a weighted score we do not expose at this time.

* * *

## 5 key component breakdown

5-key-component-breakdown page anchor

Positive FeedbackNegative Feedback

### Engagement recency

engagement-recency page anchor

Positive FeedbackNegative Feedback

Engagement is a key factor that inbox providers evaluate when determining the quality of your sending. Typically, a mailbox provider will assess a sender's mail based on the positive and negative engagement of their recipients. For example, when a recipient opens and clicks your message, that's positive, while not opening or marking your message as spam is negative.

Engagement recency measures the percentage of unique email addresses a customer has sent to in the past 30 days that have also engaged (opened or clicked) with an email in the past 90 days. A higher percentage of previously engaged recipients indicates a higher likelihood of mail being "wanted."

SendGrid tracks engagement recency via the [Open Tracking feature](/docs/sendgrid/ui/account-and-settings/tracking#open-tracking "Open Tracking feature") located in your Twilio SendGrid account. Keep in mind that [Apple Machine Opens](/docs/sendgrid/for-developers/tracking-events/understanding-apple-mail-privacy-protection-and-open-events "Apple Machine Opens") are removed from this metric.

A low engagement recency metric means that you are sending to many email addresses that have not engaged with an email from your account in the past 90 days. We use engagement recency in our SEQ metric because engagement is a key factor in how inbox providers determine the quality of your sending.

#### **How to improve engagement recency**

how-to-improve-engagement-recency page anchor

**Sunset policy**

You can improve your engagement recency by creating a [sunset policy(link takes you to an external page)](https://sendgrid.com/blog/building-your-business-case-for-an-email-sunset-policy/ "sunset policy") that removes unengaged senders from your list. Sunsetting is the strategy of reducing the number of emails recipients receive (or dropping recipients from your list altogether) when they haven't engaged with your messages after a set length of time.

The best sunset policies are dynamic. For example, after one month of non-engagement, you should start sending _less_ email to those recipients. After 3 months, you should start sending even less frequently. After 6 months, you should send a [re-engagement campaign(link takes you to an external page)](https://sendgrid.com/blog/4-tips-for-sending-re-engagement-email-campaigns/ "re-engagement campaign"). If the recipient(s) doesn't engage with the re-engagement campaign, you should remove them from your list entirely. This will help keep positive interactions high by sending to those you know will engage and reduce negative signals by sending less to those who are not engaging. Engagement recency is a major factor looked at by inbox providers when making an assessment about your emails.

**Opt-in workflow**

Improving your [opt-in workflow(link takes you to an external page)](https://sendgrid.com/blog/double-opt-in-3-helpful-tricks-to-confirm-your-subscribers/ "opt-in workflow") can also help improve your engagement recency. Confirmed opt-in is the gold standard for obtaining permission to send a recipient marketing messages. Not implementing confirmed opt-in can lead to recipients being added to your list who really don't want your messages. In addition to confirmed opt-in, setting proper expectations at the point of sign up will ensure that your recipients know what types of messages they should expect to receive from you. This will also boost engagement recency.

### Unique open rate

unique-open-rate page anchor

Positive FeedbackNegative Feedback

Email open rate represents the percentage of recipients who have opened an email in proportion to the total number of people to whom the mail was delivered. The open rate metric looks at the unique open rates for the last 7 days and 30 days of your 5 most contacted mailbox providers. The lowest rate of these three measures is used to calculate your unique open rate. Apple Machine Opens and non delivery events like blocks or bounces are removed when calculating this metric.

#### How to improve unique open rates

how-to-improve-unique-open-rates page anchor

**Dynamic sending lifecycle**

You can improve unique open rates by creating a dynamic sending lifecycle, meaning you send less email over time as people stop engaging with your communications.

**A/B test**

You can [A/B test different email strategies(link takes you to an external page)](https://sendgrid.com/blog/ab-testing-explained-used-transactional-email/ "A/B test different email strategies") as you make content and lifecycle frequency changes. Monitor which strategy has a more positive response, such as higher open rates and conversions. You should look at your SendGrid stats along with customer engagement data of your own to determine trends where people engage more or less. Keep positive interactions high and negative ones low by implementing a sunset policy. For example, you may stop sending marketing emails to customers who haven't engaged in the last three to six months.

**Segmentation**

Segment your content types as well as your recipients. If you are sending marketing and transactional content from the same account, consider splitting these into their own mail streams. Transactional email and marketing email are evaluated differently by inbox providers. We recommend segmenting these by utilizing Subusers depending on your account package. See our [Onboarding Guide](/docs/sendgrid/onboarding/email-api/evaluate-and-plan-your-strategy "Onboarding Guide") for help building an ideal account structure.

You should also review your engagement statistics by mailbox provider. If you have a single mailbox provider that is underperforming in terms of unique open rate, start sending less mail to that domain by targeting only very recently engaged recipients. After a few weeks, your open rate should improve at that mailbox provider and result in a better unique open rate metric.

### Bounce rate

bounce-rate page anchor

Positive FeedbackNegative Feedback

A bounce occurs when a message is sent to an email address that is undeliverable. The bounce rate metric represents the percentage of emails that bounce as compared to the total number of emails you've attempted to send in the last 7 days and 30 days. When calculating the bounce rate, we only consider permanent bounces that result from sending to non-existent email addresses. The highest of these bounce rates is used to calculate this metric. Generally, a high bounce rate will be an indicator of email acquisition issues, whether that's issues with address validation or sign-up forms that need to be improved.

#### How to Improve Bounce Rates

how-to-improve-bounce-rates page anchor

**Opt-in and address validation**

Implementing fully confirmed opt-in will help improve your bounce rate metric by eliminating invalid addresses at the point of signup. You can also leverage SendGrid's [email address validation API(link takes you to an external page)](https://sendgrid.com/solutions/email-api/email-address-validation-api/ "email address validation API") to validate emails at the point of signup.

**Sunset Policy**

Implementing an effective sunsetting policy will also help improve your bounce rate. An inactive email address can be technically valid; however, these inactive addresses are often "switched off" and then become invalid. A sunsetting policy will ensure these inactive addresses are removed from your list long before they become invalid and generate a bounce.

### Bounce classification

bounce-classification page anchor

Positive FeedbackNegative Feedback

Twilio SendGrid audits the bounce responses provided to us by inbox providers and classifies them into [seven different categories(link takes you to an external page)](https://sendgrid.com/blog/bounce-and-block-classifications/ "seven different categories"). The bounce classification metric used for SEQ considers bounces with a "Reputation" or "Content" classification. These two classifications were chosen as they are indicators that inbox providers are seeing too many negative signals from your emails, and the providers are refusing to deliver emails because of this sending behavior.

#### **How to Improve Bounce Classification**

how-to-improve-bounce-classification page anchor

If you have a low bounce classification metric, we recommend ensuring that you're sending timely and relevant messages to your recipients. Many of the same strategies that apply to addressing the other engagement metrics apply to addressing bounce rate issues. You may:

  * Sunset addresses that have not engaged in the last few months.
  * Confirm addresses are valid before you add them to your marketing lifecycle.
  * Avoid sending third-party or unnecessary emails.
  * A/B test content changes if your content is being highlighted in bounce classifications.



It's also important to check your IP addresses and sending domains to determine if they're listed on any blocklists. You can then work with the blocklist provider to remediate the issue. Bounce classifications are provided in both [Deliverability insights(link takes you to an external page)](https://sendgrid.com/blog/get-started-with-deliverability-insights/ "Deliverability insights") and via the[Event Webhook.(link takes you to an external page)](https://sendgrid.com/blog/bounce-block-classifications-in-event-webhook/ "Event Webhook.")

It's also a good idea to determine which mailbox providers are sending these negative signals. You can use Deliverability Insights or our Event Webhook to view this data by inbox provider.

### Spam rate

spam-rate page anchor

Positive FeedbackNegative Feedback

Spam rate is an indicator of poor quality email. Recipients generally only mark emails as spam when they are confused as to why they are receiving the content or they are unhappy with the emails they are receiving. Spam rate for SEQ evaluates recent spam complaints over the short term (7 days).

#### **How to improve spam rate**

how-to-improve-spam-rate page anchor

If you have a low spam rate metric, we recommend ensuring that you're sending timely and relevant messages to your recipients. You may:

  * Ensure the people you are sending to have explicitly opted in and are very aware of your brand. There should be no confusion as to why they are receiving these emails.
  * Send at a frequency that makes sense to how people engage with your brand. Sending too many emails can cause email fatigue. Be very clear in your opt-in process as to what your sending cadence will be. Consider allowing people to choose the frequency of which you send them marketing emails.



* * *

## Why should senders use SEQ?

why-should-senders-use-seq page anchor

Positive FeedbackNegative Feedback

SEQ makes understanding the performance of your emails seamless. It helps you understand how wanted your emails are and where you have opportunities for improvement. Keeping positive interactions high and negative ones low increases the chances of your emails getting to the inbox.

* * *

## How can you use SEQ today?

how-can-you-use-seq-today page anchor

Positive FeedbackNegative Feedback

SendGrid has found that SEQ is not only helpful in directing senders on how to improve their sending, but it can also be used to monitor and manage traffic at scale. You can review Subuser SEQ scores to decide how to group senders in IP Pools (it is a best practice to group senders by sending habits and reputation), and you can use it to quickly identify and troubleshoot an underperforming sender among your Subusers if you send on behalf of many users.

* * *

## Conclusion

conclusion page anchor

Positive FeedbackNegative Feedback

Using SEQ is a powerful way to understand a sender's email deliverability performance. In understanding how wanted your emails are and by making the right improvements, you can increase your chances of getting to the inbox. If you desire a more customized plan for how you send emails and assistance evaluating your SEQ performance, we suggest working with our Email Deliverability consultants - they have additional insight and experience that helps senders make the right improvements to your email program.
