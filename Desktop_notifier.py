from plyer import notification
notification_title="Greetings from Github"
notification_message="Thank you for creating an account with us.Have a good day"
notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False)
