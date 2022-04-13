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