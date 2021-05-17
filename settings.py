import db


DATABASE_BACKEND = db.MemoryDatabase

# For Redis Backend
# DATABASE_BACKEND = db.RedisDatabase

DATABASE_CONNECTION = DATABASE_BACKEND()
