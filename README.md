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
- [Other dependenicies as listed in 'reuirements.tx'](#requirements)

### Installation

1. **Clone the Repository**

git clone <repository_url>
cd The-Velvet-Lift</repository_url> 












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

