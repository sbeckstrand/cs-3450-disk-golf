# Milestone 3

## General Notes

For full disclosure, I think our team could have done a much better job at sticking to the structure of coordinating sprints as suggested in this milestone document. Instead, we kind of managed our own planning and processes and didnt really observe the requirements of the milestone until well into our sprints. As such, our planning and discussions have been adjusted to suit the needs for the requirements. 

## Requirements

### 1. Sprint Planning Documents

As suggested above, we didnt do a very good job at keeping to the sprint planning structure but did hit most of the points when it comes to having a backlog, creating tasks, having a platform to update them etc. As a note, we used JIRA to track our progress instead of using GitHub issues/stories. 

Additionally, prior to generating our burndown charts we neglected to set time estimates and the reports for closed sprints will not update to reflect changes to estimated time. Instead, our burndown charts reflect number of issues over time. 

##### Sprint 3: 

Notes: 

Unfortunately, in JIRA it is not possible to see the previous backlog for an already closed sprint, and we closed it prior to taking a screenshot. Instead, we took a screenshot of the two tasks we had created for this sprint. 

[Plan](/docs/planning/sprint03/plan.md)

[Burndown](/docs/planning/sprint03/burndown.png)

##### Sprint 4 

[Plan](/docs/planning/sprint04/plan.md)

[Burndown](/docs/planning/sprint04/burndown.png)

##### Sprint 5

[Plan](/docs/planning/sprint05/plan.md)

[Burndown](/docs/planning/sprint05/burndown.png)

### 2. Standup Reports

Located at [/docs/standup-reports](/docs/standup-reports)

### 3. Sprint Retrospective Reports

[Sprint 3](/docs/planning/sprint03/retrospective.md)

[Sprint 4](/docs/planning/sprint04/retrospective.md)

[Sprint 5](/docs/planning/sprint05/retrospective.md)

### 4. 70-80% of Application Completed

<details>
    <summary>List of Requirements</summary>

    #### User Authentication and Access
    a. ~~The system must require all users to authenticate themselves before giving them access to the system.~~
    i. ~~On first login, the system must allow the user to sign up a new account with username and password.~~
    b. ~~On subsequent login, the system must allow users to enter their username and password. If entered correctly, the user must be given access to the system. If entered incorrectly, the system must allow the user to try again.~~
    c. ~~Users have a combination of the following roles/permissions: Manager, Drink Meister, Sponsor.~~
    d. ~~Users with Manager permissions must have access to all Manager features.~~
    e. ~~Users with Drink Meister permissions must have access to all Drink Meister features.~~
    f. Users with Sponsor permissions must have access to all Sponsor features.

    ### User Profile Features
    a. ~~The system will allow any authenticated user to verify their own username and password.~~
    b. The system should not allow any user without Manager permissions from viewing or modifying any other user profile.
    c. ~~The system should allow user to view the balance in their account~~
    d. The system should allow users to preload money into their account.
    e. The system should allow users to use the money from their account.

    ### User Features
    a. ~~All users will be given Default Permissions and will have access to all Default features.~~
    b. The system will allow users with Default rights to sign up for, track, and edit score for tournaments.
    i. The system will allow the User to select a tournament from a list. When the user selects an event, the system will display a new section on the dashboard to enter score.
    c. ~~Users will be able to select a drink at any time, provided by the Drink Meister.~~
    i. If the user decides to order a drink, the system requires the user pays before placing the order.
    d. The User should be able to view a leaderboard of past tournaments.
    i. Tournaments leaderboards will be populated once the given tournament reaches completion by the Manager’s order.
    e. The user should be able to leave the tournament at any point.
    i. ~~No refunds for the drinks ordered.~~

    ### Manager Features
    a. ~~Managers will be given Manager rights and have access to all Manager features.~~
    b. ~~Managers will have the option to start and stop tournaments at any given moment.~~
    i. Managers can allocate prize money, which is contingent on the donations of sponsors.
    c. Managers can change the roles of all other users.

    ### Drink Meister Features
    a. ~~Meisters will be given Drink Meister rights and have access to all Drink Meister features.~~
    b. ~~Meisters must view customer orders.~~
    c. ~~Meisters can Add different drink selections for users.~~
    d. ~~Meisters can Remove different drink selections for users.~~
    e. ~~Meisters can Modify different drink selections for users.~~

    ### Sponsors
    a. Sponsors will be given Sponsor rights and have access to all Sponsor features.
    b. Sponsors must upload a picture file for their logo.
    c. Sponsors allocate donations to be handles and distributed by the Manager role.
    d. Sponsors that donate will have their logos appear on user screens.






    ### Non-Functional Requirements

    1. ~~The system must user a database~~
    a. ~~The system’s database must store user account information, including Username, Password, and Account Balance.~~
    b. ~~The system must store information about the tournaments represented in the system.~~
    i. ~~The system must keep track of the individual users within the tournament by representing them with User ID’s.~~
    2. ~~The team will use the Git version control system, with GitHub as a remote repository.~~
    3. ~~The system must be deployable~~
    a. ~~Can either be local or cloud hosted.~~
    4. ~~The system’s interface must be mobile device friendly.~~
</details>

### 5. Unit Tests Covering major logic

### 6. Updated Documentation







