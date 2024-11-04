
.PHONY: build microservice_a microservice_b microservice_c

build: microservice_a microservice_b microservice_c

deploy:
	kubectl apply -f deployment/kubernetes/applications/a/
	kubectl apply -f deployment/kubernetes/applications/b/
	kubectl apply -f deployment/kubernetes/applications/c/

microservice_a:
	cd microservice/a && docker build -t a . && cd ../..

microservice_b:
	cd microservice/b && docker build -t b . && cd ../..

microservice_c:
	cd microservice/c && docker build -t c . && cd ../..


deploy_utils:
	kubectl apply -f deployment/kubernetes/utils


ping:
	kubectl exec -it $(kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep curl-test) -c curl-test curl http://a:8080/abc