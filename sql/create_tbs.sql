CREATE TABLESPACE tbs_default
  DATAFILE 'tbs_perm_01.dat' 
    SIZE 20M
  ONLINE;

CREATE TABLESPACE tbs_autoextend
  DATAFILE 'tbs_perm_02.dat' 
    SIZE 10M
    REUSE
    AUTOEXTEND ON NEXT 10M MAXSIZE 200M;

CREATE TEMPORARY TABLESPACE tbs_tempo
  TEMPFILE 'tbs_temp_02.dbf'
    SIZE 10M
    AUTOEXTEND OFF;

CREATE TEMPORARY TABLESPACE tbs_tempo_autoextend
  TEMPFILE 'tbs_temp_01.dbf'
    SIZE 5M
    AUTOEXTEND ON;


-- TABLESPACE TBS_DEFAULT created.
-- TABLESPACE TBS_AUTOEXTEND created.
-- TABLESPACE TBS_TEMPO_AUTOEXTEND created.
-- TABLESPACE TBS_TEMPO created.

