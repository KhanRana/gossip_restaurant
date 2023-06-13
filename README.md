# Dine & Gossip

![Dine & Gossip](documentation/pages/responsive.png)

Dine & Gossip is restaurant table booking system website built using Django, Python, HTML, CSS and JavaScript.

This project was created as my fourth milestone project for my Level 5 Diploma in Web Application Development with the Code Institute. On the website, A registered user can book a table, change or/and cancel a booking. The user can also change email, username and profile photo. 

[Visit Dine & Gossip Here](https://gossip-dining.herokuapp.com/)


---

## Contents

* [User Experience](#project-background)
    * [Project Goals](#project-goals)
  * [Project Plan](#scope-plan)
    * [Feature Planning](#feature-planning)
  * [Structure Plane](#structure-plane)
    * [User Stories](#user-stories)
    * [Database Schema](#database-schema)
  * [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
    * [Defensive Programming](#defensive-programming)
  * [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Database Used](#database-used)
  * [Frameworks Used](#frameworks-used)
  * [Libraries & Packages Used](#libraries--packages-used)
  * [Programs Used](#programs-used)
* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
* [Testing](#testing)
* [Future Implementations](#future-implementations)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## Project Background


#### **Project Goals**

Dine & Gossip is an authentic Malaysian restaurant that serves authentic Malyasian street food.

The primary users will be people who would like to dine in by reserving  tables.

Restaurant industry is booming and and Dine & Gossip are committed to providing great customer experience. Therefore, an advance booking system is setup.


## Project Plan

#### **Feature Planning**
The site has two main users: customers and admin. User roles are included in this project as there are different features of the site dependant on what type of user you are.  Users (who have registered) and Admins (users who have superuser status and are able to perform additional tasks on the site reserved for shop owners, such as adding new products.) Admins are also able to use their accounts in the same way a user would. Followin user stories have been implemented. Details can be found in the github project issues.

 Feature | 
| :--- | :--- | 
| User roles | ✅ |
| Register as a user| | ✅ |
| Admin panel | ✅ |
| User login | ✅ |
| User logout | ✅ |
| User Profile | ✅ |
| User profile update | ✅ |
| Book a table | ✅ |
| Change a booking | ✅ |
| Cancel a booking | ✅ |
| View menu | ✅ |
| Check your bookings| ✅ |
| See notification of success or error | ✅ |


I used github kanban board to manage the project and user stories.

![Project Management](documentation/stories/user_stories.png)



#### **Database Schema**

I have opted to use a relational database as this will best suit my requirements. The schema is created by using pygraphviz and pydot.

![Database Schema](documentation/database/database-schema.png)

Auth and djano_admin log is produced using DBSchema.

![Database Schema](documentation/database/auth&django.png)


### Website Skeleton

#### **Wireframes**

Wireframes for the project were created using [Balsamiq](https://balsamiq.com/)

* Base Template - This template contains the header and footer which are used throughout the website. This template is used as a base and then other pages content will be injected into main section using django template language.

![Base Template Wireframe](documentation/wireframes/base.png)

* Home Page

![Home Page Wireframe](documentation/wireframes/home.png)

* Register Page - The register page will allow users to register for an account with a username/email 

    ![Register Page Wireframe](documentation/wireframes/register.png)
  
* Authorised User - Once a user has setup an accout they can access table bookings and their profiles and can update it 
    ![Profile Page Wireframe](documentation/wireframes/authorised_user.png)

* Login Page - The login page will allow users to sign into their account with either their username.

    ![Login Page Wireframe](documentation/wireframes/login.png)

* Logout Page - The logout page will ask the user to confirm they wish to logout. If the user clicks the logout button they will be logged out of their account and redirected to the logout page with a login link.

  ![Log out Page Wireframe](documentation/wireframes/logout.png)

* Profile Page - Users can see and update their profile.

  ![Profile Page Wireframe](documentation/wireframes/profile.png)

* Bookings (Admin View) - The Admin view of the products page is identical to that for a user, except for the addition of an edit and delete button below each item. This will allow the admin to be able to edit or delete products easily from the products view page.

* Menu Page - User can see the menu 

![Profile Page Wireframe](documentation/wireframes/menu.png)

* Book a tabe - Table booking form

![Profile Page Wireframe](documentation/wireframes/table.png)

* Bookings - Users can see all their bookings and link to manage them

![Profile Page Wireframe](documentation/wireframes/bookings.png)

---


#### **Defensive programming**

Defensive programming has been used throughout the site to prevent users accessing pages when they don't have the relevant permissions. This has been accomplished by checking whether a user is a superuser for admin related tasks. If users try to access pages that they don't have the required permission level for, they will directed to sign in page. Only logged in user can have access to only their on bookings and profiles.

#### **Home Page**

The home page shows an image of some delicious Malaysian food with amessage that it is real Malay food. 

![Home Page Screenshot](documentation/pages/home.png)

### **About Page**
The about page shows a brief introduction to the business, their inspiration.

![Home Page Screenshot](documentation/pages/about.png)


#### **Booking Page**

Logged in user can access this page and can select a table for the given number of peoples for a future date. 

![Products Page Screenshot](documentation/pages/table.png)


#### **Menu**

User can access this page and see the available items on the menu.

![Products Page Screenshot](documentation/pages/menu.png)


#### **Manage Booking**

The page shows a list of users bookings which they can manage as well. 

![Product Details Page Screenshot](documentation/pages/bookings.png)


#### **Update Booking  Page**

Whe a user selects a booking from the list, the update booking page would let the user change or cancel the booking.

![Product Details Page Screenshot](documentation/pages/update_booking.png)

#### **Profile Page**

The profile page is broken into two sections,  one for the users currnt details and a form to updates users name, email and photo.

![Profile Page Screenshot](documentation/pages/profile.png)


#### **Admin Page for managing the site**

The admin page for website is only accessible for superusers.  The admin page is where superusers can create, edit and delete menu, bookings, edit and delete profile. Create, update and delete bookings.

![Admin Page Screenshot](documentation/pages/admin.png)

#### **Register Page**

The signup page asks the user to enter their email address twice (to prevent any input errors) select a username for their account, and then input their password twice (again to check for input errors). The user is also given a link at the bottom if they already have an account. On successful registration, user will be redirected to the login page.

![Signup Page Screenshot](documentation/pages/register.png)

#### **Log in Page**

The sign in page provides inputs for a user to enter their username/email together with their password. A message at the bottom of the page provides a link to users if they don't currently have an account which directs them to the register page. 

![Login page](documentation/pages/login.png)

#### **Logout out page**

When a user selects the logs out, logout out page will be shown with a login link should the user wish to log back in.

![Sign Out Page Screenshot](documentation/pages/logged_out.png)

### Accessibility

I have been mindful during coding to ensure that the website is as accessible friendly as possible. This has been have achieved by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site if any.
* Providing information for screen readers where there are icons used and no text.
* Ensuring that there is a sufficient colour contrast throughout the site. (update on colours chosen explained in the colour scheme section.)

Accessibility was tested using Lighthouse.

![Tests](documentation/tests/accessibility.png)

---

## Technologies Used

### Languages Used

HTML, CSS, JavaScript, Python

### Database Used

PostgreSQL for development and deployment.

[Railway](https://railway.app/)

### Frameworks Used

[Django](https://www.djangoproject.com/) - Version 4.2 - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Version 4.0 - A framework for building responsive, mobile-first sites.

### Libraries & Packages Used

[Font Awesome](https://fontawesome.com/) - Version 6.2.1 - Used for the iconography of the site, this was added using a CDN link.

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Used for authentication, registration & account management.

[django_crispy_forms](https://pypi.org/project/django-crispy-forms/) - provides a tag and filter that lets you quickly render forms

[gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server

[pillow](https://pypi.org/project/Pillow/) - Python imaging library

[dj_databsae_url](https://pypi.org/project/dj-database-url/) - allows us to utilise the DATABASE_URL variable

[psycopg2](https://pypi.org/project/psycopg2/) - a postgres database adapter which allow us to connect with a postgres database

[django-storages](https://pypi.org/project/django-storages/) - a storage backend library

### Programs Used

[Am I Responsive](https://ui.dev/amiresponsive) - To create the responsive images of the site on a variety of device sizes.

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[DBShema](https://dbschema.com/) - Used to host the database.

[Favicon.io](https://favicon.io/) - To create the favicon.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for this project.

[Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot, test features and solve issues with responsiveness and styling.

[Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.

---

## Deployment & Local Development
1. Setup heroku CLI and create 
    ``` npm install -g heroku
    heroku login
    cd ~/myapp
    heroku create gossip-dining
    ```
    

#### **Generate a SECRET KEY & Updating Debug**

1. A secret 16 character string secret key was generated using pythons secrets module
    ``` python
        imoprt secrets
        key = secretc.hex_token(16)
    ```
2. In Heroku settings create a new config var with a key of `SECRET_KEY`. The value will be the secret key we just created. Click add.
3. In settings.py we can now update the `SECRET_KEY` variable, asking it to get the secret key from the environment, or use an empty string in development:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
    ```

4. We can now adjust the `DEBUG` variable to only set DEBUG as true if in development:

    ```python
    DEBUG = 'True' in os.environ
    ```

5. Save, add, commit and push these changes.

### Deployment
1. Cloudinary Storage for images  [Cloudinary](https://cloudinary.com/)

2. Railway App for database Storage [Database](https://railway.app/)

3. Heroku for hosting the website [Heroku](https://heroku.com/apps/gossip-dining/)


#### **Features for next version**

In future implementations I would like to:

* User should not be able to book a table if the booking time on the same day has passed such as booking feature for 6pm should not be available when it is past 6pm.

* User would not be able to cancel bookings from the list if the time has already passed.

* Users can order a collection or delivery

* Login and register using social media accounts 

* Add user reviews for the restaurant with a rating facility for each menu item so other user would know what are the favourites

* Let users to update/reset their passwords

* Due to time constraints, I have not been able to implement the review and menu item like funcionality as I had hoped. However, I would like to include them in the future version.

* I would also like to improve the website layout and make it aesthetically pleasing, and also add a gallery and links to social media accounts.


---

## Testing

### CSS
 * W3C was used to validate the CSS.
 ![CSS Testing](documentation/tests/css.png)
 
 ### Javascript
  * JS hint is used to test the js file
![JS Testing](documentation/tests/js.png)
  
 ### Python
  * I used autopep8 to check all files for PEP8 compilance and then used CI Jupyter to verify the formatting
  ![Python Testing](documentation/tests/jupyter1.png)
  ![Python Testing](documentation/tests/jupyter2.png)

### Manual Testing
* I manually checked all forms, pages and logic for to identify any errors. Python indentation was done by autopep8. 
![Date Testing](documentation/tests/date_test.png)

![Confirm Testing](documentation/tests/booking_confirm.png)

![Double Booking Testing](documentation/tests/double_booking.png)

![Update Testing](documentation/tests/update_booking.png)


### Accessibility
* I used google devtools lighthouse for accessibility scores
![Accessibility](documentation/tests/accessibility.png)


---

## Bugs

* A logic error appeared in my update view that kept creating new booking instead of updating. It turns out, I was using create method instead of update that. Thanks to help from a Tutor who pointed it.

* There was a bug that was causing issues on the menu page. I accidently use an 'id' attribute instead of class for a looping variable.

![Menu Bug](documentation/bugs/menu_bug.png)

The issue was spotted when I was running html test.

![Menu Bug](documentation/bugs/menu_bug_id.png)

*A similar bug was present in the footer where one 'div' tag was not closed properly and that caused issues for the whole website. I discovered the issue when tested for html.

![Footer Bug](documentation/bugs/footer_bug.png)


* I was particulary stuck with a bug which was not restricting users from double booking on the same day. A user could not book a table for the same time any other day though. It turns out my availability function was only testing for the time and not date. After reversing the order of the logic, the bug was fixed. 

* Another interesting bug was to change the user image in the profile. My logic kept resizing and changing the imgage but kept throwning error that the path is not accessible. I tried many way and finally with belowmentioned code help it was fixed.

---

## Credits

### Code Used

I have taken a code snippet to resize the image in the cloudinary.  
[Profile Update](https://stackoverflow.com/users/13449046/takib-ahmed)


### Media

The main background image was taken from free image source unsplash 
[Background for unsplash](https://unsplash.com/images/food)


### Acknowledgments

I would like to acknowledge the following people who have helped me with completing this project:

* My family for their patience and support whilst working on my final project.
* The Code Institute Tutor who assisted me with a particularly difficult bug.
* I would also like to thank my mentor who has provided guidance and encourangement 
* Last but not least a special thanks to Ed the Tutor, who helped me identify and fix last bug in the update view

