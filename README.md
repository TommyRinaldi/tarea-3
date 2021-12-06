# tarea-3
La tarea está basada en los códigos y/o comandos de la ayudantía
1. Instalar nginx en caso de no tenerlo instalado, luego editar el archivo de configuración nginx.conf ubicado en etc/nginx y agregar el archivo de configuración "configuracion.conf" como en ayudantía
2. Luego con docker instalado usar los siguientes comandos paraa crear la base de datos master y la slave
  sudo docker run -dti -p 55432:5432 --name postgresql-master \
  -e POSTGRESQL_REPLICATION_MODE=master \
  -e POSTGRESQL_USERNAME=my_user \
  -e POSTGRESQL_PASSWORD=password123 \
  -e POSTGRESQL_DATABASE=my_database \
  -e POSTGRESQL_REPLICATION_USER=my_repl_user \
  -e POSTGRESQL_REPLICATION_PASSWORD=my_repl_password \
  bitnami/postgresql:latest**
  
  sudo docker run -dti -p 65432:5432 --name postgresql-slave \
  --link postgresql-master:master \
  -e POSTGRESQL_REPLICATION_MODE=slave \
  -e POSTGRESQL_USERNAME=my_user \
  -e POSTGRESQL_PASSWORD=password123\
  -e POSTGRESQL_MASTER_HOST=master \
  -e POSTGRESQL_MASTER_PORT_NUMBER=5432 \
  -e POSTGRESQL_REPLICATION_USER=my_repl_user \
  -e POSTGRESQL_REPLICATION_PASSWORD=my_repl_password \
  bitnami/postgresql:latest
  
3. Luego crear en la base de datos por defecto postgres la tabla "tabla" con las columnas "numero" correpsndiente a un integer y la columna "string" correspondiente a un varchar
4. Ejecutar en tres terminales flask run --port 3000, flask run --port 3001 y flask run --port 3002 respectivamente
5. Abrir un navegador en localhost/inventario
