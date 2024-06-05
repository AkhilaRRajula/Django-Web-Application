# Django Job Application Web Application

## Project Overview
This is a Django-based web application for managing job applications. It allows users to fill out a job application form and receive an email confirmation upon submission. The admin panel provides features to view, add, edit, and delete applications, with various filters to manage the data efficiently.

## Features
- **Job Application Form:** Users can submit their job applications through a web form.
- **Email Notifications:** Applicants receive an automatic email confirmation after submitting their application.
- **Admin Panel:** Admins can view, add, edit, and delete job applications. The panel includes filters to easily manage the data.
- **Navigation Bar:** Easy access to the Home, About, and Contact pages.

## Screenshots
### Job Application Form
![Job Application Form](https://github.com/AkhilaRRajula/Django-Web-Application/assets/42290255/a25e5d51-c403-4f09-9752-a352d9e953a8)

### Admin Panel
![Admin Panel](https://github.com/AkhilaRRajula/Django-Web-Application/assets/42290255/ead2c424-801f-4785-ab28-b24f107f9800)


### Email Confirmation
![Email Confirmation](https://github.com/AkhilaRRajula/Django-Web-Application/assets/42290255/bbb91833-7d13-49bc-bc0f-649fd9c05ceb)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Job Application Form: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin`

## Usage
1. **Submit an Application:**
   - Navigate to the home page.
   - Fill out the job application form.
   - Click submit to receive a confirmation email.

2. **Admin Panel:**
   - Log in to the admin panel with your superuser credentials.
   - View, add, edit, or delete applications.
   - Use filters to manage the applications based on date, occupation, etc.

## Code Overview
- **Templates:**
  - `base.html`: Contains the navigation bar and other common elements.
  - `index.html`: The job application form.
  - `about.html`: Information about the website.
  - `contact.html`: Placeholder for the contact page.

- **Views:**
  - `views.py`: Contains the logic for rendering the form and handling submissions.

- **Models:**
  - `models.py`: Defines the JobApplication model with fields like first name, last name, email, etc.

- **Forms:**
  - `forms.py`: Contains the JobApplicationForm used to render the form in the template.

- **URLs:**
  - `urls.py`: Defines the URL patterns for the application.

- **Settings:**
  - `settings.py`: Configure email settings and other Django settings.

## Email Configuration
To enable email notifications, configure the email settings in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-email-host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

