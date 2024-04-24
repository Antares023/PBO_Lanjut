create table jadwal(
id serial primary key not null,
kd_mk varchar(10) unique not null,
mk varchar(50) not null,
kelas varchar(20) not null,
dosen varchar(50) not null);