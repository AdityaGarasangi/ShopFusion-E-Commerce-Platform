# ShopFusion - E-Commerce Web Application

ShopFusion is a modern e-commerce platform built with Django, providing a seamless shopping experience for users. The application allows customers to browse products, manage their carts, place orders, and manage their accounts. ShopFusion also features an intuitive dashboard for sellers to manage their products, track sales, and view statistics.

## Features

- **User Authentication**: User registration, login, and logout functionality.
- **Product Management**: Sellers can create, edit, and delete products.
- **Shopping Cart**: Add items to the cart and view cart details before checkout.
- **Checkout Process**: Users can complete their orders by providing personal details.
- **Sales Statistics**: Sellers can view statistics about their sales.
- **Responsive Design**: The platform is fully responsive and optimized for both desktop and mobile use.

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS (Bootstrap v5.3), JavaScript
- **Database**: SQLite (default) or PostgreSQL (for production)
- **Authentication**: Django's built-in authentication system
- **Web Framework**: Django


## Setup Instructions

### Prerequisites

- Python 3.x
- Django 4.x (or later)
- SQLite or PostgreSQL

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AdityaGarasangi/shopfusion-E-Commerce-Platform.git
   cd shopfusion-E-Commerce-Platform

2. **Install Dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. **Set Up Database**

   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. **Create Superuser (Optional)**

   ```bash
   python manage.py createsuperuser

5. **Run the Development Server**

   ```bash
   python manage.py runserver

6. **Access the Application**

   Open your browser and go to ```http://127.0.0.1:8000/user/register``` to view the website.
























   
