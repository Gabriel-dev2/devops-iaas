'''
Abstract class
'''
import os
import json

# jira library
from jira import JIRA

ATLASSIAN_URL = os.environ.get('ATLASSIAN_URL')
USER_NAME = os.environ.get('USER_NAME')
API_TOKEN = os.environ.get('API_TOKEN')


class Action():

    def __init__(self, logger):
        self.__logger = logger

    
    def create_jira_authentication(self):
        jira = JIRA(ATLASSIAN_URL, basic_auth=(USER_NAME, API_TOKEN))
        return jira

    def handler(self, request, response):
        pass # abstract method