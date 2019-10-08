# Mailing genius

## Installation

```
	git clone https://github.com/Souldiv/mailing-genius.git
	pip install requirements.txt
```

## Sample Usage

```
	>>> from sendmails import send_mails
	>>> sm = send_mails("api key")
	>>> sm.send(from, to, subject)
```

## Sengrid CLI

```cmd
	python sengrid_cli.py --html ['html_path'] --file ['mail_address_file_path] --attach ['path(optional)]
```
