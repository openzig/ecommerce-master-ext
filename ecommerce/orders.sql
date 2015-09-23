BEGIN;
CREATE TABLE "orders_order" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" integer REFERENCES "auth_user" ("id"),
    "order_id" varchar(120) NOT NULL UNIQUE,
    "cart_id" integer NOT NULL REFERENCES "carts_cart" ("id"),
    "status" varchar(120) NOT NULL,
    "shipping_address_id" integer NOT NULL REFERENCES "accounts_useraddress" ("id"),
    "billing_address_id" integer NOT NULL REFERENCES "accounts_useraddress" ("id"),
    "sub_total" decimal NOT NULL,
    "tax_total" decimal NOT NULL,
    "final_total" decimal NOT NULL,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL
)
;
CREATE INDEX "orders_order_6340c63c" ON "orders_order" ("user_id");
CREATE INDEX "orders_order_8a7b7230" ON "orders_order" ("cart_id");
CREATE INDEX "orders_order_9d06984a" ON "orders_order" ("shipping_address_id");
CREATE INDEX "orders_order_6bc022d9" ON "orders_order" ("billing_address_id");

COMMIT;
