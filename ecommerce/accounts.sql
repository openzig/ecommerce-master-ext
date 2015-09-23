BEGIN;
CREATE TABLE "accounts_userdefaultaddress" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"),
    "shipping_id" integer,
    "billing_id" integer
)
;
CREATE TABLE "accounts_useraddress" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "address" varchar(120) NOT NULL,
    "address2" varchar(120),
    "city" varchar(120) NOT NULL,
    "state" varchar(120),
    "country" varchar(120) NOT NULL,
    "zipcode" varchar(25) NOT NULL,
    "phone" varchar(120) NOT NULL,
    "shipping" bool NOT NULL,
    "billing" bool NOT NULL,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL
)
;
CREATE TABLE "accounts_userstripe" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"),
    "stripe_id" varchar(120)
)
;
CREATE TABLE "accounts_emailconfirmed" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"),
    "activation_key" varchar(200) NOT NULL,
    "confirmed" bool NOT NULL
)
;
CREATE TABLE "accounts_emailmarketingsignup" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "email" varchar(254) NOT NULL,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL
)
;
CREATE INDEX "accounts_userdefaultaddress_85061455" ON "accounts_userdefaultaddress" ("shipping_id");
CREATE INDEX "accounts_userdefaultaddress_95d2df3c" ON "accounts_userdefaultaddress" ("billing_id");
CREATE INDEX "accounts_useraddress_6340c63c" ON "accounts_useraddress" ("user_id");

COMMIT;
