
echo "############# start dcloud istio services override to localhost #############"
kubectl exec $(kubectl get -A pods --selector=istio=pilot -o jsonpath='{.items[*].metadata.name}') \
  -n $(kubectl get -A pods --selector=istio=pilot -o jsonpath='{.items[*].metadata.namespace}') \
  -c discovery -- curl -s 'localhost:15014/debug/registryz' |
  jq -r '.[].Attributes.Name' |
  while read d; do echo "$d 127.0.0.1"; done
echo "############# end dcloud istio services override to localhost #############"
