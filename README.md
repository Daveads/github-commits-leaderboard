# Raider 

Raider ranks specific users based on their GitHub commits for the current year and orders them by commit frequency. The system sends the commit statistics for the year, along with daily commit information, either for you or specific users via email.



### Usage

1. Users commit for the current year:
   Edit the `brainiacs.txt` file and add your GitHub username.

2. To get daily commits:
   Edit the `specific_brainiacs_data.json` file and add your username.

3. To receive emails:
   Add your email addresses.

**NOTE:**
For daily commits Email, add your username to list in the `brainiacs.txt` and `specific_brainiacs_data.json` files.




## For local build or pushing to a server:

- Clone the repository:
   ```
   git clone git@github.com:daveads/raider.git
   ```

- Edit the environment variables:
   ```
   mv env_var .env
   // Edit details in the .env file
   ```

- Set up environment variables and perform other setup:
   ```bash
   bash run.sh
   ```

// Once these steps are completed, you should be all set!
