# Make file for swagger 
SOURCE_YAML_FILE=lambda.yml
SWAGGER_ROOT=~/swagger


service: 
	swagger-codegen generate \
	-i $SWAGGER_ROOT/$SOURCE_YAML_FILE \
	-l python-flask \
	-o $SWAGGER_ROOT/server/lambda/flaskConnexion \
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
	#open abstract.pdf
	rm -fR $SWAGGER_ROOT


