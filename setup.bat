
set API_NAME=api
set REGION=us-east-1
set STAGE=test

awslocal lambda create-function --region %REGION% --function-name %API_NAME% --runtime nodejs8.10 --handler lambda.apiHandler --memory-size 128 --zip-file fileb://%API_NAME%-handler.zip --role arn:aws:iam::123456:role/irrelevant




awslocal apigateway create-rest-%API_NAME% --region %REGION% --name %API_NAME%

awslocal lambda list-functions --query "Functions[?FunctionName==`%API_NAME%`].FunctionArn" --output text --region %REGION%

awslocal lambda list-functions --query "Functions[?FunctionName=='%API_NAME%'].FunctionArn" --output text --region %REGION%


arn=arn:aws:lambda:%REGION%:000000000000:function:%API_NAME%



awslocal apigateway get-rest-apis --query "items[?name=='%API_NAME%'].id" --output text --region %REGION%


id=64qwdemnxi


awslocal apigateway get-resources --rest-%API_NAME%-id 9632kgflpn --query 'items[?path==`/`].id' --output text --region %REGION%

res_id=z0342by1lo



awslocal apigateway put-method --region %REGION% --rest-%API_NAME%-id 9632kgflpn --resource-id wx9sjqd5sn --http-method GET --request-parameters "method.request.path.somethingId=true" --authorization-type "NONE" 


awslocal apigateway put-integration --region %REGION% --rest-%API_NAME%-id 9632kgflpn --resource-id wx9sjqd5sn --http-method GET --type AWS_PROXY --integration-http-method POST --uri arn:aws:apigateway:%REGION%:lambda:path/2015-03-31/functions/arn:aws:lambda:%REGION%:000000000000:function:a/invocations --passthrough-behavior WHEN_NO_MATCH 




awslocal apigateway create-deployment --region %REGION% --rest-%API_NAME%-id 9632kgflpn --stage-name %STAGE%










