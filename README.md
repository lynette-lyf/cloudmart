# E-Commerce Platform - Cloudmart
## Stream Four Project: Full Stack Frameworks with Django Milestone Project - Code Institute

This e-commerce platform is a food retailer that aims to specialize in selling popular snacks from all over the world. These snacks are usually unavailable in many places except its country of origin, difficult to import or even have a short shelf-life. Hence, there is an increasing demand for these products. Currently, the shop only has products from Japan, Korea and Taiwan.

## Demo
<a href="https://gph.is/g/Z2dol6D"><img src="https://media.giphy.com/media/kBZuVdQqTzYpfjRy42/giphy.gif"/></a>

A live demo can be found [here](https://lyf-cloudmart.herokuapp.com/).

To login as a test user:

`username: testuser                                                                                                             password: cloud123`

## UX

The overall design of the website has different shades of purple and pink colours and has the same pixelated cloud background which syncs with the theme of the company. To keep things consistent, each component in the website has its own theme (e.g The accounts app comprising of the login/logout/register pages have the same theme, the user profile page comprising of the user's details, orders and wishlist have the same theme.) Each page does not stray too far from the generic e-shop layout which users - who frequently do online shopping, may find easy to use.

In the landing page, the user is greeted with an interactive hero image that encapsulates the title and slogan of the e-shop while capturing their attention as they move their cursor. They can then choose to access the shop via the call-to-action button and browse the products.

For any action that the user attempts to perform, a notification would pop-up which informs the user that the action they are trying to complete is successful/unsuccessful. This gives the user assurance.

Other than notifications, illustrations can also be found on majority of the pages as they are visual representations of expressing messages. They also help to elevate the website's aesthetics and improve the overall interface as a whole.

Since the e-shop only retails food commodities that cannot be found locally, it can appeal to these groups of people:
- People who have heard of the food product
- People who have heard of the food product and are unable to purchase them in their own country of residence
- People who have not heard of any of these food products but are interested in purchasing for their own consumption or as a gift
- People who have not heard of any of these food products but are only interested in browsing, discovering and knowing more about the unique food products from all over the world
- People who are going to travel to the countries listed in the shop and are only interested in browsing the shop as a reference for what food products to get at the country they were travelling to

The e-shop shares the common functions of an e-commerce website which allows users to register or login to their account, browse the shop's catalog, view the details of the products, add or remove products from their cart or wishlist, checkout, make payments for their purchases and track their order.

## Technologies
### Styling
1.	HTML
2.	CSS
3.  Javascript
4.  jQuery
3.	Bootstrap (4.3.1)
3.  Materialize
4.  Crispy Forms
8.	Font Awesome (4.7.0)
9.	Google Fonts API
10. TweenMax (jQuery CDN)
11. Draggable (jQuery CDN)

### Framework
1.  Django 2 (2.2.4)
4.	Python (3.6)
5.	Jinja2 (2.10.3)

### Additional plug-ins
1.  Stripe (Payments)
2.  Gunicorn (WSGI application server)
3.  Psycog2 (PostgreSQL database adapter for Python)
4.  Pillow (PIL fork)
5.  Django-mathfilters (Python module)

### Database
1. dbsqlite3
2. AWS S3
3. PostgreSQL

## Features
#### 1. Landing page and overall feature:
**•	Parallax on cursor effect**

Found in the landing page, the interactive feature allows users to move their cursor around the page to toggle the parallax effect.

**•	Mobile responsive navbar

The navigation bar collapses in mobile view and the 'burger' menu icon transitions into a 'X' close button upon toggling it in mobile view.

**•	Able to view number of carted items at the top of every page**

**•	Notifications appear on top of the page every time a certain action is made by the user**

#### 2. Accounts:
**•	Login**

**•	Logout**

**•	Register**

**•	Password Reset**

**•	Profile**

Able to view their account details, order transactions, order summary and wishlist

#### 3. Shop:
**•	View all products in the catalog or filter them by country**

**•	View individual product page with details and descriptions of the product**

**•	Add/Remove product to cart**

**•	Toggle 'Add to Wishlist' and 'Remove from Wishlist' button to Add/Remove product to the wishlist**

#### 4. Cart:
**•	Able to increase or decrease the quantity of products in cart and remove the product from the cart**

If the cart item has a remaining quantity of 1 and the user presses the decrease button, the cart item will just be deleted off the cart. If there are no items in the cart, a message will appear on the cart notifying the user that the cart is empty.

#### 5. Wishlist:
**•	Wishlist items appear in the wishlist when the user has toggled the 'Add to Wishlist' button**

**•	Wishlist items disappear from the wishlist when the user has added it to their cart**


#### 6. Checkout:
**•	Delivery and Payment Form**

**•	Payment Gateway that accepts all forms of credit card payment via Stripe**

### Features Left to Implement
- Improve the mobile and browser responsiveness of all pages
- Add a product carousel that features 'Top Picks' to the landing page - which allows users to scroll through the products horizontally
- Add reviews for each product and allow users to post their review and rate each product from 0 out of 5
- Automated chat support feature
- Fix invalid user or password error on login page

## Testing

All user actions (e.g add to cart, add to wishlist) are in working condition. All forms and their validations are working. Links are routed correctly. Ensured that elements can only be viewed by certain actions made by members and non-members - members have full access while the latter have partial. Members are restricted from the backend Django database and Admin(superuser) able to create, read, edit and delete models and metadata from the database. Stripe payment is on test mode and is able to capture the amount entered by a successful payment transaction.

To ensure compatibility and responsiveness, the site was tested across multiple browsers such as Chrome, Firefox, Safari and Internet Explorer and on multiple android devices - Galaxy S5, Pixel 2, Pixel 2 XL and iOS devices - iPhone 5-X, iPad and iPad Pro. Majority of the pages in the website are not mobile responsive hence the position of the layout will not be aligned properly. The website is best viewed on screens with widths >1200px. There is an error that shows up when the user logs in with an invalid user or password. This is addressed in 'Features Left to Implement' section of this documentation.

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

Image hover effects credits to CodePen user [Naoya](https://codepen.io/nxworld/pen/ZYNOBZ) 

**DISCLAIMER: This e-commerce platform is entirely fictional and resemblances in its name to actual companies, are entirely coincidental and thereafter do not aim to replicate them in any way. This is for educational use.**

