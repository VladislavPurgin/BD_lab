--Hash

DROP INDEX IF EXISTS "hash_index_id_rs";
CREATE INDEX "hash_index_id_rs" ON "Railway_station" USING hash("id_rs");

SELECT COUNT(*) FROM "Railway_station" WHERE id_rs % 2 = 0;

SELECT COUNT(*) FROM "Railway_station" WHERE name = 'modern' ;

SELECT AVG("id_rs") FROM "Railway_station" WHERE name = 'modern' AND name = 'free' and name = 'white';

SELECT SUM("id_rs"), MAX("id_rs") FROM "Railway_station" WHERE id_rs < 12000 GROUP BY id_rs % 2;


--BRIN

DROP INDEX if exists name_brin_index;
CREATE INDEX name_brin_index ON "Railway_station" USING brin (name) WITH(pages_per_range=128);

select COUNT(*) from "Railway_station" where name  = 'modern' ;

select count(name) from "Railway_station" where name  != 'modern';

select count(*) from "Railway_station" where name  = 'modern' and name  = 'free' and name  = 'white';

select count(name) from "Railway_station" where name  != 'modern' and name  != 'free' and name  != 'white' and name  != 'bad';
