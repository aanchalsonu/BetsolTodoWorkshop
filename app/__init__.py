"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="ddpg-cgrqndvdvk4rjsvdgrgg-a.oregon-postgres.render.com",
        database="betsoltodo_pc0s",
        user="betsoltodo_pc0s_user",
        password="pxfsODSdmoBDHrubwC1tArVJWrODnGsM")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
