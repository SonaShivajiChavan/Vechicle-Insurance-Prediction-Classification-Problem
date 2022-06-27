Vechicle Insurance Prediction

Background:
Just like medical insurance, there is vehicle insurance where every year customer needs to pay a premium of certain amount to insurance provider company so that in case of unfortunate accident by the vehicle, the insurance provider company will provide a compensation (called ‘sum assured’) to the customer. Building a model to predict whether a customer would be interested in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue.

The goal is:
Build machine learning model to predict whether the policyholders (customers) from past year will also be interested in Vehicle Insurance provided by the company.

Feature Descriptions:
id: Unique ID for the customer
Gender: Gender of the customer
Age: Age of the customer
Driving_License: 0 : Customer does not have DL, 1 : Customer already has DL
Region_Code: Unique code for the region of the customer
Previously_Insured: 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance
Vehicle_Age: Age of the Vehicle
Vehicle_Damage: 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past.
Annual_Premium: The amount customer needs to pay as premium in the year
PolicySalesChannel: Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.
Vintage: Number of Days, Customer has been associated with the company
Response: 1 : Customer is interested, 0 : Customer is not interested