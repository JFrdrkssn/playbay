<h1 align="center" style="font-size: 250%;"><b>
PlayBay
</b></h1>

PlayBay is a site centered on the PlayStation® gaming console. 

The purpose of the site is to provide a place where people interested in PlayStation® can read and post entries ranging from news to group plays, interact with other users and act as a hub solely dedicated to the console. 

It is designed to look and feel similar to the PlayStation® 5 brand and console.

Users can register an account to access full CRUD functionality for posting on the site. 

[Check the live project here!](https://playbay.herokuapp.com/)

![Am I Responsive?](media/air.png)

<br/><br/>

# **User Experience (UX)**

## **User stories**

- ### First visit

  - As a User, I want to intuitively understand what the site is about.

- ### Navigation

  - As a User, I want to intuitively understand how to navigate the site.
  - As a User, I want it to be clear where I am on the site.
  - As a User, I want to be able to search and filter posts based on category.
  - As a User, I want to be able to search for post titles and content.

- ### Registration

  - As a User, I want to be able to register an account so I can further interact with the site.
  - As a User, I want to be able to add profile information about myself.

- ### Site Interaction

  - As a User, I want to be able to post entries.
  - As a User, I want to be able to edit and delete posts created by me.
  - As a User, I want to be able to comment on posts.
  - As a User, I want to be able to like/upvote posts.

- ### Admin

    - As an Admin, I want to be able to manage posts.
    - As an Admin, I want to be able to manage comments.
    - As an Admin, I want to be able to add content specific related content, like categories.

  <br/><br/>

## **Design**

- **Color Scheme**

  - A white background coupled with shades of blue, gold and grey provides clear contrast that is also easy on the eyes. It matches the aesthetic profile of the PlayStation® 5 console, giving a clear connection between the two.
  - The navigation bar and footer of the site has a sharper white, providing a very slight contrast to the main contents of the site.
  - Images for posts can be uploaded by a user, therefore the prominent white color coupled mostly with blue helps create a neutral background for images of any composition.
  - Some smaller elements are gold. In the world of PlayStation®, the gold/yellow color scheme is part of a special subscription model, and provide a great contrast to the white and blue colors that are part of the core brand color scheme.

- **Typography**

  - The Play font is used for the site logo. The font has a modern and sleek look while also reminding of the font used by the PlayStation® brand itself.
  - The Poppins font is used everywhere else on the site. It is clear, sleek and provide a good separation between characters, making it easy to read and blending in well.
  - Sans-serif is used as a backup-font.

## **Wireframes**

- [Home](media/wireframes/homewf.png)
- [Post](media/wireframes/postdetailwf.png)
- [Add Post](media/wireframes/addwf.png)
- [Edit Post](media/wireframes/editwf.png)
- [Delete Post](media/wireframes/deletewf.png)
- [Register](media/wireframes/regwf.png)
- [Log in](media/wireframes/linwf.png)
- [Log out](media/wireframes/loutwf.png)

## **Bad UX**
When a user posts or edits a post, the resulting text content is displayed as one chunk of text. When editing a post created as a superuser on the admin panel (Summernote WYSIWYG), the form field when editing on the deployed site shows Markdown being applied. A normal user would have to implement their own Markdown or let a superuser edit the post on the admin panel. This is not preferable at all.
<br/>
A reference to adding a Rich Text Editor as a future feature can be found below.
<br/><br/>

# **Agile**

For this project the GitHub Kanban agile project management tool was used for workflow.
![Kanban](media/kanban.png)
<br/><br/>

# **Unfinished Features**

## _These features were never implemented due to time constraint._

- Search and filter - A search bar for listing and filtering specific content.
  <br/><br/>

## _These features are planned._

- Profile page
  - A profile page where users can do things like adding profile picture, PlayStation® username and change password.
    <br/><br/>
- Nested comment system
  - A system for replying to certain comments and create threads.
    <br/><br/>
- Image copyright control
  - A system for checking copyright protected material. A first draft would be to implement an "approved" status on uploaded media, where the admin can check validity.
    <br/><br/>
- Image resizing and compression
  - Cloudinary, which is used by the site to store images, has an auto-transform function. This would help resize and compress images to prevent them from being too big and slowing down the site.
    <br/><br/>
- Rich text editor - The default text field when adding posts does not provide enough customization. A rich text editor would help format blog post content.
  <br/><br/>

# **Data Model**

## ERD

![ERD](media/db_diagram_playbay.png 'ERD')

## User Model (AllAuth)

- ID of User is linked via a ForeignKey relation in the Post Model author field.
- ID of User is linked via a ForeignKey relation in the Post Model likes ManyToMAny field.
- ID of User is linked via a ForeignKey relation in the Comment Model user field.

## Post Model

- ID of Post is linked via a ForeignKey relation in the Comment Model post field.

## Database

- SQLite has been used in delevopment to store data.
- PostgreSQL is used in production to store data.
  <br/><br/>

# **Technologies**

## **Languages**

- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.w3schools.com/js/js_es6.asp)
- [Python](https://www.python.org/)

## **Programs**

- [Gitpod](https://gitpod.io)
  - Gitpod was used to host a virtual workspace.
- [Git](https://git-scm.com/)
  - Git was used for version control by utilizing the Gitpod terminal to commit and push to GitHub.
- [GitHub](https://github.com/)
  - GitHub is used to store the projects code after being pushed from Git.
- [Django](https://www.djangoproject.com/)
  - Django was used as the primary framework for building the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  - Crispy Forms was used to render the comment form on the site.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html)
  - AllAuth was used for user authentication.
- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap was used for styling and responsiveness.
- [Cloudinary](https://cloudinary.com/)
  - Cloudinary is used for image hosting.
- [SQLite](https://www.sqlite.org/index.html)
  - SQLite was used as the database for development.
- [PostgreSQL](https://www.postgresql.org/)
  - PostgreSQL is used as the deployed database.
- [Heroku](https://id.heroku.com/login)
  - Heroku is used to host the application.
- [Gunicorn](https://gunicorn.org/)
  - Gunicorn is used for deploying the project to Heroku.
- [dbdiagram](https://dbdiagram.io/home)
  - dbdiagram was used to create the ERD.
- [Google Fonts](https://fonts.google.com/)
  - Google fonts was used to import the Play and Poppins fonts.
- [Font Awesome](https://fontawesome.com/)
  - Font Awesome was used to style instruction icons.
- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used to create wireframes for design purposes.
- [Image-Resizer](https://imageresizer.com/)
  - Image-Resizer was used to resize images.
- [TinyPNG](https://tinypng.com/) 
  - TinyPNG was used to compress image files.
  <br/><br/>

# **Testing**

The W3C Markup Validator, W3C CSS Validator Services, JSHint and PEP8 were used to validate the site to ensure there were no syntax errors in the project.

- [W3C Markup Validator](https://validator.w3.org/nu/) show no errors.
  - [.html](media/w3cvalidation/htmlvalid.png)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) show no errors.
  - [style.css](media/w3cvalidation/cssvalid.png)
- [PEP8](http://pep8online.com/) show no errors except lines being too long. 
  - [views.py](media/pep8/viewspep.png) 
  - [models.py](media/pep8/modelspep.png) 
  - [forms.py](media/pep8/formspep.png) 
  - [admin.py](media/pep8/adminpep.png) 
  - [urls.py](media/pep8/urlspep.png)
- [JSHint](https://jshint.com/)
  - [JSHint validator](media/jshint.png)
  <br/><br/>

Lighthouse

![Lighthouse](media/lighthouse.png)

<br/><br/>

## **Testing User Stories from User Experience (UX) Section**

### First Visit

- As a First Time User, I want to intuitively understand what the site is about.
  - When first visiting the site several elements point to the site subject.
    - The name and logo of the site is PlayBay, pointing to the connection with PlayStation®.
    - Posts on the site have an image which looks like the background theme of the PlayStation® console, or images uploaded based on the subject or game connected to the console.
    - Posts on the site have a label corresponding to the particular category of the post. The categories point to regular labels for game sites, like review and news. Party is a particular category linked to the "group chat" function of the console, again connecting it to PlayStation®.
    - The navigation bar has a slogan derived directly from PlayStation®, "Play Has No Limits", which is the slogan used for the current generation PlayStation® console.
<br/><br/>

### Navigation

- As a User, I want to intuitively understand how to navigate the site.
  - The navigation bar links at the top of the site have clear names for what they do. Post+ is the least obvious, but the target audience most likely understands it purpose.
  - The site redirects the user to the correct site based on input. If a user likes a post, the page simply reloads. If a user logs in, it redirects to the home page. If a user edits their post, they are redirected to the edited post.
- As a User, I want it to be clear where I am on the site.
  - The links in the navigation bar does not have an "active" state. Regardless, there are few pages and each one is sufficiently different as to not confuse anyone. Clicking "Login", for example, takes the user to a form, which is obviously not a post.
- As a User, I want to be able to search and filter posts based on category.
  - This not possible right now. It's a planned feature. Since there are only a few posts on the site as of now, this is not an immediate issue.
- As a User, I want to be able to search for post titles and content.
  - Same as above.
<br/><br/>

### Registration

- As a User, I want to be able to register an account so I can further interact with the site.
  - Registration is easy and only has username and password as required fields.
- As a User, I want to be able to add profile information about myself.
  - This is not possible right now. It's a planned feature. As the site grows, this would be an essential part of creating a community on the site.
<br/><br/>

### Site Interaction

- As a User, I want to be able to post entries.
  - When logged in, the navigation bar has a "Post+" link. The + sign is golden for added visibility. A user has to provide a category, title, excerpt and content. Images are optional.
- As a User, I want to be able to edit and delete posts created by me.
  - When logged in, the home page post list has en "Edit" button if the user is the author of the post. The detailed view of posts by the user has both "Edit" and "Delete" links. The "Edit" page has a form for editing the post except images. The "Delete" page has a big red button with a warning to the user.
- As a User, I want to be able to comment on posts.
  - When logged in, a user can comment on any posts via a form at the bottom of each post.
- As a User, I want to be able to like/upvote posts.
  - When logged in, a user can like or unlike posts. This is done on the particular post's page that you want to like/unlike.
<br/><br/>

### Admin

- Ad an Admin, I want to be able to manage users.
  - On the Admin page, I can create, read, update and delete users.
- As an Admin, I want to be able to manage posts.
  - On the Admin page, I can create, read, update and delete posts.
- As an Admin, I want to be able to manage comments.
  - On the Admin page, I can create, read, update and delete comments.
- As an Admin, I want to be able to add content specific related content, like categories.
  - On the Admin page, I can create, read, update and delete categories.
<br/><br/>

## **Manual Testing**

### **Navigation**

| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Site logo | Click "PlayBay" | Takes the user to the home page. | ✓ |
| Home | Click "Home" | Takes the user to the home page. | ✓ |
| Register | Click "Register" | Takes the user to register page. | ✓ |
| Register page | Click "Register" | If user registers, redirect to home  | ✓ |
| Login | Click "Login" | Takes the user to the login page. If user logs in, redirect to home. | ✓ |
| Login page | Click "Log in" | If user logs in, redirect to home. | ✓ |
| Logout | Click "Logout" | When logged in, takes the user to the logout page. | ✓ |
| Log out page | Click "Log out" | If user logs out, redirect to home. | ✓ |
| Post+ | Click "Post+" | When logged in, takes the user to the add post page. | ✓ |
| Post+ page | Click "Post!" | If user adds post, redirect to this post. | ✓ |
| Blog post | Click on a blog post | Takes the user to the specific post. | ✓ |
| Edit button/link | Click "Edit" | When logged in and author of specific post, the "Edit" button on home or link on blog post pages is displayed. | ✓ |
| Edit page | Click "Edit"| When logged in and author of specific post, clicking "Edit" on home or blog post pages takes the user to the Edit Post page. | ✓ |
| Edit post | Click "Edit" | Clicking "Edit" on the Edit Post page, redirect to this post. | ✓ |
| Delete link | Click "Delete" | When logged in and author of specific post, clicking "Delete" on blog posts is displayed. | ✓ |
| Delete page | Click "Delete" | When logged in and author of specific post, clicking "Delete" on blog posts takes the user to the Delete Post page. | ✓ |
| Delete post | Click "Delete" | Clicking "Delete" on the Delete Post page, redirect to home. | ✓ |
| Social | Click social media icon | Clicking an social media icon link in the footer redirects to the specific site. | ✓ |
| Unauthorized | Visit page unauthorized | Reaching an edit or delete page through URL manipulation for a specific post the user did not create, display information and a link to go back. | ✓ |

<br/><br/>

### **Features**

| Test    | Action          | Expected Result                                    | Pass |
| ------- | --------------- | -------------------------------------------------- | ---- |
| Like    | Click like icon | When clicked, increment/decrement like counter.     | ✓    |
| Comment | Comment         | Display comments with username and date of comment. | ✓    |


<br/><br/>

### **Validation**

| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Register | Form valid | If the form is valid, a success message notifying the user is displayed. | ✓ |
| Register | Form invalid | If the form is NOT valid, i.e required field not filled, wrong password format or duplicate username the user is notified of the error. | ✓ |
| Log in | Form valid | If the form is valid, a success message notifying the user is displayed. | ✓ |
| Log in | Form invalid | If the form is NOT valid, i.e required field not filled or wrong password, the user is notified of the error. | ✓ |
| Log out | Logging out | If the user logs out, a success message notifying the user is displayed. | ✓ |
| Post+ | Add form valid | If the form is valid, a success message notifying the user is displayed. | ✓ |
| Post+ | Add form invalid | If the form is NOT valid, i.e required field not filled or title already exist the user is notified of the error. | ✓ |
| Edit post | Edit form valid | If the form is valid, a success message notifying the user is displayed. | ✓ |
| Edit post | Edit form invalid | If the form is NOT valid, the user is notified of the error. | ✓ |
| Delete post | Deleting post | If the user deletes a post, a success message notifying the user is displayed. | ✓ |
| Comment | Comment form valid | If the form is valid, a success message notifying the user is displayed. | ✓ |
| Comment | Comment form invalid | If the form is NOT valid, the user is notified of the error. | ✓ |
| Message | Form/button validation | Display message when logging in/out, registering, commenting and adding, editing and deleting posts. | ✓ |
| Message JS | Form/button validation | Messages displayed should disappear automatically after 5 seconds. | ✓ |

<br/><br/>

### **Error Handling**

| Test | Action | Expected Result | Pass |
| ---- | ------------ | --------------- | ---- |
| 404 | Wrong URL | If page does not exist, display custom 404 page with information and link to go back. | ✓ |

<br/><br/>

## **Bugs**

### Fixed

[DetailView](media/bugs/pk_or_id.png)

- Django Generic DetailView must be called with either object pk or slug
  - Fix: Removed references to slugs for URLs and replaced with pk.

[Add comment](media/screenshots/add-comment.png)

- Adding a comment produced IntegrityError due to foreign key constraint due to changing fields in model
  - Fix: Add new ForeignKey field with a different name in Comment model, linking to User ID.

A couple small bugs concerning redirects were due to not referencing the correct URL path and pk.
<br/><br/>

### Remaining Found Bugs

- When clicking the like button and using the browser to go back, you have to click twice.
  <br/><br/>

# **Deployment**

## **Development**

1. Clone [this repository](https://github.com/JFrdrkssn/project4)
2. Install Python
3. Install Django and create an app using these commands in your terminal

        pip3 install Django==3.2 gunicorn
        django-admin startproject your_project_name .
        python3 manage.py startapp your_app_name
        pip3 install -r requirements.txt
        python3 manage.py makemigrations
        python3 manage.py migrate

- Make sure your INSTALLED_APPS in settings.py look like this:
    
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.sites',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'cloudinary_storage',
            'django.contrib.staticfiles',
            'cloudinary',
            'django_summernote',
            'crispy_forms',
            'your_app_name',
        ]

4. Create or log in to an account on Heroku
5. Create a new app on Heroku
6. Open your app on Heroku and go to Resources, Add-ons and search for PostgreSQL
7. Add PostgreSQL
8. In the Deploy section on Heroku, go to Deployment method and add your GitHub repository
9. Create or log in to an account on Cloudinary
10. Copy your API Environment Variable
11. Go back to Heroku, Settings and click on Reveal Config Vars
12. Add your Cloudinary API variable, SECRET_KEY and DISABLE_COLLECTSTATIC. PostgreSQL should already be there.
    - CLOUDINARY_URL | your_api_variable
    - SECRET_KEY | your_choice ([Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/))
    - DISABLE_COLLECTSTATIC | 1
13. Create an env.py in the root directory, add it to .gitignore and add these lines at the top

        import os

        os.environ["DATABASE_URL"] = "postgresql from your Heroku config vars"
        os.environ["SECRET_KEY"] = "your secret_key here"
        os.environ["CLOUDINARY_URL"] = "cloudinary url here"

14. At the top of your settings.py file, add these

        from pathlib import Path
        import os
        import dj_database_url
        from django.contrib.messages import constants as messages
        if os.path.isfile('env.py'):
            import env

15. Comment out DATABASES in your settings.py file and add this DATABASES below

        #DATABASES = {
        #   'default': {
        #       'ENGINE': 'django.db.backends.sqlite3',
        #       'NAME': BASE_DIR / 'db.sqlite3',
        #   }
        #}

        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }

16. In your settings.py file, make sure DEBUG is set to FALSE

        DEBUG = False

17. In your settings.py file, replace STATIC_URL with these lines

        STATIC_URL = '/static/'
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

18. In your terminal, run migrations

        python3 manage.py makemigrations
        python3 manage.py migrate

19. Create a superuser for your site

        python3 manage.py createsuperuser

20. Run your app locally

        python3 manage.py runserver
<br/><br/>

## **Production**

1. In your settings.py file, set DEBUG to True

        DEBUG = True

2. Add these to your settings.py file, just under DEBUG

        X_FRAME_OPTIONS = 'SAMEORIGIN'

        ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost']

        ACCOUNT_EMAIL_VERIFICATION = 'none'

3. On Heroku, go to Settings and Reveal Config Vars
4. Remove DISABLE_COLLECTSTATIC
5. On Heroku, go to Deploy and scroll down to choose whichever method to deploy you want
    - You can automatically deploy the app everytime your GitHub repository is updated
    - You can manually deploy the app
6. On Heroku, go to Settings and scroll down to Domains where you find the URL to your site
<br/><br/>


# **Credits**

## **Code**

- This project was made with Django's built in batteries-included functionality. The base layout and styling is from Code Institute's walkthrough blog project [GitHub](https://github.com/Code-Institute-Solutions/django-blog-starter-files). Some ideas and inspiration came from this Codemy Django blog series on [YouTube](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi).

## **Content**

- The structure and layout of this README.md was based on [this template](https://github.com/Code-Institute-Solutions/SampleREADME) by [Code Institute](https://codeinstitute.net/). Some text was also copied. Additional inspiration for this README.md was given from other templates in Code Institute's course curriculum and my mentor's previous student and alumnus Christopher Goodfellow and his [Tarmachan](https://github.com/Tawnygoody/Tarmachan) project.

## **Media**

- Angelo Abear on [Unsplash](https://unsplash.com/@angeloabear)
  - [Placeholder](https://unsplash.com/photos/knTKij60p3g) image for posts.
- [Psyonix](https://www.psyonix.com/) for the Rocket League image.
- [Polyphony Digital](https://www.gran-turismo.com/us/) for the Gran Turismo 7 image.
- [FromSoftware](https://www.fromsoftware.jp/ww/) for the Elden Ring image.
- [PlayStation Store](https://store.playstation.com/sv-se/category/ec9d8f57-3e46-454e-82df-5df7ded119a3?gclid=CjwKCAjw6dmSBhBkEiwA_W-EoFK5NY6jjBGOPWQOungzjHCEJE_m_70bsfjY6o-tN6ywQ2JYuEa2HRoCPhoQAvD_BwE&gclsrc=aw.ds) for the Spring Sale image.
- [Rockstar Games](https://www.rockstargames.com/) for the GTA Online image.

## **Acknowledgements**

- My Mentor, Gerard McBride, for continuous helpful feedback and support.
- [Stack Overflow](https://stackoverflow.com/) for all kinds of tips and tricks.