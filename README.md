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
-- TODO write scripts here

##### Deploy all applications into cloud 
-- TODO write scripts here
-- should be simple kubectl apply 

##### Validate all work in cloud
-- TODO write scripts here
-- kubectl port-forward ...
-- curl .... /a /ab /abc

##### Start 'b' on localhost
-- TODO write scripts here

##### How to register 'b' on localhost and how it unregister 'b' in cloud
-- TODO write scripts here


