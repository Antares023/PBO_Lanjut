create table mahasiswa(
id serial primary key not null,
nim varchar(10) unique not null,
nama varchar(50) not null,
jk varchar(1) not null,
kode_prodi varchar(10) not null);