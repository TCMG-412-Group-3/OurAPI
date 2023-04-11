import typer
import requests

#Typer truly is the 'FastAPI' for CLI's :D
app = typer.Typer()
BASE_URL = "http://34.135.137.212:4000"

#Example of a command
# @app.command()
# def hello(name: str):
#     """Say hello to someone"""
#     typer.echo(f"Hello {name}!")

@app.command()
def md5(input: str = typer.Argument(..., help="The string to hash")):
    """Hash a string using MD5"""
    response = requests.get(f"{BASE_URL}/md5/{input}")
    typer.echo(response.json())

@app.command()
def factorial(input: int = typer.Argument(..., help="The integer number to calculate the factorial of")):
    """Calculate the factorial of a number"""
    response = requests.get(f"{BASE_URL}/factorial/{input}")
    typer.echo(response.json())

@app.command()
def fibonacci(input: int = typer.Argument(..., help="The integer number to calculate the fibonacci sequence to")):
    """Calculate the fibonacci sequence to a number"""
    response = requests.get(f"{BASE_URL}/fibonacci/{input}")
    typer.echo(response.json())

@app.command()
def is_prime(input: int = typer.Argument(..., help="The integer number to check if it is prime")):
    """Determine if a number is prime"""
    response = requests.get(f"{BASE_URL}/is-prime/{input}")
    typer.echo(response.json())

@app.command()
def slack_alert(input: str = typer.Argument(..., help="The message to send to the slack channel")):
    """Send a message to a slack channel"""
    response = requests.get(f"{BASE_URL}/slack-alert/{input}")
    typer.echo(response.json())

@app.command()
def key_val(key: str = typer.Argument(..., help="The key to store the value under"),
            value: str = typer.Argument(..., help="The value to store"),
            delete: bool = typer.Option(False, "--delete", "-d", help="Delete a key-value pair"),
            update: bool = typer.Option(False, "--update", "-u", help="Update a key-value pair"),
            create: bool = typer.Option(False, "--create", "-c", help="Create a key-value pair")
):
    """Create, read, update, or delete a key value pair; command without any options is only a GET request for the
    key-value pair"""
    if create:
        payload = {"storage-key": key, "storage-val": value}
        response = requests.post(f"{BASE_URL}/keyval", json=payload)
        typer.echo(response.json())
    elif update:
        payload = {"storage-key": key, "storage-val": value}
        response = requests.put(f"{BASE_URL}/keyval", json=payload)
        typer.echo(response.json())
    elif delete:
        response = requests.delete(f"{BASE_URL}/keyval/{key}")
        typer.echo(response.json())
    else:
        response = requests.get(f"{BASE_URL}/keyval/{key}")
        typer.echo(response.json())


if __name__ == "__main__":
    app()
