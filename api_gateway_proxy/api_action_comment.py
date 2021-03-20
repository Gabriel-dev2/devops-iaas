import json
import os
import traceback

from api_action import Action


class APIActionComment(Action):

    def __init__(self, logger):
        super().__init__(logger)
        self.__logger = logger

    
    def __add_comment(self, issue, comment):
        response = ''
        try:
            jira = super().create_jira_authentication()
            comment_id = jira.add_comment(issue, comment)
            response = f'Comment successfully added: {comment_id}'
        except Exception as why:
            raise why
        return response


    def handler(self, request, response):
        comment = request.get('message')
        issue = request.get('branch')
        data = self.__add_comment(issue, comment)
        response['data'] = {'result': data}
        return response