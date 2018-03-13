# Make file for swagger 
# define macros
SWAGGER_CODEGEN=java -jar lib/swagger-codegen-cli.jar
SOURCE_YAML_FILE=lambda.yml
SWAGGER_ROOT=~/swagger
FLASK_APP_PATH=server/lambda/flaskConnexion
container:

service: 
	
	pip install -r requirements.txt
	
	${SWAGGER_CODEGEN} generate \
	-i $SWAGGER_ROOT/$SOURCE_YAML_FILE \
	-l python-flask \
	-o ${SWAGGER_ROOT}/${FLASK_APP_PATH} \
	-D supportPython2=true
	

start:
	python -m swagger_server
test:
	#rm -f	*.pdf *.bbl *.log *.blg *.aux *.out *.idx *.run.xml *.bcf
	#rm -rf $SWAGGER_ROOT
	curl -X POST "http://localhost:8080/api/upload" -H  "accept: multipart/form-data" -H  "Content-Type: multipart/form-data" -F "file_name=@README.md;type=text/markdown"


stop:
	#mkdir dest  
	ps -ef | egrep 'swagger_server'  | grep -v grep | awk '{print $2}' | xargs kill -9

clean:
	#stop process and remove the swagger root directory
	#ps -ef | egrep 'swagger_server'  | grep -v grep | awk '{print $2}' | xargs kill -9
	stop
	rm -fR $SWAGGER_ROOT



