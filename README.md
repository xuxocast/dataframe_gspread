# dataframe_gspread
Enlace entre pandas y google sheets

## Dependencias

1. Pandas
2. numpy
2. gspread
3. gspread_pandas

## Client Credentials

To allow a script to use Google Drive API we need to authenticate our self towards Google. To do so, we need to create a project, describing the tool and generate credentials. Please use your web browser and go to Google console and:

-Choose Create Project in popup menu on the top.

-A dialog box appears, so give your project a name and click on Create button.

-On the left-side menu click on API Manager.

-A table of available APIs is shown. Switch Drive API and click on Enable API button. Do the same for Sheets API. Other APIs might be switched off, for our purpose.

-On the left-side menu click on Credentials.

-In section OAuth consent screen select your email address and give your product a name. Then click on Save button.

-In section Credentials click on Add credentials and switch OAuth client ID (if you want to use your own account or enable the use of multiple accounts) or Service account key (if you prefer to have a service account interacting with spreadsheets).

-If you select OAuth client ID:
Select Application type item as Other and give it a name.
Click on Create button.
Click on Download JSON icon on the right side of created OAuth client IDs and store the downloaded file on your file system.

-If you select Service account key
Click on Service account dropdown and select New service account
Give it a Service account name and ignore the Role dropdown (unless you know you need this for something else, it's not necessary for working with spreadsheets)
Note the Service account ID as you might need to give that user permission to interact with your spreadsheets
Leave Key type as JSON
Click Create and store the downloaded file on your file system.

-Please be aware, the file contains your private credentials, so take care of the file in the same way you care of your private SSH key; Move the downloaded JSON to ~/.config/gspread_pandas/google_secret.json (or you can configure the directory and file name by directly calling gspread_pandas.conf.get_config
Thanks to similar project df2gspread for this great description of how to get the client credentials.

