from webbrowser import open
from getCreds import get_creds

def open_chart() -> None:
    """
    Opens the pixela graph of the specified username and graph-ID in their default browser
    Args:
        None
    Returns:
        None
    """
    creds = get_creds()
    username = creds["username"]
    graphID = creds["graphID"]
    url = f"https://pixe.la/v1/users/{username}/graphs/{graphID}.html"
    open(url)

