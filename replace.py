import os

hub_url = os.environ.get('HUB_URL')
if not hub_url or not hub_url.startswith('http'):
  raise Exception('Faltou definir a variavel de ambiente HUB_URL. Ex.: https://api.santander.corp')

sso_url = os.environ.get('SSO_URL')
if not sso_url or not sso_url.startswith('http'):
  raise Exception('Faltou definir a variavel de ambiente SSO_URL. Ex.: https://wastfcdvlbr01.bs.br.bsch')



folder = '/usr/share/nginx/html/'

counter = 0

for subdir, dirs, files in os.walk(folder):
    for file in files:
        FILE = os.path.join(subdir, file)
        print FILE

        content = ''
        with open(FILE, 'r') as input:
            content = input.read()
            content = content.replace('SANTANDER_REPLACE_HUBURL', '%s' % hub_url)
            content = content.replace('SANTANDER_REPLACE_SSO', '%s' % sso_url)

        with open(FILE, 'w') as output:
            output.write(content)

        counter = counter + 1

print counter
