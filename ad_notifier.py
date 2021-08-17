import click



# @click.command()
# @click.argument('url')
# @click.option('--email', envvar="EMAIL_ADDRESS")
# @click.option('--reset-cache', is_flag=True, default=False)
# def main(url: str, email: str, reset_cache: bool):
#     print("I'm the add cli")
#     print(f"url: {url}")

#     if email:
#         print(f"email: {email}")
    
#     if reset_cache:
#         print("reset_cache is true")


@click.group()
def main():
    pass


@main.command()
@click.argument('url')
@click.option('--email', envvar="EMAIL_ADDRESS")
@click.option('--reset-cache', is_flag=True, default=False)
def run_once(url, email, reset_cache):
    process_url(url,email, reset_cache)


def process_url(url, email, reset_cache):
    print(f"url: {url}")
    if email:
        print(f"email: {email}")
    if reset_cache:
        print("reset_cache is true")


if __name__ == "__main__":
    main()