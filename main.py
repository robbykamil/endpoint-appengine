#main.py

import os

import cloudstorage
from google.appengine.api import app_identity

import webapp2


def get(self):
	bucket_name = os.environ.get(
		'sign-image', app_identity.get_default_gcs_bucket_name())


def read_file(self, huruf):
	with cloudstorage.open(huruf) as cloudstorage_file:
		self.response.write(cloudstorage_file.readline())
		cloudstorage_file.seek(-1024, os.SEEK_END)
		self.response.write(cloudstorage_file.read())
