import faulthandler

#faulthandler.enable()

from google.auth.transport.requests import AuthorizedSession
from google.auth import credentials

creds = credentials.AnonymousCredentials()
project = "sijunliu-dca-test"

import certifi
def where():
    return "C:\\workspace\\corp_cert\\google-auth-library-python\\my\\ec_cert.pem"
certifi.where = where

def offload_callback_raw():
    with open("./cert.pem", "rb") as f:
        cert = f.read()

    key = {
        "type": "raw",
        "info": {
            "pem_path": "./key.pem"
        } 
    }

    return cert, key

def offload_callback_windows():
    with open("./ec_cert.pem", "rb") as f:
        cert = f.read()

    key = {
        "type": "windows",
    }

    return cert, key

def raw_callback():
    with open("./cert.pem", "rb") as f:
        cert = f.read()

    with open("./key.pem", "rb") as f:
        key = f.read()

    return cert, key

def run_sample(callback):
    authed_session = AuthorizedSession(creds)
    authed_session.configure_mtls_channel(callback)
    print(authed_session.is_mtls)

    response = authed_session.request('GET', "https://localhost:3000/foo")
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    # run_sample(raw_callback)
    # run_sample(offload_callback_raw)
    run_sample(offload_callback_windows)