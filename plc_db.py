import time
from firebase_admin import credentials
from firebase_admin import db
from pyModbusTCP.client import ModbusClient

# Fetch the service account key JSON file contents
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "schneider-project",
  "private_key_id": "ffe6c921bf720c81ac12a07aed76b34a4724403d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDlQUJjdgYIYyio\n3VejDooRZxIp2HGiorrnVcXL9AJ9KFOb7HmLaAvucRfnBbRO/p9uKPbdGVLI52pW\nfUruW7kjbbwOGkcXhx+WLU/4BuCClLshHOVP47MZNvEOku6zIpCCWHsNfi2Rk3NS\nUxpF9IwwH4o7bVFEj3g/h3SSR7TfDRjZ0J6MlnHv3n/UISIPU1HkgxeEvnJ7OKpP\nt0M9rWWoPcrAD7ZUf4usTXpdrfYnpzX3Igx6ImBDPpjt4+21eMqmSkZGZBcIRLe2\nQmoa3liTxGNUBjU59NMP4syaTBUAbCa5zZ5ncM90M/mCsy2baFwF+xT8m3H29FPQ\nUcYyo/qTAgMBAAECggEALf41r3aSJ0Sdd6NQXaohEPS4tCR0R8iV7qtKj2xYw3s/\nqtx6Vfl9y0xtGzANyHtUyOj2/cyCy0OCFe/1BHTqY600OTAUayf0slBM5tmaWRg1\noqMFbk2kNL7NBbt8n/ujOkM+DKrvwXDvheieMMKrDUyGkv2PfE28NiKaxG4WX1kE\nGgOTzYFg9IzlPvX8tF40SPAKraUg/sKreamu5DHp0PJyF1xYXR8eRpzs7lUP9o4W\njWvHQItRSYb6mfbf0yo02ZdBezFxTI7wF1YjYQmdSBZN2aqjPdBSdzCAQh6cMOZr\n+4mawZKn3eYdOsqqEBIj3O8EWqE6Rnmc3t3iEAcIYQKBgQD0MU+Py71BdIbOsJiI\nWrGBhWYtXxK9omFo09Zhe13CF/f/r3mvy4PokSBi0+G5J0u/F6e792e6fAeRgXXe\nlTHj0lL0mDZHPwK8w5ECuxvNIi3F4W+dBOR92I+DAsWpQYtSlesiqRmRIOAdhFDR\nuXhfPWTeIkTUIR8c6AtgUzDtPwKBgQDwVwuTSdIhzWUNgqSlB9T4V41OgUOuimts\nPCXgAlCcu2oa7+firjiNk60P16Q9ZfQ/lf040/0LtcOawk4/h4J7Rq9fps0SaiiT\n8WdI3DJqsyxsYdWBiN+6jQQrZnspKmIYt3D2vHGyDFaGOjM5K+wERz7iAbdUPfbL\na4gI6/eZrQKBgQCdVNwPKNTiRGLK7usIB28QpVNk7jmT5vhd4wbgPez1rh3CJlv/\n0N9HS6ITKrLnaZMbJvGSYN/7PgheTowUAgpn385E+4EVPFrWJibbHJTYASp+sTYJ\nc+qHzq0AWxvhZnKOnjsmVM89O3JKckLkLVyJ+HNxz6CLEGAMbtFNmawPXwKBgQDd\nlBLK7yM5IMkKpKiwscDKWMWhXBGPKHSTa/yrQtcZOLxBK29JEMB43m6OjYwRQx7l\nRJ4Zt2+zTReSZZOIhKFqkCd9cyXb1V2lz8keZkxhDOFm5ufVreA+eGYgsTHZKQcZ\nrH4MLH5R3Ygj5iJ1kiXdZ+X0rgpcM2iF8JSRTSOQXQKBgGcpn7ao2xoszv54apUP\ndhdROLteLrHUPJasTaksTWtFLnxI+5Fi0xz+veiqr3uV4zK1GID3ntC8N968m3Se\naE6telg+HZodjaq3v4/FZ0C6q9fPVwWx7aE8clkTI5Gph6rDV8DW1k0DTftzn3s2\nvIaiTEl9QF/S7oR27363/wqW\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ygdjt@schneider-project.iam.gserviceaccount.com",
  "client_id": "103751846783469949126",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ygdjt%40schneider-project.iam.gserviceaccount.com"
})
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred,
	{
    'databaseURL': 'https://schneider-project.firebaseio.com/'
})

c = ModbusClient()
c.host("192.168.0.112")
c.port(502)
c.open()
ref = db.reference('connect_plc')
value = ref.get()
app1 = value["appliance1"]
app2 = value["appliance2"]
app3 = value["appliance3"]
c.write_single_coil(0, app1)
c.write_single_coil(1, app2)
c.write_single_coil(2, app3)

while (True):
	value = ref.get()
	if(app1 != value["appliance1"]):
		print("app1 changed : " + str(value["appliance1"]))
		app1 = value["appliance1"]
		c.write_single_coil(0, app1)

	if(app2 != value["appliance2"]):
		print("app2 changed : " + str(value["appliance2"]))
		app2 = value["appliance2"]
		c.write_single_coil(1, app2)

	if(app3 != value["appliance3"]):
		print("app3 changed : " + str(value["appliance3"]))
		app3 = value["appliance3"]
		c.write_single_coil(2, app3)
