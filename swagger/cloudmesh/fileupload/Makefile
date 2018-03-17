# Make file for swagger 
# define macros
SWAGGER_CODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
SOURCE_YAML_FILE=fileupload.yml
SWAGGER_ROOT=./swagger
FLASK_APP_PATH=server/fileupload/flaskConnexion

container:
	# Add docker commands
service: 
	
	#pip install -r requirements.txt
	
	${SWAGGER_CODEGEN} generate \
	-i ${SWAGGER_ROOT}/${SOURCE_YAML_FILE} \
	-l python-flask \
	-o ${SWAGGER_ROOT}/${FLASK_APP_PATH} \
	-D supportPython2=true
	

start:
	cd ${SWAGGER_ROOT}/${FLASK_APP_PATH}
	python -m swagger_server
test:
	touch samplefile.txt
	curl -X POST "http://localhost:8080/api/upload" -H  "accept: multipart/form-data" -H  "Content-Type: multipart/form-data" -F "file_name=@samplefile.txt;type=text/markdown"


stop:
	#mkdir dest  
	ps -ef | egrep 'swagger_server'  | grep -v grep | awk '{print $2}' | xargs kill -9

clean:
	#stop process and remove the swagger root directory
	#ps -ef | egrep 'swagger_server'  | grep -v grep | awk '{print $2}' | xargs kill -9
	stop
	rm -fR $SWAGGER_ROOT


