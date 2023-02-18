from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps.mainapp.routes import api_router


def create_app(debug=True):
    app = FastAPI(debug=debug)
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(api_router)
    return app

# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware
#
# from .apps import authapp
# from game_blog.apps.mainapp.routes import router
#
# from .database import engine
# from .apps.postapp import models
#
# game_blog.apps.users.models.Base.metadata.create_all(bind=engine)
# game_blog.apps.posts.models.Base.metadata.create_all(bind=engine)
#
#
# def create_app(debug=True):
#     app = FastAPI(debug=debug)
#
#     origins = [
#         "http://localhost:3000",
#         "localhost:3000"
#     ]
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=origins,
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"]
#     )
#     app.mount('/static', StaticFiles(directory='game_blog/static'),
#               name='static')
#     app.include_router(router)
#     return app
