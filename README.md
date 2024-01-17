# Team_Management_API

## Installing using GitHub

1. Install PostgresSQL and create a database.

   ```bash
   git clone https://github.com/Veinmax/team_management_api.git
   cd team_management_api
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   Configure Environment Variables:
- Create a .env file in the project root.
- Make sure it includes all the variables listed in the .env.sample file.
- Ensure that the variable names and values match those in the sample file.
   ```bash
   set SECRET_KEY=<your secret key>
   python manage.py migrate
   ```

Run the Server:
```bash
python manage.py runserver
```
