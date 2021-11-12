#sleep 30
# awslocal 호출 --endpoint-url=http://localstack:4566 생략 가능
# localstack 은 docker-compose service 이름인데, 여기에 밑줄이 있으면 네트워크 접속이 안됐음.
# regtion 은 DEFAULT_REGION=ap-northeast-2 으로 자동 지정됨.
 
echo "## creating topics"
awslocal sns create-topic --name my-sns 