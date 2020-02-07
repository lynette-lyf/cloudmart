# E-Commerce Platform - Cloudmart
## Stream Four Project: Full Stack Frameworks with Django Milestone Project - Code Institute

This e-commerce platform is a food retailer that aims to specialize in selling popular snacks across the globe and shares the common functions of an e-commerce website which allows users to register or login to their account, browse the shop's catalog, view the details of the products, add or remove products from their cart or wishlist, checkout, make payments for their purchases and track their order.

## Demo
<a href="https://lyf-cloudmart.herokuapp.com/"><img src="https://media.giphy.com/media/kBZuVdQqTzYpfjRy42/giphy.gif"/></a>

##### A live demo can be found [here](https://lyf-cloudmart.herokuapp.com/).

##### To login as a test user:

`username: testuser`

`password: cloud123`

## UX

The overall design of the website follows a purple-pink colour palette that is consistent throughout the interface. Every page communicates its purpose clearly and does not stray too far from the generic e-shop layout which users - who frequently do online shopping, may find easy to use.

In the landing page, the user is greeted with an interactive hero image that encapsulates the title and slogan of the e-shop while capturing their attention as they move their cursor. They can then choose to access the shop via the call-to-action button and browse the products.

If the user attempts to perform an action, a notification would pop-up which informs the user that the action they are trying to complete is successful/unsuccessful.

Since performing certain actions (e.g. Checkout, View Cart, Add to Cart, Add to Wishlist) would require the user to login or register, users would be redirected to the login page and are prompted to login or register if they attempt to perform the actions without signing in.

Illustrations can also be found on majority of the pages as they are visual representations of expressing messages. They also help to elevate the website's aesthetics and improve the overall interface as a whole.

The website also takes on a mobile-first approach and is optimized for mobile viewing.

## User Stories

These are the user stories that highlights the requirements of each feature from an end-user perspective, for development purposes.

Users refer to web surfers, customers and potential customers. As a user...

`I want to browse the products by category, so that I can view a list of products filtered according to my selection.`

`I want the website to be mobile responsive, so I can view the website conveniently from my smartphone or tablet.`

`I would like to read the product description, so I  can know more about the product.`

`I want to add/remove a product to my cart, so I can continue shopping and collating my order before checking out.`

`I want to amend the quantity of products in my cart, so I can decide the amount to purchase.`

`I want to ensure that the payment function, account function and all data stored inside are secure, so that my sensitive information (e.g. passwords, credit card details) will not be vulnerable to cyber threats.`

`I would like to check my order status, so that I can be updated on the whereabouts of my order.`

Superusers refer to the e-commerce platform's administrator or business owner. As a superuser,

`I want to be able to create, read, update and delete information to the website's database, so that I can oversee and control the website's operations.`

`I would like the cart, wishlist and payment features to be member exclusive, so I can get more audiences to register an account with me.`

## Wireframes
<a href="https://www.figma.com/file/Khr3UTEU8X50Q1xMUwYyhk/Cloudmart-Wireframes?node-id=0%3A1"><img src="https://i.imgur.com/kaCO9es.png"/></a>

##### Click [here](https://www.figma.com/file/Khr3UTEU8X50Q1xMUwYyhk/Cloudmart-Wireframes?node-id=0%3A1) for preview

## Technologies
### Styling
1.	HTML/CSS
2.  Javascript
3.  jQuery
4.	Bootstrap (4.3.1)
5.  Materialize
6.  Crispy Forms
7.	Font Awesome (4.7.0)
8.	Google Fonts API
9. TweenMax (jQuery CDN)
10. Draggable (jQuery CDN)

### Framework
1.  Django 2 (2.2.4)
2.	Python (3.6)
3.	Jinja2 (2.10.3)

### Additional Plug-ins
1.  Stripe (Payments)
2.  Gunicorn (WSGI application server)
3.  Psycog2 (PostgreSQL database adapter for Python)
4.  Pillow (PIL fork)
5.  Django-mathfilters (Python module)

### Database
1. dbsqlite3
2. AWS S3
3. PostgreSQL

### Others
1. Figma (Wireframing tool)

## Features
#### 1. Landing page and overall feature:
**•	Parallax on cursor effect**

Found in the landing page, the interactive feature allows users to move their cursor around the page to toggle the parallax effect.

**•	Mobile responsive navbar**

The navigation bar collapses in mobile view and the 'burger' menu icon transitions into a 'X' close button upon toggling it in mobile view.

**•	Able to view number of carted items at the top of every page**

**•	Notifications appear on top of the page every time a certain action is made by the user**

#### 2. Accounts:
**•	Login/Logout**

**•	Register**

**•	Password Reset**

**•	Profile**

**•	Order tracking**

Able to view their account details, order transactions, order summary and wishlist

#### 3. Shop:
**•	View all products in the catalog or filter them by country**

**•	View individual product page with details and descriptions of the product**

**•	Add/Remove product to cart**

**•	Add/Remove product to wishlist**

#### 4. Cart:
**•	Able to increase or decrease the quantity of products in cart and remove the product from the cart**

#### 5. Wishlist:
**•	Wishlist items appear in the wishlist when the user has toggled the wishlist button via catalog or individual product page**

**•	Wishlist items will automatically be removed from the wishlist once the user has added it to their cart**

#### 6. Checkout:
**•	Delivery and Payment Form**

**•	Payment Gateway that accepts all forms of credit card payment via Stripe**

**•	Order Summary**

### Features Left to Implement
- Add pagination to catalog, transaction and wishlist page (e.g. Limit to 6 items per page)
- Add a product carousel that features 'Top Picks' to the landing page - which allows users to scroll through the products horizontally
- Add reviews for each product and allow users to post their review and ratings for each product
- Automated chat support feature

## Testing

All user actions (e.g add to cart, add to wishlist) works fine. All forms and their validations are working. Links are routed correctly. Ensured that elements can only be viewed by certain actions made by members and non-members - members have full access while the latter have partial. Members are restricted from the backend Django database and Admin(superuser) able to create, read, edit and delete models and metadata from the database. Stripe payment is on test mode and is able to capture the amount entered by a successful payment transaction.

To ensure compatibility and responsiveness, testing was done across multiple browsers such as Chrome, Firefox, Safari and Internet Explorer and on multiple android devices - Galaxy S5, Pixel 2, Pixel 2 XL and iOS devices - iPhone 5-X, iPad and iPad Pro.

## Deployment
This site is hosted using Heroku, deployed directly from the master branch and Github. The deployed site will update automatically upon new commits to the master branch.

To run locally, you can clone this repository directly into the editor of your choice by pasting `heroku git:clone -a lyf-cloudmart` into your terminal.

## Credits
### Media  
I do not own any of the content shown in this website. All gifs, open-sourced illustrations, background images and the product images and their description were taken from various websites.

### Acknowledgements

Responsive navbar tutorial by Youtuber [Dev Ed](https://www.youtube.com/watch?v=gXkqy0b4M5g&t=127s)

Parallax effect on cursor credits to CodePen user [GreenSock](https://codepen.io/GreenSock/pen/OeqgrZ)

Gradient background tutorial by Youtuber [DarkCode](https://www.youtube.com/watch?v=NnrBempao2M&t=169s)

Account form layout credits to CodePen user [Tirth Patel](https://codepen.io/T-P/pen/bpWqrr)

Shop cart layout inspired by Dribble user [Olia Gozha's design](https://dribbble.com/shots/5039057-Shopping-cart-V2)

Image hover effect credits to CodePen user [Naoya](https://codepen.io/nxworld/pen/ZYNOBZ) 

##### DISCLAIMER: This e-commerce platform is entirely fictional and resemblances in its name to actual companies, are entirely coincidental and thereafter do not aim to replicate them in any way. This is for educational use.