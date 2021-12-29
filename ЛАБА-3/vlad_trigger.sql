--after delete, insert

CREATE TABLE "train"(
"train_id" serial PRIMARY KEY,
"train_model" text,
"train_count" int
);

CREATE TABLE "train_log"(
"id" serial PRIMARY KEY,
"train_log_id" int,
"train_log_model_name" text
);

INSERT INTO "train"("train_model", "train_count")
VALUES ('train1' , '10'), ('train2', '20'), ('train3', '30'), ('train4', '40'),
('train5', '50');




CREATE OR REPLACE FUNCTION after_delete_insert_func() RETURNS TRIGGER as $trigger$
DECLARE
	
BEGIN
	IF new."train_count" <= 30 THEN
		RAISE NOTICE 'train_count <= 30';
		INSERT INTO "train_log"("train_log_id", "train_log_model_name") VALUES (new."train_id", new."train_model" || '_small');
		RETURN NEW;
	ELSE
		RAISE NOTICE 'train_count >= 30';
		INSERT INTO "train_log"("train_log_id", "train_log_model_name") VALUES (new."train_id", new."train_model" || '_big');
		RETURN NEW;
	END IF;

END;
$trigger$ LANGUAGE plpgsql;

CREATE TRIGGER "after_delete_insert_trigger"
AFTER DELETE OR INSERT ON "train"
FOR EACH ROW
EXECUTE procedure after_delete_insert_func(); 



DELETE FROM "train" where "train_id" = 4;

INSERT INTO "train"("train_model", "train_count") VALUES ('model6', '6') ;
