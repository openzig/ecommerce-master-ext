BEGIN;
CREATE TABLE "carts_cartitem_variations" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "cartitem_id" integer NOT NULL,
    "variation_id" integer NOT NULL REFERENCES "products_variation" ("id"),
    UNIQUE ("cartitem_id", "variation_id")
)
;
CREATE TABLE "carts_cartitem" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "cart_id" integer,
    "product_id" integer NOT NULL REFERENCES "products_product" ("id"),
    "quantity" integer NOT NULL,
    "line_total" decimal NOT NULL,
    "notes" text,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL
)
;
CREATE TABLE "carts_cart" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "total" decimal NOT NULL,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL,
    "active" bool NOT NULL
)
;
CREATE INDEX "carts_cartitem_variations_56694d3f" ON "carts_cartitem_variations" ("cartitem_id");
CREATE INDEX "carts_cartitem_variations_e3f47db4" ON "carts_cartitem_variations" ("variation_id");
CREATE INDEX "carts_cartitem_8a7b7230" ON "carts_cartitem" ("cart_id");
CREATE INDEX "carts_cartitem_7f1b40ad" ON "carts_cartitem" ("product_id");

COMMIT;
