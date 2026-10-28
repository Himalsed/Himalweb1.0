# Himalweb

Portfolio site built with Flask.

## Contact form email setup

The contact form sends messages through Gmail using SMTP. Set these environment variables in the environment where the Flask app runs:

- `GMAIL_ADDRESS`: Gmail account used to send the messages.
- `GMAIL_APP_PASSWORD`: an app password created for that Gmail account. Use an app password, not the account's regular password.
- `CONTACT_RECIPIENT`: inbox that should receive contact form submissions. This can be the same Gmail address as `GMAIL_ADDRESS`.
- `FLASK_SECRET_KEY`: a long, random secret used to sign Flask sessions.

For local development, copy `.env.example` to `.env`, replace the example values, and run the app. The `.env` file is ignored by Git and must stay private.

For deployment, add the variables in the hosting provider's environment or secrets settings, then restart or redeploy the Flask app. A local `.env` file is not uploaded with the Git repository. The deployed app logs which setting is missing without logging any credential values.
