drop table if exists ruuvitagData;
create table ruuvitagData (
id integer primary key autoincrement,
temperature integer,
pressure integar,
humidity integer,
ruuvitagId text not null,
timestamp Datetime not null
);