### DCloud (Dev Cloud)

##### Goal
With Istio and Kubernetes be able to launch some service(s) on localhost when all others are in cloud

##### Project example microservices:
- a (routes  /a /ab /abc)
- b (routes  /b /bc )
- c (routes  /c )

##### Goal
- 'a' and 'c' in kubernetes
- 'b' on localhost
- port-forward 'a' and call route /abc, this will validate our flow
  ```'a'(in cloud) -> 'b'(localhost) -> 'c'(in cloud)```

###### routes explained based on microservice 'a'
- /a  -> response data directly from microservice 'a'</br>
```
{ 
  "a": "hello from a"
}
```
- /ab -> also call 'b' via route /b, json response from 'b' merged with our data </br>
```
{ 
  "a": "hello from a", 
  "b": "hello from b"
}
```
- /abc -> also call 'b' via route /bc, response from 'b' merged with our data('b' call 'c' /c and merge response) </br>
```
{ 
  "a": "hello from a", 
  "b": "hello from b", 
  "c": "hello from c"
}
```


#### Development

##### Prerequisites
- Required environment variables
```DCLOUD_PUBLIC_KEY```
```DCLOUD_USER_EMAIL```

##### Kubernetes/Minikube Istio setup 
- [historical issue, may be not relevant now](https://stackoverflow.com/questions/72073613/istio-installation-failed-apple-silicon-m1)
- [install istioctl](https://istio.io/latest/docs/setup/install/istioctl/)
- ```istioctl install``` ( I got docker pull issue from local docker desktop kubernetes, describe failed pod and pull image manually )
- ```istioctl operator init --hub=ghcr.io/resf/istio```
- ```
  kubectl apply -f - <<EOF
  apiVersion: install.istio.io/v1alpha1
  kind: IstioOperator
  metadata:
    namespace: istio-system
    name: example-istiocontrolplane
  spec:
    hub: ghcr.io/resf/istio
    profile: demo
  EOF
- ```kubectl apply -f ${ISTIO_HOME}/samples/addons/```

##### Build docker images
- ```cd images/bastion && docker build -t bastion . && cd ../..```
- ```cd microservice/a && docker build -t a . && cd ../..```
- ```cd microservice/b && docker build -t b . && cd ../..```
- ```cd microservice/c && docker build -t c . && cd ../..```

##### Deploy applications into cloud
- ```kubectl apply -f deployment/kubernetes/applications/a/```
- ```kubectl apply -f deployment/kubernetes/applications/b/```
- ```kubectl apply -f deployment/kubernetes/applications/c/```

##### Deploy bastion tools into cloud
### TODO dkuzkin how to put public ssh key into deployment
- ```kubectl apply -f deployment/kubernetes/dcloud/```

##### Usage of bastion tools
###### Allow incoming requests from kubernetes bastion reverse-ssh pod to localhost
###### terminal 1
- ```kubectl port-forward svc/dcloud-app-user-1 2222```
###### terminal 2
- ```ssh -p 2222 -N -R 9000:127.0.0.1:8080 admin@127.0.0.1```
###### simple validate we are able to connect to localhost from kubernetes
- Run microservice/a/app/run.py 
- ```kubectl apply -f deployment/kubernetes/applications/test```
- ```kubectl exec -it $(kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep curl-test) -c curl-test curl http://dcloud-app-user-1:9000/a```

#### Allow outcoming requests from localhost to bastion proxy pod
- /etc/hosts should be enriched with istio services to be routed on localhost ( this is more simple than use Dnsmasq, anyway sudo required )
- [retrieve list of istio registered services](/scripts/istio_services_list.sh)
- execute ```sudo vi /etc/hosts``` and add all istio registered services
- ```cd images/bastion-ingress-proxy && docker build -t bastion-ingress-proxy . && cd ../..```
- TODO dkuzkin kubectl apply for bastion-ingress-proxy
- TODO dkuzkin curl example
  kubectl exec -it $(kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep curl-test) -c curl-test curl -H "HOST: google.com" http://bastion-ingress-proxy:8080
- 
- kubectl exec -it $(kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep bastion-ingress-proxy) -c bastion-ingress-proxy /bin/sh
- 
- curl -H "HOST: google.com" http://bastion-ingress-proxy:8080
- TODO otyschenko
- ```kubectl port-forward svc/dcloud-app-user-1 2221```

##### Validate all work in cloud
-- TODO write scripts here
-- kubectl port-forward ...
-- curl .... /a /ab /abc

##### Start 'b' on localhost
-- TODO write scripts here

##### How to register 'b' on localhost and how it unregister 'b' in cloud
-- TODO write scripts here


