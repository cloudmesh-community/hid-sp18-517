# Make file for swagger 
# define macros

#SWAGGER_CODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
SWAGGER_CODEGEN=java -jar swagger-codegen-cli.jar 
SOURCE_YAML_FILE=fileupload.yml
SWAGGER_ROOT=.
FLASK_APP_PATH=server/fileupload/flaskConnexion

container:
	# Add docker commands
	sudo docker build -t cloudmesh-fileupload .
	sudo docker run -p 8080:8080 cloudmesh-fileupload 
service: 
	
	pip install -r requirements.txt
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar	
	${SWAGGER_CODEGEN} generate \
	-i ${SWAGGER_ROOT}/${SOURCE_YAML_FILE} \
	-l python-flask \
	-o ${SWAGGER_ROOT}/${FLASK_APP_PATH} \
	-D supportPython2=true

	cp -r *.py ${FLASK_APP_PATH}/swagger_server/controllers/
	

start:
	cd ${SWAGGER_ROOT}/${FLASK_APP_PATH};python -m swagger_server
	#/usr/bin/python -m swagger_server
test:
	touch samplefile.txt
	curl -X POST "http://localhost:8080/api/upload" -H  "accept: multipart/form-data" -H  "Content-Type: multipart/form-data" -F "file_name=@samplefile.txt;type=text/markdown"


stop:
	#mkdir dest  
	ps -ef | egrep 'swagger_server'  | grep -v grep | awk '{print $$2}' | xargs kill -9

clean:
	#stop process and remove the swagger root directory
	#ps -ef | egrep 'swagger_server'  | grep -v grep | awk '{print $$2}' | xargs kill -9
	rm -fR ${SWAGGER_ROOT}/server


