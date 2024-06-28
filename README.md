# [Jolie Mimi Boutique](https://jolie-mimi-boutique-ad3e13f83c61.herokuapp.com/)
<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/f1dfc90f-5e31-4d60-bbb4-149347e985e1" alt="Jolie Mimi Boutqique">
</div>

## About
 [Jolie Mimi Boutique](https://jolie-mimi-boutique-ad3e13f83c61.herokuapp.com/)is an ecommerce platfom as a ladies' boutique, dealing with the latest, chick and trendy clothes alongside some jewellery items, developed on Django. It encompasses user registration, profile management, newsletter subscriptions, and product purchases facilitated by Stripe. Users of Jolie Mimi Boutique can submit their reviews about the products they have bought or want to buy. Frontend admin controls empower easy management of products and users. In addition, the website has a functionality that is a live chat, this live chat can be controlled by the shop owner/staff and could be limited to one or more staff depending on the average number of customers serving. Via this chat facility customer can interact with the customer care/sales staff to get instant help before buying any product or service provided by the website.

---

# E-commerce website

**Deployed website: [Link to website](https://jolie-mimi-boutique-ad3e13f83c61.herokuapp.com/)**


![Main image](readme-images/main-page.jpeg)

**Card number for payment testing: 4242424242424242**
 

## Table of Contents
1. <details open>
    <summary><a href="#ux">UX</a></summary>

    <ul>
    <li><details>
    <summary><a href="#goals">Goals</a></summary>

    - [Visitor Goals](#visitor-goals)
    - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    </details></li>

    <li><details>
    <summary><a href="#visual-design">Visual Design</a></summary>

    - [Wireframes](#wireframes)
    - [Fonts](#fonts)
    - [Colors](#colors)
    </details></li>

     <li><details>
    <summary><a href="#agile-development">Agile Development</a></summary>

    - [Milestones](#project-milestones)
    - [Progression](#project-progression)
    </details></li>

    </ul>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#site-pages">Site Pages</a></summary>

    - [Homepage](#homepage)
    - [Newsletter Subscription Popup](#newsletter-subscription-popup)
    - [Footer](#footer)
    - [Product List](#product-list)
    - [Product Detail](#product-detail)
    - [Contact Page](#contact-page)
    - [FAQ Page](#faq-page)
    - [Profile Page](#profile-page)
    - [Cart Page](#cart-page)
    - [Toasts Including Bag Preview](#toasts-including-bag-preview)
    - [Product Management](#product-management)
    - [Checkout](#checkout)
    - [Checkout Success](#checkout-success)
    - [Authentication Pages](#authentication-pages)    
    </details></li>

    <li>
    <a href="#features-not-yet-implemented">Features Not Yet Implemented</a>
    </li>
    </ul>
</details>

3. <summary><a href="#technologies-used">Technologies Used</a></summary>

4. <summary><a href="#webhooks">Webhooks</a></summary>

5. <summary><a href="#database-design">Database Design</a></summary>

6. <summary><a href="#ecommerce-business-model">Ecommerce Business Model</a></summary>

7. <summary><a href="#search-engine-optimization-and-social-media-marketing">Search Engine Optimization And Social Media Marketing
</a></summary>

8. <summary><a href="#testing">Testing</a></summary>

9. <a href="#deployment">Deployment</a>

10. <a href="#credits-and-acknowledgements">Credits and Acknowledgements</a>

----

# UX

The website was created to be eye-catching and user-friendly. The user is given plenty of choices to choose from when they are shopping. The emphasis is on the user experience; the user can navigate the website easily to fulfill users' goals. The website is designed to be easy to use and easy to understand. Additionally, the website attracts customers to become a part of loyalty programs by giving them additional discounts on their purchases.
It also handles all personnel functionality moving from admin to manager to logistics to other personnel.
Business goals were to make the website as scalable as possible and reusable in the real world so that the store personnel could use it according to their position in the company.

## Goals
### Visitor Goals

Target Audience (Two different cultures):

Our online boutique, where elegance meets empowerment! We pride ourselves on offering a curated selection of the latest fashion trends to make every woman feel confident and stylish. From chic dresses perfect for a night out to sophisticated workwear that commands attention, our collection caters to ladies and young girls who seek to express their unique personalities through fashion. Our easy-to-navigate website ensures a delightful shopping experience from the comfort of your home, where you can explore, browse, and discover pieces that resonate with your style. Join us online, where fashion dreams come true and every outfit tells your story. This website may hold many products, and it is essential to make sure that the website is easy to use and navigate. It is also a platform where two cultures join together which means not only Western but even Indian clothes can also be purchased from the same website.
 
User Goals:

- Find and purchase top-quality fabric, latest, trendy, chic, dresses and jewellery.
- Easy checkout, safe & secure payment payment option. 
- Stay informed about the latest trends, tips, and news in the fashion industry.
- Easily navigate the website to discover relevant products and content.
- Customize their profiles and engage with other customers through recommendations, reviews, and likes


### Business Goals

- Develop a dynamic and interactive e-commerce platform that offers a seamless shopping experience for women of all ages, emphasizing convenience and quality.
-Drive consistent traffic by providing engaging features beyond product listings, such as interactive forums and customer care resources, fostering a thriving online community.
- Maintain a regular cadence of product updates and promotions to keep users engaged and coming back for new offerings.
- Establish Jolie Mimi Boutique as a trusted authority in the fashion industry by curating and showcasing only high-quality products from reputable brands, ensuring customer satisfaction and loyalty.
- Implement strategies to highlight top-selling products, user favorites, and exclusive deals, driving sales and potentially attracting partnerships with leading garments suppliers or brands.

### User Stories

All user stories can be found in the linked GitHub project [here](https://github.com/users/Mr-KulwinderSingh/projects/8)

## Visual Design
### Wireframes

All wireframes can be found via this link to the GitHub folder [here](https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/tree/main/readme-images/wireframes)

### Fonts

- **Logo:** 
**[Nunito](https://fonts.google.com/specimen/Nunito?query=Nunito):** Nunito is an impactful display font that adds a rebellious vibe to an e-commerce platform. With its simple & clear appearance, Nunito commands smoothness and makes a clear statement, perfect for conveying a sense of activism or boldness in the design. Its distinct letterforms and unique style give to the project a standout aesthetic, while still maintaining legibility for titles and description.

**[Jaini](https://fonts.google.com/?preview.text=Jolie-Mimi-Boutique&query=Jaini):** Jaini is a font that can suit any type of logo, but its unique and mixed italic style makes the name Jolie Mimi Boutique look more elegant and clear, adding to its sophistication. 
Both Protest Strike and Dancing Script were used for my logo - they excellently contrast each other. 

**[Sans-serif]** Choosing sans-serif as the backup ensures universal legibility,especially on screens and digital platforms. Sans-serif fonts are known for their clarity and readability, making them a reliable fallback option in case any issues arise with the primary or secondary font choices. I also used cursive as the backup font for Dancing Script in the logo. 



### Colors

<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/3fbf3f1d-e495-48e4-8fe2-89d52bf110e6" alt="colors">
</div>

In crafting the color palette for this project, I aimed to strike a perfect balance between vibrancy, clarity, and visual appeal. Let's delve into why each color was carefully chosen:

- **Off Pink (#e12656) for the Logo**: Off Pink, kind a fushia colour is a bit unique and girlish colour which suits the best for our ladies' fashion boutique, being a classic and glossy look provides a strong combination of our logo and the delivery banner and follow the line down to shop now button. Its timeless appeal ensures that our brand identity stands out boldly against lighter backgrounds, guaranteeing excellent readability and visibility. Plus, base pink exudes professionalism and sophistication, aligning perfectly with our brand's ethos.
    
- **White (#FFFFFF) for the Background**: White serves as the canvas upon which all other colors and content come to life. Its clean and neutral nature creates a sense of spaciousness and cleanliness, enhancing readability and user experience. A white background exudes simplicity and elegance, perfectly complementing various design styles.
    
- **Yellow (#ffc107) for Buttons, messages background**: #ffc107 is a darker shade of yellow. It carries a rich and deep tone that exudes sophistication and depth. This color combines the vibrancy of yellow with the calming qualities, resulting in a hue that is both bold and grounded.
    

In essence, our color palette embodies simplicity and vibrancy, creating a visually appealing and user-friendly experience. The combination of classic pink, pristine white, and lively yellow forms a cohesive design that effectively communicates our brand's message. This palette also allows our vibrant product and brand name to shine, creating a dynamic and engaging platform for our audience.

## Agile Development

The journey of Jolie Mimi Boutique began with the establishment of a GitHub Projects Page, serving as the central hub for project management. This platform played a pivotal role in organizing tasks systematically, creating user stories, and breaking them down into actionable steps. The overarching goal was to create a structured roadmap that would guide the project towards successful completion within the designated timeframe. Utilizing the GitHub Projects Page enabled the tracking of the project's evolution, assignment of tasks, and achievement of milestones, ensuring a smooth and organized development process. The MoSCoW method, alongside customized GitHub project labels, was instrumental in assisting me in prioritizing essential tasks within the constraints of my available time.

To view the:

* project Kanban board, issues [please follow this link.](https://github.com/users/Mr-KulwinderSingh/projects/8)

### Project Milestones

The project was divided into several key milestones, each representing a significant phase in the development process. Within each milestone, epics were identified, representing broader themes or features to be implemented. These epics were further broken down into user stories, representing specific functionalities or requirements from the user's perspective. Finally, tasks were defined within each user story, representing the individual steps needed to fulfill the user story's objectives.

### Example Milestones, Epics, User Stories, and Tasks (Not Representative of the Actual Project):

1. **Milestone 1: Project Setup**
    
    - Epic 1: Repository Setup
        - User Story 1: Initialize Git repository
            - Task 1: Create repository on GitHub
            - Task 2: Clone repository locally
        - User Story 2: Setup Development Environment
            - Task 1: Install necessary dependencies
            - Task 2: Configure project settings
2. **Milestone 2: User Authentication**
    
    - Epic 2: User Registration
        - User Story 3: Allow users to register for an account
            - Task 1: Create user registration form
            - Task 2: Implement backend logic for user registration
        - User Story 4: Enable email verification for new accounts
            - Task 1: Generate verification email upon registration
            - Task 2: Implement email verification process
3. **Milestone 3: Product Management**
    
    - Epic 3: Product Listing
        - User Story 5: Display list of available products
            - Task 1: Design product listing page UI
            - Task 2: Fetch and display products from database
        - User Story 6: Implement product search functionality
            - Task 1: Create search bar component
            - Task 2: Implement search logic

### Project Progression

The project evolved iteratively, with each milestone representing a significant step forward in the development process. Tasks within each milestone were completed incrementally, with regular reviews and adjustments made to ensure alignment with project goals and user requirements.

In summary, the use of project milestones, epics, user stories, and tasks, coupled with effective project management tools like GitHub Projects and Kanban boards, facilitated a structured and organized approach to building Fetch & Feast.


## Features

### Existing Features

### Site Pages

- ### Homepage

- **Navigation Bar:**
    - The navigation bar serves as a central hub for accessing key features and navigating the site.
    - **Logo:**
        - Positioned prominently on the left side of the navigation bar, the logo serves as a visual anchor, reinforcing brand identity.
    - **Search Bar:**
        - Located prominently within the navigation bar, the search bar allows users to quickly find specific products or content.
    - **Account Dropdown:**
        - For logged-out users, the account dropdown provides options to log in or sign up for an account.
        - Logged-in users have access to their profile, enabling them to manage their account settings, view orders, and access additional features.
        - Superusers have additional options for product management, allowing them to oversee content creation and updates.
    - **Main Navigation:**
        - Positioned below the account dropdown, the main navigation menu offers dropdown options for each page category, Product and More.
        - Each dropdown menu provides access to specific sections or pages related to the respective category, enhancing navigation efficiency for users.

- **Hero Image:**

    - The main homepage showcases a large, visually striking hero image that instantly grabs the user's attention. High-quality hero image shows a girl sitting on an elevator, appealing to female customers with trendy fashion clothes and jewelry. 
    - A prominent call-to-action button invites users to enter and explore the site's products.

<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/3d3a0259-23cf-41f7-8053-dfc49b01c3cf" alt="hero-image-and-nav">
</div>
<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/b0c6d87b-b9d6-454c-a77d-ca430e8b542b" alt="hero-image-and-nav-mobile">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/1c735239-0d1c-4e01-9b0b-05c21438109a" alt="hero-image-and-nav-mobile">
</div>

- ### Footer
    
    - The footer section of the website offers convenient navigation and essential information for users.
    - **Contact Us:**
        - Includes links to the contact page and FAQ section, providing users with quick access to assistance and support.
        - **FAQs :**
        This link leads to the FAQ section, providing users with quick access to answers of Frequently Asked Questions.
    - **My Account Column:**
        - For logged-out users, this column features options to log in or sign up for an account.
        - Logged-in users have access to their profile, allowing them to manage their account settings, and sign out if needed.
        - Superusers have additional options for product management, enabling them to oversee content creation and updates.
    - **Contact Info:**
        - Includes essential contact details are the most important links for the customers, for their convenience most appropriate contact link is whatsapp, through this they can be redirected to WhatsApp on their mobile phone and chat about the product & services, real link has been given through the site. Next to this is email the for the customers who want to be contacted via email. Telephone number is next in the list and last link address with the google map. Contact details such as phone number, email address, and location, ensure users can reach out for assistance or inquiries. 
    - **Social Media and Legal Links:**
        - Features a link to the site's Facebook page, facilitating social media engagement and community interaction.
        - Includes copyright information and a link to the privacy policy, ensuring compliance with legal requirements and providing transparency to users regarding data usage and privacy practices.

<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/64c9ad05-c6a6-45dc-8d32-c118684d9b1b" alt="footer">
</div>

- Mobile

<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/5e2fb208-25fb-4733-8cc5-b8a946a4462c" alt="footer-mobile">
</div>

## Web Marketing

Newsletters were implemented in the email_notification app. The manager can create a newsletter and send it to all customers. It also handles sending newsletters about new loyalty programs with promo codes.

1. News Letter/ Subscribtion

To send a newsletter to all customers, the manager can create a newsletter and send it to all customers.
I have used Django EmailMultiAlternatives to send the newsletter.

![NewsLetter]()

2. Discounts and offers

To send a newsletter about new loyalty programs, offers, and discounts to all customers, the manager/admin can create a newsletter using the same form with a promo code field filled with a legend. Django EmailMultiAlternatives is also responsible for it.



3. Facebook

Facebook is essential for the store to be able to reach customers. According to the statistics, the store has a good reach among people who prefer to use Facebook. Facebook has excellent coverage worldwide among people who can purchase products online.

"Jolie Mimi Boutique" Facebook page is for marketing purposes to post adverts and exciting content and engage users.

![Jolie Mimi Boutique](readme-images/facebook-page.jpeg)

Please follow the links to see more images:

[facebook-page](https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/3c0ef45f-6715-4a48-b8f6-37c3c99b3f12)

[facebook-page-2](https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/a1f880bc-70c8-4721-b632-3d3d911914bd)

[facebook-page-3](https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/1c23a8f0-86af-4dbd-b96a-f2a0983d0068)


4. Instagram

Instagram attracts people of younger ages and is essential for the store to be able to reach this age group. According to the statistics, 90% of Instagram users are under 35 years old. [See report](https://info.lse.ac.uk/staff/divisions/communications-division/digital-communications-team/assets/documents/guides/A-Guide-To-Social-Media-Platforms-and-Demographics.pdf)

"Jolie Mimi Boutique" Instagram page is for marketing purposes to post adverts, interesting content, and engage users.

![Jolie Mimi Boutique](readme-images/instagram.jpeg)


- ### Product List
    - The product list feature provides users with a straightforward and intuitive way to browse through available products.
    - **Display Format:**
        - Products are presented in individual cards, each containing essential information such as the product image, name, rating, reviews,selling price, (discounted price, for future development) and category.
        - For superusers, additional options to edit/update and delete products are available directly within the product cards.
    - **Pagination:**
        - To enhance usability and manageability, the product list displays a maximum of 4 products in a row and scroll-down button can show all of them.
        - If user wants to go back and have a look at particular one which was at the top row of the page, He can use the 'Back to Top' button, which is located at the bottom right corner of the page.

<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/d963d3ae-47cd-4bfe-b6dd-0db609038ee8
" alt="products">
</div>
<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/4709e570-cff5-4272-b516-778f44bae65f" alt="products-mobile">
</div>

- ### Product Detail
    - The product detail section on the product page provides users with comprehensive information about the selected product.
    - **Content Displayed:**
        - Product Name: Clearly identifies the product for users.
        - Price: Displays the price of the product, allowing users to make informed purchasing decisions.
        - Average Rating: Shows the average rating of the product based on user reviews from the ratings model, providing social proof and credibility.
        - Category: Indicates the category to which the product belongs, aiding users in navigation and organization.
        - Edit/Delete Links (for Superusers): Allows superusers to perform administrative actions such as editing or deleting the product directly from the product detail page.
        - Product Description: Provides a detailed description of the product, highlighting its features and benefits.
        - Quantity Selector: Enables users to select the desired quantity of the product before adding it to their shopping bag.
        - "Keep Shopping" Button: Offers users the option to continue browsing other products without leaving the current page.
        - "Add to Bag" Button: Allows users to add the selected quantity of the product to their shopping bag, initiating the checkout process.
    - **Product Image:**
        - The product image is prominently displayed within the product detail section.
        - A simple Bootstrap popup modal is implemented to allow users to view a larger version of the product image if desired, enhancing the user experience by providing a closer look at the product.

<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/ebd363f3-9e4a-46c8-8a4b-4851f9745ea8" alt="products">
</div>

- ### Reviews

    - The `product_detail` view renders the reviews.
    - Reviews for the products are retrieved from the database and paginated for easy navigation.
    - Users can submit a review of the product by using a very easy form, with validation to ensure proper input.
    - A check is performed to determine if the current user has an account, allowing only verified account holders to submit reviews.
    - Profile names of users who submitted reviews are displayed alongside the date and stars, enhancing the credibility of the ratings and reviews.
    - Superusers can edit or delete individual reviews/ratings through dedicated updated reviews.
.

<div align="center">
 <img src="https://github.com/Mr-KulwinderSingh/jolie_mimi_boutique/assets/124357266/87704023-b1a2-44d8-8009-052eb354d621" alt="reviews">
</div>


## Technologies used
- ### Languages:
    
    + [Python 3.8.5](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
    + [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    + [jQuery](https://jquery.com/): was used to control click events and sending AJAX requests.
    + [jQuery User Interface](https://jqueryui.com/) was used to create interactive elements.

- ### Databases:

    + [SQLite](https://www.sqlite.org/): was used as a development database.
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.


- ### Other tools:

    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Gunicorn](https://gunicorn.org/): the web server used to run the website.
    + [Psycopg2](https://www.psycopg.org/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
    + [Render](https://pypi.org/project/render/): was used to render the README file.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    + [Draw.io](https://www.lucidchart.com/) was used to make a flowchart for the README file.
    + [Color-hex](https://www.color-hex.com/) was used to make a colour palette for the website.
    + [Photoroom](https://www.photoroom.com/) was used to edit and change the background of all the pictures, all pictures are real and taken with Redmi 12 5g mobile. 3 pictures are downloaded from google.
    + [BGJar](https://www.bgjar.com/): was used to make a background images for the website.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [JShint](https://jshint.com/): was used to validate JS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.
    + [geonames](https://www.geonames.org/) was used to get the country and city names.
    + [Multiple Video & Image Upload Plugin - jQuery Miv.js](https://www.jqueryscript.net/form/multi-video-image-upload.html) was used to upload multiple videos and images. **Note:** the plugin  is using special characters in css and js files that I am aware about!
    + [stripe](https://stripe.com/): was used to create the payment system.
    + [birme.net](https://www.birme.net/): was used to crop and center unsplash images.
    + [Sitemap Generator](https://www.xml-sitemaps.com/) was used to create the sitemap.xml file.
    + [Privacy Policy Generator](https://www.privacypolicygenerator.info/) was used to create the privacy policy.
    + [Django-extensions](https://django-extensions.readthedocs.io/en/latest/) was used to create a Entity-Relationship Diagram.

# Webhooks
    
- The site uses a secure and robust webhook system to ensure that the payment process cannot be interrupted and corrupted, either through user error or malicious intent. Webhooks are incorporated via the Stripe payment system and are handled on the Stripe website, by way of the python code in `checkout > webhook_handler.py` and `checkout > webhooks.py`

<div align="center">
 <img src="" alt="stripe-webhooks">
</div>
