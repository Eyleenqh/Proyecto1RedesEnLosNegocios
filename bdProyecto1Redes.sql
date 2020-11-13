CREATE DATABASE bdRedes;
use bdRedes;

CREATE TABLE archivosPeligrosos(
	id int primary key  AUTO_INCREMENT,
	nombre varchar(100) not null,
	firma varchar(200) not null
);

CREATE  TABLE clientes(
	id int primary key AUTO_INCREMENT,
	direccionIp varchar(50) not null
);

CREATE TABLE cliente_archivo(
	id int primary key AUTO_INCREMENT,
	idCliente int not null,
	idArchivoPeligroso int not null
);

insert into archivosPeligrosos(nombre, firma) values ('1+Sirenas.pdf','734d5358b80246d38e9601d6812ec4ec');
insert into archivosPeligrosos(nombre, firma) values ('10 metodoPlanInformatico-20.pdf','9268276aff5cafec239d35dc2db658c6');
insert into archivosPeligrosos(nombre, firma) values ('11 alineamiento-20.pdf','4fb517c7df76703646affdc7545e2f73');
insert into archivosPeligrosos(nombre, firma) values ('2 planificacion2-20.pdf','7e123e04774630e5e50c8dfc5b5672a1');
insert into archivosPeligrosos(nombre, firma) values ('2+Encanto.pdf','6d6452a5ec65c62408cb22af092b831e');
insert into archivosPeligrosos(nombre, firma) values ('3 Resumen planificación estrategica-20.pdf','98a5c5674cc97fcc130331fceaedca93');
insert into archivosPeligrosos(nombre, firma) values ('4 ENTORNO-20.pdf','7bfa9bbc007929e1cc1f76dcd0866296');
insert into archivosPeligrosos(nombre, firma) values ('4+Elegía.pdf','69d8c68d4b23ea343a299477f39bf214');
insert into archivosPeligrosos(nombre, firma) values ('5 INSTRUMENTOS  DE ANÁLISIS1-20.pdf','bc954206c5dc36aad6b3978acf41e66f');
insert into archivosPeligrosos(nombre, firma) values ('6 cadenavalor-20.pdf','ebf67901bf70d22833366bce826166d3');
insert into archivosPeligrosos(nombre, firma) values ('7 1VISION Y MISION-20.pdf','a9065a6654609c139ea1e96e9a542fd7');
insert into archivosPeligrosos(nombre, firma) values ('8 2diagnostico-20.pdf','9bd0822790fb98bbb5903b0666040cc6');
insert into archivosPeligrosos(nombre, firma) values ('9 Planificacion Informatica-20.pdf','702ac13ea628e7efd9053dd2ecb0d198');
insert into archivosPeligrosos(nombre, firma) values ('actualizacionbd.sql','9c087bfd9f2ef6795af54e078a327e6f');
insert into archivosPeligrosos(nombre, firma) values ('administracion (1).pdf','0ab1279ab833f9992f70ee7a03196a49');
insert into archivosPeligrosos(nombre, firma) values ('Amanda Hocking-CM3-Olas.pdf','212700a07ff813529379872f4860c88e');
insert into archivosPeligrosos(nombre, firma) values ('BD Redes.txt','c7108df12b5be5783971d7590b362a01');
insert into archivosPeligrosos(nombre, firma) values ('BD SQLite.txt','464dae7f9c8c0b161dfd0228ba9b9afb');
insert into archivosPeligrosos(nombre, firma) values ('bdProyectoRedes.sql','7ec19a95a0af4fe2b4b295c71dce3f8b');
insert into archivosPeligrosos(nombre, firma) values ('casos.txt','d41d8cd98f00b204e9800998ecf8427e');
insert into archivosPeligrosos(nombre, firma) values ('Don Domingo de Don Blas.doc','bf8f36418298d6435af8b406f90a78c8');
insert into archivosPeligrosos(nombre, firma) values ('Doramass.docx','dac85fa93fb170460ca027f0b4f8ea56');
insert into archivosPeligrosos(nombre, firma) values ('El Anticristo.doc','02c6746a63b4e3513619811d7449e953');
insert into archivosPeligrosos(nombre, firma) values ('El Capitan Cap.doc','49b9f79e08cbc78a4095f3e73c37e5a2');
insert into archivosPeligrosos(nombre, firma) values ('El Dueño de las Estrellas.doc','78e4aa5cbca3d3c24caec6591085a6d9');
insert into archivosPeligrosos(nombre, firma) values ('El Examen de Maridos.doc','c2d82060c53a417f6a631d5a21ed0ae5');
insert into archivosPeligrosos(nombre, firma) values ('estructura.png','47b737fed039cf7741a00209ca3ebb5a');
insert into archivosPeligrosos(nombre, firma) values ('Historia de mis Libros.doc','cd4f6a877829b8eb0aaa078757587a50');
insert into archivosPeligrosos(nombre, firma) values ('IF6201 proyecto III.pdf','2913d12c0e497025ae522f40c9837fec');
insert into archivosPeligrosos(nombre, firma) values ('INFORME LABORES DE JULIO 2018 A JULIO 2019 SEDE DEL ATLÁNTICO.pdf','35ecb14fffb5809f7782c2286db1661e');
insert into archivosPeligrosos(nombre, firma) values ('INFORME LABORES2017-2018 (1).pdf','2e2613ff93933365e1363f2262bf8148');
insert into archivosPeligrosos(nombre, firma) values ('Inserts.txt','c47ebfd536583a81a1040a96c43bd2bb');
insert into archivosPeligrosos(nombre, firma) values ('La Buenaventura.doc','712229d3ed72150d9a3550fa4dfc9ad8');
insert into archivosPeligrosos(nombre, firma) values ('La Crueldad por el Honor.doc','1e1237f744a1254d2f14887231b810f0');
insert into archivosPeligrosos(nombre, firma) values ('La Cueva De Salamanca.doc','b58ec629e3cf9882e19c79406a0340d0');
insert into archivosPeligrosos(nombre, firma) values ('La Culpa buscar la Pena y el Agravio la Venganza.doc','ef5052f9e43fce4f9b6f4219ec15d0aa');
insert into archivosPeligrosos(nombre, firma) values ('La Mujer Alta.doc','a8f71299d428cde6ab2c190df62981e5');
insert into archivosPeligrosos(nombre, firma) values ('Links Proyecto Aplicada.txt','529d85c8e3766a59a7d82fb0667335ef');
insert into archivosPeligrosos(nombre, firma) values ('Los Ojos Negros.doc','5492636dd6b8cbb16494d9d60ae6a997');
insert into archivosPeligrosos(nombre, firma) values ('OPES-37-2015 planes.pdf','f61fab2fada5b3cd449402390ab12033');
insert into archivosPeligrosos(nombre, firma) values ('planificacion.pdf','9bd1462a6b01ac701f08c699e7618318');
insert into archivosPeligrosos(nombre, firma) values ('planinformaticotrivinno (1).pdf','239ca26e2ab33dce9efcd046413a2bc9');
insert into archivosPeligrosos(nombre, firma) values ('plan_estrategico_institucional_2018-2020.pdf','586a4e3a4af72ab51d9b570bbfd449a3');
insert into archivosPeligrosos(nombre, firma) values ('PNDIP  2019-2022.pdf','e0cb7b3fbabb46879239fc800e24b8fd');
insert into archivosPeligrosos(nombre, firma) values ('Poryecto 3.txt','dc8600bcf1b8bfba9177ed6dce01aec6');
insert into archivosPeligrosos(nombre, firma) values ('Proyecto de investigación y desarrollo - I.pdf','ebe2a9ae4cf738ef86faaeabeaf1fdf3');
insert into archivosPeligrosos(nombre, firma) values ('psiproc.pdf','ecfe1df23ee1ad2c0802418e9403e24b');
insert into archivosPeligrosos(nombre, firma) values ('script.sql','6367c034ca862f31cb5c618ad68161ef');
insert into archivosPeligrosos(nombre, firma) values ('Tradicion Oral.docx','47484c25cf3e976c3edb45dfe9dfc92c');
insert into archivosPeligrosos(nombre, firma) values ('Vigui.pptx','3dcb95a994ce02922f4773909b436126');

DELIMITER $$
create procedure obtenerArchivosPeligrosos()
BEGIN
	select c.direccionIp, a.nombre , count(*) as cantidadDetecciones from cliente_archivo ca join archivospeligrosos a on a.id = ca.idArchivoPeligroso
join clientes c on c.id = ca.idCliente
GROUP BY ca.idArchivoPeligroso, ca.idCliente ORDER BY c.direccionIp asc;
END$$
DELIMITER ;


/*Datos prueba*/
insert into clientes(direccionIp) values ('123.123.123.54');
insert into clientes(direccionIp) values ('172.196.123.10');

insert into cliente_archivo (idCliente, idArchivoPeligroso) values(1,1);
insert into cliente_archivo (idCliente, idArchivoPeligroso) values(1,2);
insert into cliente_archivo (idCliente, idArchivoPeligroso) values(1,1);
insert into cliente_archivo (idCliente, idArchivoPeligroso) values(1,5);
insert into cliente_archivo (idCliente, idArchivoPeligroso) values(2,1);
insert into cliente_archivo (idCliente, idArchivoPeligroso) values(2,1);
insert into cliente_archivo (idCliente, idArchivoPeligroso) values(2,3);

select * from archivosPeligrosos;
select * from cliente_archivo;
select * from clientes;
call obtenerArchivosPeligrosos
