import os
import requests
import traceback

from api_action import Action

class APIActionVersion(Action):

    def __init__(self, logger):
        super().__init__(logger)
        self.logger = logger

    
    def handler(self, request, response):
        response['data'] = {'version': os.environ.get('VERSION')}
        return response