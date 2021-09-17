Tournament App

1. Introduction and Context:

During large disk golf tournaments, effective organization can be difficult to achieve. To remedy the issue, this project's goal is to build an application that permits users to access only what they need for their roles in the tournament.

The application will allow users to define their role for all upcoming tournaments, as well as sign up digitally for any tournament designated. Users who plan out these tournaments have the option to use administrative tools to set up tournament dates, prize money, and other user roles.

The application will allow users to login to track their own score as they advance through the tournament. A leaderboard will be established using live data, which will be posted at the conclusion of each tournament.



2. Users and their Goals:

The following Use Case diagrams will describe the application's actors and their interactions.














ROLES/Permissions:

DEFAULT USER – Can also be considered a “Player” role. Initial set of permissions for every User that first logs onto our application. They will have immediate access to sign up for a tournament, order drinks, input funding (ATM), or request an Admin/Manager for additional roles.

MANAGERS – Application admins. They approve or decline all role requests by the default user. They set up and close out the tournaments and manage/reward the money donated by Sponsors.

SPONSORS – Provide the money to the Manager for the prize money. Upload an image of logo is required to run this role, to be displayed when funding is provided. 

DRINK MEISTER – Receives orders for drinks by Default User, approves drink and supplies the drink to them.



Database:

Tourney	Description	Holes	Participants	StartDate

Drink	Description	Type	Price
