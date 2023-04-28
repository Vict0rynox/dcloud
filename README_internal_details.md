### From Kubernetes to localhost

For exact code check [init_cmd.sh](scripts/init_cmd.sh)

Start open-ssh server(dcloud-bastion)(with user public key) (service/deployment) in kubernetes

Reverse ssh localhost with dcloud-bastion (bastion-egress-proxy container)

This allow traffic from kubernetes pod to be send to localhost

### From localhost to Kubernetes

We achieve this via overrides in host, so all registered istio services names(like a,b,c in demo target to localhost)

kubectl port-forward with dcloud-bastion (bastion-ingress-proxy container)

bastion-ingress-proxy container is simple nginx server that proxy to target based on HOST header value
