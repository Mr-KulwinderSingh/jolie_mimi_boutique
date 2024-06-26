# [Jolie Mimi Boutique](https://jolie-mimi-boutique-ad3e13f83c61.herokuapp.com/)
<div align="center">
 <img src="readme-images/am-i-responsive.jpeg" alt="Jolie Mimi Boutqique">
</div>

[Jolie Mimi Boutique](https://jolie-mimi-boutique-ad3e13f83c61.herokuapp.com/) is an ecommerce platfom as a ladies' boutique, dealing with the latest, chick and trendy clothes alongside some jewellery items, developed on Django. It encompasses user registration, profile management, newsletter subscriptions, and product purchases facilitated by Stripe. Users of Jolie Mimi Boutique can submit their reviews about the products they have bought or want to buy. Frontend admin controls empower easy management of products and users. Something new has also been introduced which is a live chat, this live chat can be controlled by the shop owner/staff and could be limited to one or more staff depending on the average number of customers serving who can answer customer questions straight away.

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
    - [Ratings](#ratings)
    - [Blog List](#blog-list)
    - [Blog Detail](#blog-detail)
    - [Comment Section](#comment-section)
    - [Post Update](#post-update)
    - [Contact Page](#contact-page)
    - [FAQ Page](#faq-page)
    - [Profile Page](#profile-page)
    - [Newsletter Subscription Management](#newsletter-subscription-management)
    - [Bag Page](#bag-page)
    - [Toasts Including Bag Preview](#toasts-including-bag-preview)
    - [Product Management](#product-management)
    - [Blog Management](#blog-management)
    - [Checkout](#checkout)
    - [Checkout Success](#checkout-success)
    - [Authentication Pages](#authentication-pages)    
    </details></li>

    <li>
    <a href="#features-not-yet-implemented">Features Not Yet Implemented</a>
    </li>
    </ul>
</details>
------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
