# Monkey. Mind.
This is an interactive meditation website geared to the fast pace professionals looking to tame their monkey mind. This app's features will help individuals focus, relax, and improve overall well-being.
With different categories and meditation selections, Monkey. Mind. has meditations and sound baths to suite everyone!
## Index:

- [Scope](#Scope)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Data Models](#data-models)
- [Milestones](#milestones)

## Scope

The final objective is to build an app where users can add meditations to their profile and complete them at their own leisure. Ultimately I would like to add my own database of actual meditations and create a meditation "to-do" list for the user based on what the user is mentally, emotionally, and physically feeling.

##### Technologies in play

- Python
- Django
- PostGreSQL
- Bootstrap4
- Canva
- Unsplash
- CSS
- HTML
  

## User Stories

Monkey. Mind. users are seeking out meditations based on different categories related to mental, physical, and emotional needs. The user will be able to make a meditation "to-do" list in their profile.

#### Non-authenticated Users can:

- View landing page
- Browse 
- Signin

#### Authenticated users can

- View landing page
- Browse
- Add meditations to profile
- View their profile page
- View their meditation history
- View past meditation history
- Can delete meditations in profile
- View meditation detail page
- Update their profile 

## Wireframes

### Landing

Users will see input to signin or browse
![image](https://user-images.githubusercontent.com/69656339/101191953-3534e380-360f-11eb-82bd-7f4461b918f9.png)
### Registration

Users who need to create will be guided to registration page
![image](https://user-images.githubusercontent.com/69656339/101192111-6f05ea00-360f-11eb-86e3-4a9a040c0056.png)
![image](https://user-images.githubusercontent.com/69656339/101192244-a5dc0000-360f-11eb-8a75-65417da535e8.png)
### Home Page

Build out city database/log individual articles, title, data, submit to memory.

This will allow user to input Article and comment data to database, as well as have access to edit past Articles and comments.  These articles will be visible with hyperlinks to view article and comment details
![image](public/images/landing.png)
### Show Article Page

Details each article by: (name, date/time, comments)

View 1
![image](public/images/article_view.png)
## Data Models

### User

- userId
- name
- email
- password
- imgURL
- joined on
- current city


### City

- name
- image


### Article

- title
- content
- created_on
- author (FK)
- city (FK)

### Comment

- name
- email
- body
- created_on
- article (FK)


