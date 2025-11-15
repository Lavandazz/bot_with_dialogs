from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "role" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "role" VARCHAR(30) NOT NULL DEFAULT 'user'
);
COMMENT ON TABLE "role" IS 'Модель для создания ролей';
        CREATE TABLE IF NOT EXISTS "status" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "banned" INT NOT NULL DEFAULT 0,
    "user_id_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "status" IS 'Статус пользователя.';
        ALTER TABLE "users" DROP COLUMN "role";
        ALTER TABLE "users" DROP COLUMN "status";
        CREATE TABLE IF NOT EXISTS "userrole" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "role_id" INT NOT NULL REFERENCES "role" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "userrole" IS 'Связь пользователя и роли';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "role" VARCHAR(20) NOT NULL DEFAULT 'user';
        ALTER TABLE "users" ADD "status" VARCHAR(20) NOT NULL DEFAULT 'active';
        DROP TABLE IF EXISTS "userrole";
        DROP TABLE IF EXISTS "status";
        DROP TABLE IF EXISTS "role";"""
