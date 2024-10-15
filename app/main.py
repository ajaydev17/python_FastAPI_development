# import the modules
from fastapi import FastAPI
import logging
import logging.config
from app.routers import category_routes

# logger settings
# logging.basicConfig(level=logging.DEBUG)

# select the logging info from a file
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# defining the logger
logger = logging.getLogger(__name__)

# create a fastapi server
app = FastAPI()


# api routes definition and handlers
# @app.get('/')
# async def read_root():
#     try:
#         # raising an exception
#         raise Exception('Simulated debug error occurred!!')
#     except Exception as e:
#         # logging the exception at the debug level
#         # logging.debug(f"An exception occurred: {e}")
#
#         # logging the full traceback if needed
#         # logging.debug('Exception traceback: ', exc_info=True)
#
#         # logging the error using logger logging
#         logger.error(f"An exception occurred: {e}")
#         logger.error('Exception traceback: ', exc_info=True)
#
#     return {'message': 'Hello, World!!'}

# include all the routes
app.include_router(category_routes.router, prefix='/api/category', tags=['categories'])
