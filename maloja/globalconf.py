from doreah.settings import get_settings
import os

THUMBOR_SERVER, THUMBOR_SECRET = get_settings("THUMBOR_SERVER","THUMBOR_SECRET")
try:
	USE_THUMBOR = THUMBOR_SERVER is not None and THUMBOR_SECRET is not None
	if USE_THUMBOR:
		from libthumbor import CryptoURL
		THUMBOR_GENERATOR = CryptoURL(key=THUMBOR_SECRET)
		OWNURL = get_settings("PUBLIC_URL")
		assert OWNURL is not None
except:
	USE_THUMBOR = False
	log("Thumbor could not be initialized. Is libthumbor installed?")




try:
	DATA_DIR = os.environ["XDG_DATA_HOME"].split(":")[0]
	assert os.path.exists(DATA_DIR)
except:
	DATA_DIR = os.path.join(os.environ["HOME"],".local/share/")

DATA_DIR = os.path.join(DATA_DIR,"maloja")
os.makedirs(DATA_DIR,exist_ok=True)
