#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/') #, swagger_path='c:/users/seedot1234/appdata/local/programs/python/python37/lib/site-packages')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Simple Inventory API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
