BEGIN;
CREATE TABLE "marketing_marketingmessage" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "message" varchar(120) NOT NULL,
    "active" bool NOT NULL,
    "featured" bool NOT NULL,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL,
    "start_date" datetime,
    "end_date" datetime
)
;
CREATE TABLE "marketing_slider" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "image" varchar(100) NOT NULL,
    "order" integer NOT NULL,
    "url_link" varchar(250),
    "header_text" varchar(120),
    "text" varchar(120),
    "active" bool NOT NULL,
    "featured" bool NOT NULL,
    "timestamp" datetime NOT NULL,
    "updated" datetime NOT NULL,
    "start_date" datetime,
    "end_date" datetime
)
;

COMMIT;
