BEGIN;
CREATE TABLE "products_category" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(120) NOT NULL,
    "description" text,
    "slug" varchar(50) NOT NULL UNIQUE,
    "featured" bool NOT NULL,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL,
    "active" bool NOT NULL
)
;
CREATE TABLE "products_product_category" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "product_id" integer NOT NULL,
    "category_id" integer NOT NULL REFERENCES "products_category" ("id"),
    UNIQUE ("product_id", "category_id")
)
;
CREATE TABLE "products_product" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(120) NOT NULL,
    "description" text,
    "price" decimal NOT NULL,
    "sale_price" decimal,
    "slug" varchar(50) NOT NULL UNIQUE,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL,
    "active" bool NOT NULL,
    "update_defaults" bool NOT NULL,
    UNIQUE ("title", "slug")
)
;
CREATE TABLE "products_productimage" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "product_id" integer NOT NULL REFERENCES "products_product" ("id"),
    "image" varchar(100) NOT NULL,
    "featured" bool NOT NULL,
    "thumbnail" bool NOT NULL,
    "active" bool NOT NULL,
    "updated" datetime NOT NULL
)
;
CREATE TABLE "products_variation" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "product_id" integer NOT NULL REFERENCES "products_product" ("id"),
    "category" varchar(120) NOT NULL,
    "title" varchar(120) NOT NULL,
    "image_id" integer REFERENCES "products_productimage" ("id"),
    "price" decimal,
    "updated" datetime NOT NULL,
    "active" bool NOT NULL
)
;
CREATE INDEX "products_product_category_7f1b40ad" ON "products_product_category" ("product_id");
CREATE INDEX "products_product_category_6f33f001" ON "products_product_category" ("category_id");
CREATE INDEX "products_productimage_7f1b40ad" ON "products_productimage" ("product_id");
CREATE INDEX "products_variation_7f1b40ad" ON "products_variation" ("product_id");
CREATE INDEX "products_variation_06df7330" ON "products_variation" ("image_id");

COMMIT;
