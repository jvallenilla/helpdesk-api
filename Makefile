interprete = @python3 manage.py

install:
	@pip3 install --upgrade pip
	@pip3 install -r helpdesk/requirements.pip

seeder:
	$(interprete) shell < tickets/seeders/defaults.py

migrations:
	$(interprete) makemigrations
	$(interprete) migrate

reset_db:
	$(interprete) flush --noinput
