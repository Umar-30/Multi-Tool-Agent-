import aiosmtplib

from email.mime.text import MIMEText

from app.config import settings


async def send_email(
    to_email: str,
    subject: str,
    body: str
):

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = settings.EMAIL_USER
    msg["To"] = to_email

    await aiosmtplib.send(
        msg,
        hostname="smtp.gmail.com",
        port=465,
        username=settings.EMAIL_USER,
        password=settings.EMAIL_PASSWORD,
        use_tls=True
    )