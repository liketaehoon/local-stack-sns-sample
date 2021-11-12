# local-stack-sns-sample
- Local Stack을 이용해 SNS 개발 환경 구축 테스트를 설명 한다.

### local stack start
```bash
cd local_setting
docker compose up
```
### serverless start
```bash
npm install
serverless offline start --stage local
```

### test
```bash
curl localhost:3000/local/trigger
```