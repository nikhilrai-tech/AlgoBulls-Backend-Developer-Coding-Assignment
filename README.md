# AlgoBulls-Backend-Developer-Coding-Assignment
Design a simple To-Do List App using Django
Create a Django app with appropriate models to store information for the To-do List
app. The app should be able to store the following information:
a. Timestamp: Timestamp at which a task was created.
Should be auto-set when creating a new entry. A user should not be able to
edit this.
b. Title: Title of the task to be done.
i. A user can set this while creating a new entry. A user can also change
this while updating an existing entry.
ii. Max length: 100 characters.
iii. Mandatory field
c. Description: Description of the task to be done.
i. A user can add details about this task.
ii. Max length: 1000 characters
iii. Mandatory field
d. Due Date: Expected due date to finish the task
i. A user can set this while creating a new entry. A user can also change
this while updating an existing entry.
ii. Optional field
e. Tag: One or more tags that the user can add to the entry
i. A user can set this while creating a new entry. A user can also change
this while updating an existing entry. Multiple tags can be added to the
same entry
ii. Optional field
iii. Multiple tags with the same value should be saved only once.
f. Status: Shows status of a task
i. Should be one of these values.
1. OPEN (Default value)
2. WORKING
3. DONE
4. OVERDUE
ii. Mandatory field
2. Django Admin interface should be enabled for the model(s). The admin site should
have the following:
a. Appropriate validation checks are in place. The ones defined in Point 1 above
should be enforced.
(Ex: In 1.a, A user should not be able to edit the timestamp.)
b. Proper changelist view with filters for every model
c. Proper fieldsets for every model
3. The following REST APIs should be created using DRF (DjangoRestFramework):
a. CREATE a todo item
b. READ one todo item
c. READ all todo items
d. UPDATE a todo item
e. DELETE a todo item
4. Create & Share a working Postman Collection which can be used to test all the APIs
mentioned in Point 3. Above.
5. Enable support for Basic Authentication for all the API
