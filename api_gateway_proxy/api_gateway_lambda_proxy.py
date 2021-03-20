import json
import os
import traceback

# LAMBDA LAYERS
from lambda_utils import logger as lambda_logger
from lambda_utils.validator import ParamsValidator

# actions
from api_action_version import APIActionVersion
from api_action_comment import APIActionComment

env_validator = ParamsValidator(os.environ)
logger = lambda_logger.Logger(__name__, env_validator.get_parameter('LOGGIN_LEVEL'), enable_xray=True)

def lambda_handler(event, context):
    response = {}
    response['headers'] = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    response_body = {}

    try:
        logger.info('Starting execution')
        response_body = router(event)
        response_body['status'] = 'SUCCESS'
        response['statusCode'] = '200'

    except AttributeError as why:
        traceback_message = traceback.format_exc()
        response_body = format_error_message(traceback_message=traceback_message, why=why, response_body=response_body)

    except Exception as why:
        traceback_message = traceback.format_exc()
        response_body = format_error_message(traceback_message=traceback_message, why=why, response_body=response_body)
        response['statusCode'] = 500

    response['body'] = json.dumps(response_body)
    return response

def format_error_message(traceback_message, why,response_body):
    response_body['status'] = 'ERROR'
    response_body['cause'] = str(why)
    response_body['traceback'] = str(traceback_message)
    logger.error(__error_message(str(why), traceback_message))
    return response_body

def __error_message(message, traceback_msg):
    return f'Lambda function failed to execute: {message}: {traceback_msg}'

def router(event):

    response_body = {}

    logger.debug(json.dumps(event))

    resource = event.get('resource')

    # validating body
    body_str = event.get('body')
    body = {} if body_str is None else json.loads(body_str)

    action = None

    if resource == '/version':
        action = APIActionVersion(logger)
    elif resource == '/issue/comment':
        action = APIActionComment(logger)
    elif resource == '/project/release/{projectName}':
        # implementar action de releases
        pass
    else:
        raise AttributeError(f'Resource {resource} not found')

    response_body = action.hander(body, response_body)

    return response_body
