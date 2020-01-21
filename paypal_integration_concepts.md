# Using Braintree 





# Client Token 



Client Token - a singled data blob that includes configuration and authorization information required by the Braintree client SDK. 



A new client token should be generated for each request that's sent to Braintree. 



If these tokens are re-used excessively within a short time period, the token will be revoked for security purposes. 



**Server** is responsible for **generating the client token** that contains all of the necessary configuration information to set up the client SDKs. 



When the server provides a client token to your client, it authenticates the application to communicate directly to Braintree. 



**Your client is responsible for obtaining the client token from your server and initialise the client SDK.** 





# Payment method nonce 



The payment method nonce is a string returned by the client SDK to represent a payment method. 



**This contains a reference to the customer payment information which has been provided in your payment form**



This should be sent to your server where it can be used with the server SDKs to create a new transaction request. 







![img](https://developers.braintreepayments.com/img/developers/diagram-overview.png)





1. Your app or web front-end requests a client token from your server in order to initialise the client SDK. 
2. Your server generates and sends a client token back to your client with the server SDk. 
3. Once the client SDK is initialised and the customer has submitted payment infromation, the SDK communicates that information to Braintree and returns a payment method nonce. 
4. Send the payment method nonce to your server 
5. your server code receives the payment method nonce from your client and then uses the server SDK to create a transaction or perform other functions. 







# Crudentials



##   Credentials    





Your sandbox credentials can be found on your [My Apps & Credentials](https://developer.paypal.com/developer/applications/) page in your PayPal Developer Dashboard.

To obtain your Braintree sandbox credentials:

1. Go to [Sandbox Accounts](https://developer.paypal.com/developer/accounts/) and create a sandbox business test account.
2. Go to [My Apps & Credentials](https://developer.paypal.com/developer/applications/) and generate a Braintree sandbox credential and link it to your PayPal sandbox test account.
3. Repeat these steps for each country you want to test in.

Once you're ready to go live, be sure to switch from your sandbox credentials to production.

**[Next Page: Set Up Your Client →](https://developer.paypal.com/docs/accept-payments/express-checkout/ec-braintree-sdk/client-side/javascript/v3)**





### 