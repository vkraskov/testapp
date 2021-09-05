import uvicorn
from os import environ

if __name__ == "__main__":

    config = { 'app_host': '0.0.0.0', 'app_port': 8080 }

    if 'APP_API_HOST' in environ:
        config['app_host'] = environ['APP_API_HOST']
    if 'APP_API_PORT' in environ:
        config['app_port'] = environ['APP_API_PORT']

    uvicorn.run("main:app", host=config['app_host'], port=int(config['app_port']), reload=True)
