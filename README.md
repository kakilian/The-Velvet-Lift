# The Velvet Lift 2025

**The Velvet Lift** is a Django web application for managing cosmetic surgery procedure. The project is organized into several modular apps to keep functionality separate and maintainable.

## Project Overview

This project consists of the following Django apps:

- **assests**: Contains static files (CSS, JS, images, icons).
- **appointments**: (Previously named 'auxiliary_features') Manages appointment bookings and payment tracking.
- **main_features**: Provides additional core functionality and views (such as a homepage or other shared features).
- **technical_subsystems**: Contains technical functionality (e.g. parts of user profiles if needed).
- **template_app**: Holds gobal, reuseable templates (base, layout, header, footer, etc.).
- **user_profiles**: Dedicated app for user profile management, including extened user details and doctor information.

## Models

### user_profiles/models.py
- **UserProlfile**: Extends Django's default User Model with extra fields (phone, profile picture).
- **Doctor**: Associates a doctor (extending the User model) with a specialization.

### appointment/models.py
- **Appointment**: Records appointment bookings (links to a User and a Doctor).
- **Payment**: Tracks payment details for appointments.

### transformations/models.py
- **Tranformation**: Stores befreo-and-after images and procedure details for cosmetic procedures.

## Setup instructions

### Prerequisites
- Python 3.12.2
- Djanog 4.2.17
- [Other dependenicies as listed in 'requirements.tx'](#requirements)

## Installation ![Installation](https://img.shields.io/badge/Installation-Setup%20Guide-orange?style=for-the-badge&logo=python)


1. Install Python module dependencies:
   ```bash
   cd thevelvetlift
   pip3 install -r requirements.txt
   ```

### Frameworks/Libraries, Programs, and Tools
- Gitpod ![Gitpod](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)
- GitHub ![GitHub](https://img.shields.io/badge/GitHub-Repository-181717.svg)
- Heroku ![Heroku](https://img.shields.io/badge/Deployed%20on-Heroku-430098?style=for-the-badge&logo=heroku)

## Requirements
- Django Pillow ![Django Pillow](https://img.shields.io/badge/Django-Pillow-0.4.6-red.svg)
- Gitpod ![Gitpod](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)
- GitHub ![GitHub](https://img.shields.io/badge/GitHub-Repository-181717.svg)
- Heroku ![Heroku](https://img.shields.io/badge/Deployed%20on-Heroku-430098?style=for-the-badge&logo=heroku)

## Deployment ![Deployment](https://img.shields.io/badge/Deployment-Ready-success?style=for-the-badge)


### To deploy the project locally:
1. Install Python and pip.
2. Clone the repository:
   ```bash
   git clone https://github.com/kakilian/thevelvetlift.git
   ```
3. Navigate to the project directory and install dependencies:
   ```bash
   cd animated-waffle
   pip3 install -r requirements.txt
   ```

### To deploy the project to Heroku: ![Heroku](https://img.shields.io/badge/Deployed%20on-Heroku-430098?style=for-the-badge&logo=heroku)

1. Create a Heroku account and a new application.
2. Link your GitHub repository to Heroku.
3. Add Python and Node.js buildpacks.
4. Set the `PORT` config var to `8000`.
5. Deploy the branch and launch the application.

---

## Credits ![Credits](https://img.shields.io/badge/Credits-Thanks%20to%20all%20contributors-blue?style=for-the-badge&logo=heart)


## Bugs ![Bugs](https://img.shields.io/badge/Bugs-Squashed-brightgreen?style=for-the-badge&logo=bug&logoColor=white)


### Solved Bugs ![Killed Bugs](https://img.shields.io/badge/Killed%20Bugs-✔️-brightgreen?style=for-the-badge&logo=bugatti)


### Unsolved Bugs ![Alive Bugs](https://img.shields.io/badge/Alive%20Bugs-❌-red?style=for-the-badge&logo=bugatti)




## Future Improvements ![Future Improvements](https://img.shields.io/badge/✈️-Future%20Improvements-blue?style=for-the-badge)

- Refactor views to use class-based views where appropriate.
- Enhance user profile functionality (e.g., allow users to update their profiles).
- Add more detailed appointment scheduling features.
- Improve styling and add responsive design.





## Notes
- ### Static Files:
The static files are served from the assets/ folder. In settings.py, make sure:

python
 ```bash
STATIC_URL = "/assets/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```

- ### Templates:
Global templates are stored in ```bash template_app/templates/template_app/ ```. Use these for your base layout and shared UI components.
App Renaming:
Note that the auxiliary_features app was renamed to appointments for clarity.










## Introduction
a modern Astetik Company with years experience all under one roof to provide Woman and Men 18+ to help get a push in the right driection, looking for that special something inside.





Problems:
I spent a good part of the last days trying to find my bugs that through spelling, gap mistakes, also the programming that I thought was correct.
I also along my journey of making this APP found Django Pillow which I really wanted to use. As its an up to date revolution for programming. Again those guys get it right.
I hesitated to commit my mistakes to github as I was afraid like in previous projects I would fall trap to not knowing where I was, and would be able to grab back what was orignally coded. Sorry github for the load. 
Confusion with using simular wording as in django application like static, and templates. I needed to firstly reconise the bug I had created a solid solution to avoid the APP not functioning.
While creating the "models" althought they were a lot of fun to play around with - i got a lot of warnings from gitpod as I tried to migrate. I didnt even notice that I had placed user_profiles under another APP which confused the work progress.
Testing

Font

