# FlavourNest - Milestone personal project


## Table of Contents

 1. [Overview](#overview)
     - [Purpose](#purpose)
     - [Target Audience](#target-audience)
 2. [User Stories](#user-stories)
     - [Must-Have User Stories](#must-have-user-stories)
     - [Should-Have User Stories](#should-have-user-stories)
     - [Could-Have User Stories](#could-have-user-stories)
 3. [Design Decisions](#design-decisions)
     - [Wireframes](#wireframes)
     - [Colours](#colours)
     - [Fonts](#fonts)
 4. [Features Implementation](#features-implementation)
     - [Core Features (Must-Haves)](#core-features-must-haves)
     - [Advanced Features (Should-Haves)](#advanced-features-should-haves)
     - [Optional Features (Could-Haves)](#advanced-features-should-haves)
 5. [Testing and Validation](#testing-and-validation)
     - [Testing Results](#testing-results)
         - [Bug Fixes](#bug-fixes)
         - [Responsiveness](#responsiveness)
         - [Lighthouse Performance Test](#lighthouse-performance-test)
     - [Validation](#validation)
 6. [Deployment](#deployment)
     - [Deployment Process](#deployment-process)
     - [File Structure](#file-structure)
 7. [AI Tools Usage](#ai-tools-usage)
     - [ChatGPT](#chatgpt)
 8. [Reflection on Development Process](#reflection-on-development-process)
 9. [Code Attribution](#code-attribution)
 10. [Future Improvements](#future-improvements)

## Overview

### Purpose


FlavourNest serves as a comprehensive destination for food lovers passionate about Mediterranean dishes. The website is designed with the following purposes in mind:
<ul>
<li>
Sharing Mediterranean Recipes:  FlavourNest provides a variety of authentic Mediterranean recipes, from classic dishes to modern interpretations, catering to various dietary needs and preferences.
</li>
<li>
Engaging Mediterranean Food Community:  to create a space where Mediterranean food lovers can interact, share their cooking experiences, rate recipes, contact each other and leave reviews to foster a community of food enthusiasts.
</li>
<li>
Inspiration for All Skill Levels: Whether you’re a beginner or an experienced chef, FlavourNest offers easy-to-follow recipes and cooking tips that help users expand their cooking skills and knowledge of Mediterranean cuisine.
</li>
<li>
Personalized User Experience: The website allows users to create personalized profiles and search recipes a tailored cooking experience.
</li>
<li>
Dietary Inclusivity: We recognize the importance of catering to a variety of dietary preferences, and thus, FlavourNest ensures that every user can find recipes that suit their needs—whether they're vegetarian, gluten-free, or following any other dietary regimen.
</li>
<li>
Responsive and Accessible: Designed with user experience in mind, FlavourNest is built to be fully responsive across all devices, ensuring that users can access recipes, tips, and the community on-the-go.
</li>
</ul>
<br/>

***Here's my deployed site :*** [FlavorNest](https://flavornest-7cb17784f79b.herokuapp.com/)

***Am I Responsive***

![IAMresponsivepic]( static/images/respo.jpg "flavournest")




### UX ### :
<br/>
For this recipe blog site. The user is meant to feel the ownership of the site. Each registered user has a profile, with a picture, his shared recipes , and a list of other users to be contacted.The User Profile has the same hero picture as a profile cover picture to keep up with the recurring theme.

FlavourNest colors are inspired by the ocean and the natural beauty of the Mediterranean. Ocean coral and ocean waves are perfect Mediterranean theme, as they evoke the feeling of the sea, fresh seafood, and coastal landscapes.

The site carrys a clean theme and the colors as nuetral as possible. One of the platform's main objectives is to share recipes with images. Images will have all different colors and composition therefore the need to reduce the noise and let the images be the focal point. The background body has been kept white with a blueish footer to frame the content, the crispy green tone of the navbar is to provide freshness and subtle to give the content precidence.

### Color Scheme ###
Hex: #FF6A3D -  Warm coral </br>
Hex: #1F6F8B -  Deep blue of ocean waves </br>
Hex:  #e59572 - Soft, earthy coral with hints of peach</br>
Hex: #FFFFFF -  White

***Colours Palettes***

<figure>
    <img src="static/images/ocean-pal.jpg"
         alt="Ocean colours palette">
    <figcaption>Ocean Waves Color Palette.</figcaption>
</figure>
<figure>
    <img src="static/images/ocean-coral.jpg"
         alt="Ocean colours palette">
    <figcaption>Ocean Coral Color Palette Color Palette.</figcaption>
</figure>



### Typography ###

<ol>
<li>Primary Font:
<ul>
<li>The ***'Roboto'*** font is used for the body text, ensuring readability with a clean, modern sans-serif style. This is a versatile and legible font that works well for both short and long text, making it perfect for the content-heavy blog.</li>
</ul>

<li>Font Weight and Sizes:
<ul>
<li>Headings and important text elements (such as .recipe-header, .cover-text h2, and .navbar-brand .brand) feature bold and larger font sizes to create clear visual hierarchy. The bold weights help emphasize key content like recipe titles and blog highlights, making them stand out to the reader.
</li>
<li>Subheadings and smaller text (like .cover-text p, .navbar-subtitle, and .star-rating .star) are given a lighter weight to provide contrast and guide the reader’s eye without overwhelming the layout.</li>
<li>Font sizes are adjusted responsively, scaling down for smaller screens, ensuring the design remains accessible and aesthetically pleasing across all devices.</li></ul>
<li>Heading Style:
<ul><li>
The main headings such as .recipe-header and .navbar-brand .brand are designed to capture attention with large font sizes, bold weights, and unique styling (such as the gradient background in .recipe-header). This creates an inviting atmosphere and ensures the key sections of the page are immediately noticeable.
</li></ul>
<li>Special Fonts:
<ul><li>
***'Mea Culpa*** is used for the blog’s brand title, providing a unique and personalized touch, fitting for the cultural and culinary context of a Mediterranean food blog.</li>
<li>The ***FontAwesome*** icon font is incorporated in the rating system (.star-rating), allowing for dynamic and interactive user elements such as stars for ratings.</li></ul>
<li>Text Alignment and Spacing:
<ul><il>
Text elements like .recipe-header and .cover-text are centered, providing symmetry and balance in key sections. Additionally, line-height and margin properties improve the readability of the content, ensuring the text isn't too cramped or difficult to read.</il></ul>
<li>Hover Effects:
<ul><il>
Links and buttons have interactive hover effects, changing color on interaction, such as in the .navbar a:hover and .btn:hover styles. These changes not only improve user experience but also create a dynamic visual flow as users navigate through the site.</il></ul>

<li>The favicon I made it using canvas</li></ol>


## User Stories
In total , there is 12 user stories. 10 of them have been completed, while two couldn't be accomplished due to the lack of time.
<figure>
    <img src="static/images/board.jpg"
         alt="board">
    <figcaption>Project Board</figcaption>
</figure>

### Must Have user stories 

 #### User Story name : Manage the Blog Posts
As a Site user I can create, read, update and delete posts so that I can manage my profile content


#### Acceptance Criteria 

1. **Create a Post:**
   - The Site user can create a new recipe post with a recipe_name, ingredients, image , instructions.
   - The post is published and visible on the homepage once approved.
   - The post can be categorized (e.g., breakfast, lunch, snacks).

2. **Update a Post:**
   - The Site user can update their posts, modifying the recipe_name, ingredients, image, or category.

3. **Delete a Post:**
   - The Site user can delete their post when necessary.

#### Tasks

##### 1. Design the Post Creation Form
   - The form should include input fields for:
     - Recipe Name
     - Ingredients
     - Instructions
     - Recipe Image
     - Cooking Time
     - Preparation Time
     - Category (e.g., Breakfast, Lunch, Vegan)
   - Form should allow file upload for images and provide validation for required fields.

### 2. Implement the Backend (Model)
   - **Create Recipe Model:**
     - Define a `Recipe` model with fields:
       - `recipe_name` (CharField)
       - `slug` (SlugField)
       - `ingredients` (TextField)
       - `instructions` (TextField)
       - `recipe_image` (ImageField)
       - `status` ((0, "Draft"), (1, "Published"))
       - `category` (ForeignKey to Category model)
       - `author` (ForeignKey to User)
     - Define a `Category` model with categories like `breakfast`, `lunch`, `vegan`, etc.
     - Add necessary relationships between models (e.g., Recipe-Category, Recipe-User).

### 3. Create the View for Post Creation
   - Handle both GET and POST requests for creating a post.
   - On POST, the data is saved to the database, with a default status of 'not approved' until approved by an admin.
   - Redirect to the post list page or show a success message after the post is saved.

### 4. Display Posts on the Homepage
   - **View to Fetch and Display Posts:**
     - Show only posts where `status = 'published'` and are approved.
     - Display posts with basic details: title, category, and a thumbnail image.

### 5. Create Recipe Detail Page
   - **View to Display Recipe Details:**
     - Show full content of the post with recipe details like ingredients and instructions.
     - Display the post image and show the author's name.

### 6. Category Filter on Recipe Page
   - **Category Filter:**
     - Allow users to filter recipes by categories like `breakfast`, `lunch`, or `vegan`.
     - This can be implemented using a dropdown or clickable category filters at the top of the recipes page.

### 7. Implement Edit Recipe Form
   - **Create Edit View:**
     - If the logged-in user is the author of the post, they should have the option to edit the post.
     - The form should pre-fill the current post’s data and allow editing of the title, content, image, and category.

### 8. Add an Edit Button on Recipe Detail Page
   - **Edit Button Visibility:**
     - Display an "Edit" button only for the author of the post.

### 9. Create a View to Handle Updating Recipes
   - **Update Recipe View:**
     - Allow the author to update their post using a form (pre-filled with current data).

### 10. Add a Delete Button on the Recipe Detail Page
   - **Delete Button Visibility:**
     - Display a "Delete" button only for the author of the post.
     - When clicked, the post should be deleted from the database.

### 11. Post Default Status on Creation
   - When a post is created, it is set to `draft` by default until it is approved by an admin.

### 12. Admin Interface for Approval/Rejecting Posts
   - Create an admin interface to approve or reject posts based on the admin's review.
   - Admins can change the `status` of a post to `approved` or `rejected`.

### 13. Design UI for Post Creation, Update, and Delete Pages
   - Ensure that the pages for creating, editing, and deleting posts are intuitive and user-friendly.
   - Provide clear forms with validation and appropriate success/error messages.

### 14. Perform Manual Testing of the Entire Workflow
   - Test the process of creating, reading, updating, and deleting posts from the perspective of a site user.
   - Test admin approval/rejection process to ensure posts are correctly displayed when approved.
   - Test category filtering to ensure users can view posts by specific categories.

## User Story: "As a site user, I can click on a recipe name so that I can read the full recipe content"

### Acceptance Criteria:
- When a blog post recipe title is clicked on, a detailed view of the post is seen.
- User can print the recipe.

---

### Tasks:

1. **Create Recipe Detail View:**
   - Implement a view in Django that fetches the full recipe based on the recipe ID or slug.

2. **Design Recipe Detail Page:**
   - Display the full content of the recipe:
     - Title
     - Ingredients
     - Instructions
     - Image
     - Category

3. **Add a Print Button:**
   - Add a button or link on the recipe detail page to allow the user to print the recipe.

4. **Ensure Proper URL Mapping:**
   - Define a URL pattern for the recipe detail page, passing the recipe ID or slug in the URL to fetch the correct recipe.

5. **Add Styling for Print-Friendly Version:**
   - Implement a print-friendly layout that ensures the recipe is displayed properly when printed.

6. **Test Recipe Detail and Print Functionality:**
   - Verify that clicking on a recipe title redirects the user to the correct recipe detail page.
   - Test the print button functionality to ensure the recipe can be printed correctly.
***Wireframes***

<p>To follow best practice, using Bootstrap (which is mobile-first), I decided to create the mobile wireframe, and then scale it up for larger screens.</p>

Balsamiq

Mobile Wireframes
 <figure>
    <img src="static/images/wireframe.png"
         alt="Ocean colours palette">
    <figcaption>Mobile WireFrame.</figcaption>
</figure>

The navigation bar is available on all the website pages. It is fully responsive and provides links to all the areas of the website, some links based on whether the user is authenticated and logged in or not. Users are able to navigate on any size device with a burger menu with dropdown for small devices. users can easily click on the site logo to returnm back to the landing page.

Desktop

image

image

Mobile

image

image

Landing Page

The landing page has a carousel of 3 images taking up 3/4 of the page. These are images of photographers at work to depict what the site is about. There is an overlay of text on each that gives the purpose of the website and photography qoutes that encourage the users to sign up. The other 1/4 is taken up by three cards that explain the 3 purposes of the site, to showcase their work, provide andn or receive peer review and access information in the photography industry.

image

The Footer

The footer like the navbar is accessible on all pages of the website. On this section users can access the social sites of the website. Users have the choice to follow the blog on any of the social medis sites for any news, new implementaions announcements of future features and any updates on the newletter. Users can use these links to contact admin with any feedback and or suggestions.

image

Articles

The articles section is where users can find , view and read all the articles uploaded on the site. The user can only see a snippet of the articles in this section.

Articles are saved in categories. Users can use the search feature to narrow down on the category they are interested in.

Users can still however browse through all the articles , they have a choice to make a mental note of the articles that intrigue them using the pagination feature. Articles are displayed 6 per page.

Once a user has seen an article they like , they can click on it to view the whole article.

At the bottom of every article there is a review section. Only authenticated and logged in users can view the full article and have access to review the article

Users get a message when they've successfully sent a review

Users can see how many reviews each article has at a glance.

image

image

image

image

image

image

image

Dashboard

The Dashboard is only accessible to authenticated logged in users. This is an area where each user can see their own posted articles. In this section they are able to edit and or delete any of their articles.

Users get a message each time they successfully edit and or delete an article.

Users get a prompt message if they really want to delete. This is everytime they delete an article to give them a chance to change their mind if need be.

There is an all articles button at the top of this page for easy navigation for the user to go back to view all articles on the site.

image

image

image

Newsletter

The Newsletter provides an opportunity to promote photography services, products, workshops, or other offerings to the audience. The users can benefit from carefully curated industry content that is engaging and informative.

image

Signup

Signup page allows the users to register and join the aperture adventurers site.

This allows the user to be able to post articles as well as send reviews on other people's work.

User's get a message pop up letting themn know they have successfully signed up.

image

image

LogIn

This page allows already authenticated users to log into the site and access their dashboard as well as read and review other articles on the site.

Users get message to let then know theyve succesfully logged in

The logIn will then change to logout once the user is successfully loggedin.

The user gets a prompt message if they are sure they want to log out , before getting a message they have successfully logged out if they complete the process.

image

image

Create Article

This page is a form to create and post an article, it is only accessible to authenticated logged in users.

Here the user's can upload their Image , there are fields availalble for the user to state what equipment they used in taking the image and the settings they had on their camera.

Category has a dropdown list to choose from.

In the discription the user gets to explain what they were trying to achieve how they have got there if succesful , or they can ask their peers on what else the could have done top achieve this.

Once sent users get a message , their article has been posted successfully

image

image

image

Future Features
User Profiles

Users to have custom user profiles where they can list there accomplishments in photography and share their social media platforms.

Users will have CRUD functionality and autonomy on their profiles

Users to be able to add profile images for a more personal feel.

Reviews

Users to have added CRUD functionality on their reviews.

Users to be able to like articles as well as review them.

Direct Messaging

Users can direct message each other , requesting collaborations or seeking advise for a photo shoot privately.

Tools and Technologies used
Markdown Builder used to generate README and TESTING templates.
Git used for version control. (git add, git commit, git push)
Git used for secure online code storage.
Gitpod used as a cloud-based IDE for development.
HTML used for the main site content.
CSS used for the main site design and layout.
Python used as the back-end programming language.
Heroku used for hosting the deployed back-end site.
Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
Django used as the Python framework for the site.
PostgreSQL used as the relational database management.
PostgreSQL by Code Institute used as the Postgres database from Code Institute.
Cloudinary used for online static file storage.
WhiteNoise used for serving static files with Heroku.
Balsamiq used for creating wireframes.
Font Awesome used for the icons.
ChatGPT used to help debug, troubleshoot, and explain things.
Database Design
Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

Site used for ERD

Lucidchart

image

Agile Development Process
GitHub Projects
GitHub Projects

GitHub Projects is the Agile tool used for this project.

It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

image

image

GitHub Issues
GitHub Issues

This as an another Agile tool.

There, I used my own User Story Template to manage user stories.

It also helped with milestone iterations on a weekly basis.

Open Issues GitHub issues

Closed Issues GitHub closed issues

image

MoSCoW Prioritization
I've decomposed my Epics into stories prior to prioritizing and implementing them. Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

Must Have: guaranteed to be delivered (max 60% of stories)
Should Have: adds significant value, but not vital (the rest ~20% of stories)
Could Have: has small impact if left out (20% of stories)
Won't Have: not a priority for this iteration
Testing
[!NOTE]
Return back to the README.md file.

Feature-by-Feature Testing:

Navigation: Testested for smooth transitions between pages, links directing to the correct destinations.
Responsive Design: Checked for compatibility across various devices and screen sizes.
SS

Portfolio Display: Articles are properly showcased with accurate descriptions, images, and links.

Contact Forms: Tested the form submission process, ensuring the user receives a confirmation.

SS

User Experience Testing:

Usability Testing: Family memebers interacted with the site and provided feedback. Log out confirmation was missing a cancel option. A cancel button thst links back ti the home page was added.

Accessibility Testing: All images and links have well labeled alt text for screen reader compatibility compliance.

Compatibility Testing:

Browser Compatibility: Testing applied on different browsers (Chrome, Firefox, Safari,) to ensure consistent performance.
SS

Device Compatibility: EnsurED Functionality across various devices (desktops, laptops, tablets, and mobile phones).
SS

User Feedback Incorporation:

Color contrast user feedback has been taken into account and implemented to enhance the user experience. Text in article description has been changed from gray to black.

Code Validation
HTML
I have used the recommended HTML W3C Validator to validate all of my HTML files.

Directory	File	Screenshot	Notes
article	article-details.html	image	
article	index.html	image	
article	new-article.html	image	
article	reviews.html	image	
article	delete.html	image	
dashboard	dash.html	image	
mainhub	main.html	image	
newsletter	news.html	image	
CSS
I have used the recommended CSS Jigsaw Validator to validate all of my CSS files.

Directory	File	Screenshot	Notes
static	custom.css	image	
Python
I have used the recommended PEP8 CI Python Linter to validate all of my Python files.

Directory	File	CI URL	Screenshot	Notes
article	admin.py	PEP8 CI	image	
article	forms.py	PEP8 CI	image	
article	models.py	PEP8 CI	image	
article	urls.py	PEP8 CI	image	
article	views.py	PEP8 CI	image	
dashboard	admin.py	PEP8 CI		not used
dashboard	models.py	PEP8 CI		not used
dashboard	urls.py	PEP8 CI	image	
dashboard	views.py	PEP8 CI	image	
mainhub	admin.py	PEP8 CI		not used
mainhub	models.py	PEP8 CI		not used
mainhub	urls.py	PEP8 CI	image	
mainhub	views.py	PEP8 CI	image	
manage.py	PEP8 CI	image	
newsletter	admin.py	PEP8 CI		not used
newsletter	models.py	PEP8 CI		not used
newsletter	urls.py	PEP8 CI	image	
newsletter	views.py	PEP8 CI	image	
photography	settings.py	PEP8 CI	image	
photography	urls.py	PEP8 CI	image	
Browser Compatibility
I've tested my deployed project on multiple browsers to check for compatibility issues.

Browser					Notes
Chrome	image	image	image	Works as expected	
Firefox	image	image	image	Works as expected	
Safari	image	image	image	Works as expected	
Responsiveness
I've tested my deployed project on multiple devices to check for responsiveness issues.

Notes
Mobile (DevTools)	image	image	image	Works as expected	
Tablet (DevTools)	image	image	image	Works as expected	
Desktop	image	image	image	Works as expected	
Lighthouse Audit
I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

Page	Mobile	Desktop	Notes
image	image	Some minor warnings
Defensive Programming
Page	User Action	Expected Result	Pass/Fail	Comments
Home				
Click on Logo	Redirection to Home page	Pass	
Click on Home link in navbar	Redirection to Home page	Pass	
Gallery				
Click on Gallery link in navbar	Redirection to Gallery page	Pass	
Load gallery images	All images load as expected	Pass	
Contact				
Click on Contact link in navbar	Redirection to Contact page	Pass	
Enter first/last name	Field will accept freeform text	Pass	
Enter valid email address	Field will only accept email address format	Pass	
Enter message in textarea	Field will accept freeform text	Pass	
Click the Submit button	Redirects user to form-dump	Pass	User must click 'Back' button to return
Sign Up				
Click on Sign Up button	Redirection to Sign Up page	Pass	
Enter valid email address	Field will only accept email address format	Pass	
Enter valid password (twice)	Field will only accept password format	Pass	
Click on Sign Up button	Asks user to confirm email page	Pass	Email sent to user
Confirm email	Redirects user to blank Sign In page	Pass	
Log In				
Click on the Login link	Redirection to Login page	Pass	
Enter valid email address	Field will only accept email address format	Pass	
Enter valid password	Field will only accept password format	Pass	
Click Login button	Redirects user to home page	Pass	
Log Out				
Click Logout button	Redirects user to logout page	Pass	Confirms logout first
Click Confirm Logout button	Redirects user to home page	Pass	
Profile				
Click on Profile button	User will be redirected to the Profile page	Pass	
Click on the Edit button	User will be redirected to the edit profile page	Pass	
Click on the My Orders link	User will be redirected to the My Orders page	Pass	
Brute forcing the URL to get to another user's profile	User should be given an error	Pass	Redirects user back to own profile
repeat for all remaining pages	x	x	x	x
User Story Testing
User Story	Screenshot
As a new site user, I would like to view the articles, so that I can read and learn.	image
As a new site user, I would like to review a peer article, so that I can make a contribution to the site .	image
As a new site user, I would like to create an article, so that I can have feedback from other users.	image
As a returning site user, I would like to edit and delete my articles, so that I can manage my own content.	image
As a new site user, I would like to signup to the site, so that I can read articles and post my own.	image
As a returning site user, I would like to log in, so that I can see my posted articles.	image
As a site user, I should be able to logout, so that I can keep my account secure.	image
As a site administrator, I should be able to access all articles, so that I can review and manage site.	image
As a site administrator, I should be able to share news in the photography industry, so that I can keep users well informed.	image
Deployment
The live deployed application can be found deployed on :

Heroku.

PostgreSQL Database
This project uses a Code Institute PostgreSQL Database.

To obtain my own Postgres Database from Code Institute, I followed these steps:

Signed-in to the CI LMS using my email address.
An email was sent to me with my new Postgres Database.
[!CAUTION]

PostgreSQL databases by Code Institute are only available to CI Students.
You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
Code Institute students are allowed a maximum of 8 databases.
Databases are subject to deletion after 18 months.
Cloudinary API
This project uses the Cloudinary API to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

For Primary interest, you can choose Programmable Media for image and video API.
Optional: edit your assigned cloud name to something more memorable.
On your Cloudinary Dashboard, you can copy your API Environment Variable.
Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.
Heroku Deployment
This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
From the new app Settings, click Reveal Config Vars, and set your environment variables.
[!IMPORTANT]
This is a sample only; you would replace the values with your own if cloning/forking my repository.

Key	Value
CLOUDINARY_NAME	user's own value
CLOUDINARY_API	user's own value
CLOUDINARY_SECRET	user's own value
DB_URL	user's own value
DISABLE_COLLECTSTATIC	1 (this is temporary, and can be removed for the final deployment)
SECRET_KEY	user's own value
Heroku needs three additional files in order to deploy properly.

requirements.txt
Procfile
runtime.txt
You can install this project's requirements (where applicable) using:

pip3 install -r requirements.txt
If you have your own packages that have been installed, then the requirements file needs updated using:

pip3 freeze --local > requirements.txt
The Procfile can be created with the following command:

echo web: gunicorn app_name.wsgi > Procfile
replace app_name with the name of your primary Django app name; the folder where settings.py is located
The runtime.txt file needs to know which Python version you're using:

type: python3 --version in the terminal.
in the runtime.txt file, add your Python version:
python-3.9.18
For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

Select Automatic Deployment from the Heroku app.
Or:

In the Terminal/CLI, connect to Heroku using this command: heroku login -i
Set the remote for Heroku: heroku git:remote -a app_name (replace app_name with your app name)
After performing the standard Git add, commit, and push to GitHub, you can now type:
git push heroku main
The project should now be connected and deployed to Heroku!

Local Deployment
This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the requirements.txt file.

pip3 install -r requirements.txt.
You will need to create a new file called env.py at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

[!IMPORTANT]
This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample env.py file:

import os

os.environ.setdefault("CLOUDINARY_NAME", "user's own value")
os.environ.setdefault("CLOUDINARY_API", "user's own value")
os.environ.setdefault("CLOUDINARY_SECRET", "user's own value")
os.environ.setdefault("DB_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

Start the Django app: python3 manage.py runserver
Stop the app once it's loaded: CTRL+C or ⌘+C (Mac)
Make any necessary migrations: python3 manage.py makemigrations
Migrate the data to the database: python3 manage.py migrate
Create a superuser: python3 manage.py createsuperuser
Load fixtures (if applicable): python3 manage.py loaddata file-name.json (repeat for each file)
Everything should be ready now, so run the Django app again: python3 manage.py runserver
Cloning
You can clone the repository by following these steps:

Go to the GitHub repository
Locate the Code button above the list of files and click it
Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
Open Git Bash or Terminal
Change the current working directory to the one where you want the cloned directory
In your IDE Terminal, type the following command to clone my repository:
git clone https://github.com/shar-nm/lens-whisperer.git
Press Enter to create your local clone.
Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

Open in Gitpod

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed. A tutorial on how to do that can be found here.

Forking
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

Log in to GitHub and locate the GitHub Repository
At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
Once clicked, you should now have a copy of the original repository in your own GitHub account!
Local VS Deployment
Local development environment has different configuration settings compared to the live deployment environment on Heroku. This includes database configurations, static file serving settings, debug mode, logging configurations
Configuration settings and sensitive information such as database credentials, API keys, and secret keys are stored as environment variables in production environments in Heroku. In local env settings files and environment variables are stored locally during development.
Heroku serves static files (CSS, JavaScript, images) using WhiteNoise or by integrating with a content delivery network (CDN). In local environment, Django's development server handles static files differently.
Heroku provides security measures such as HTTPS support, automated security updates, and platform-level security features. These are not be present or configured in local development environment.
Credits
CI Blog
SteinOveHelset
Codemy
Content
ChatGPT 3.5
Adobe Creative Cloud
Source	Location	Notes
Markdown Builder	README and TESTING	tool to help generate the Markdown files
Chris Beams	version control	"How to Write a Git Commit Message"
W3Schools	entire site	responsive HTML/CSS/JS navbar
StackOverflow	troubleshooting	Authentication in django
YouTube	CRUD	tutorial for adding, viewing, updating and deleting items with django the Python
strftime	CRUD functionality	helpful tool to format date/time from string
WhiteNoise	entire site	hosting static files on Heroku temporarily
Bootstrap 5.3	entire site	responsivenes and CSS
Media
Source	Location	Type	Notes
Pixabay	articles page	image	group of photos for articles
Freepix	entire site	images	photos used thorough out the site
Freepix,lookstudio	newsletter	image	image used in the newsletter
Freepix,rawpixel.com	newsletter	image	image used in the newsletter
Acknowledgements
I would like to thank my Code Institute mentor, Tim Nelson for his support throughout the development of this project.

I would like to thank the Code Institute tutor team for their assistance with troubleshooting and debugging some project issues.
I would like to thank the Code Institute Gwent-Bootcamp for the moral support; it kept me going during periods of self doubt and imposter syndrome.
I would like to thank my partner (Michael), for believing in me, and allowing me to make this transition into software development.
I would like to thank my daughter (Nicole), for supporting me by doing all the user testing and proof-reading therefore supporting me through this career change towards becoming a software developer.
