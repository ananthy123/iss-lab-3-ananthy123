## Usage
* Access the registration form by visiting http://localhost:5000/.
* Fill out the registration form and submit the details.
* Upon successful registration, you will be redirected to a success page.
* You can view user details by visiting http://localhost:5000/user/<user_id>, where <user_id> is the user's ID.
* (Assumptions) The user ID has to start from 1 to any integer, the default user ID has been set to 0. When the user creates a new ID, the default ID will be added too for example purposes.
## Project Structure
* registration.py: The main Flask application file.
* templates/: Contains HTML templates for the application.
* form.html: Registration form template.
* success.html: Success page template.
* user_details.html: User details template.
* user_not_found.html: User not found template.
* users.txt: JSON file to store user registration details.
