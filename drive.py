from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_to_google_drive(csv_path):
    gauth = GoogleAuth()
    # gauth.credentials = gauth.SavedCredentials('mycreds.txt')  # Creates a file 'mycreds.txt' to save authentication data

    if gauth.credentials is None:
        gauth.LocalWebserverAuth()  # For first-time authentication

    elif gauth.access_token_expired:
        gauth.Refresh()  # Refreshes token if expired

    else:
        gauth.Authorize()  # Authorizes if everything is fine

    gauth.SaveCredentialsFile('client_secrets.json')  # Saves the authentication data for the next run

    drive = GoogleDrive(gauth)

    # Create a CSV file on Google Drive
    file_drive = drive.CreateFile({'title': 'apart_results.csv'})
    print(file_drive, 'ran through drive')
    file_drive.Upload()

    # Set content of the CSV file
    file_drive.SetContentFile(csv_path)
    file_drive.Upload()