from flask_sqlalchemy import SQLAlchemy


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ShopNice_App:CoutPrin@DESKTOPA26VGM9:3306/my_new_database'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODiFICATIONs = False 
