## Millenium

Running `Apache Tomcat/8.5.64`

```
java.lang.IllegalArgumentException: Invalid character found in the request target [/members.asp?nction%20x(){v%20=%22]. The valid characters are defined in RFC 7230 and RFC 3986
	org.apache.coyote.http11.Http11InputBuffer.parseRequestLine(Http11InputBuffer.java:504)
	org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:503)
	org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
	org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:831)
	org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1629)
	org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
	java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
	java.lang.Thread.run(Thread.java:748)
```

/doSignin

```
Type Exception Report

Description The server encountered an unexpected condition that prevented it from fulfilling the request.

Exception

java.lang.NullPointerException
	SignIn.service(SignIn.java:26)
	javax.servlet.http.HttpServlet.service(HttpServlet.java:733)
	org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:52)

Note The full stack trace of the root cause is available in the server logs.
```

`/?err=Invalid_Credentials`

`Cookie: JSESSIONID=B1A763938E7F8026AE279906A20F0D96`

Can login with admin admin!

### Worm

/doLaunch

`country=asasdsada&worm=rO0ABXQAE3snd29ybSc6J2Rlbl96dWtvJ30%3D`=> `¬í t {'worm':'den_zuko'}`

worm	"rO0ABXQAFXsnd29ybSA6ICdtaWxsZW5pdW0nfQ==" => 

Tries to find string...