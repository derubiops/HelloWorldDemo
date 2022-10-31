# ANSWERS.md

- How long did it take to finish the test?

  - I needed around 5-6 hours along two days. Creating documentation with care is always time consuming :)

- If you had more time, how could you improve your solution?

  - I would try figure out if would be possible to shrink even more the image size for both containers, to reduce the footprint.

- What changes would you do to your solution to be deployed in a production environment?

  - I would create a valid certificate (not self-signed) and bind it to a real domain.

  - Avoid exposing the application directly removing the binding to port 8080 in docker-compose file. That way the application would be accessible only via nginx.

  - At nginx level, as a good practice is recommended to disable some SSL protocols (TLSv1.0, SSLv3, SSLv2) and configure only secure ciphers.

- Why did you choose this language over others?

  - I have chosen Python for the app as it provides simplicity and readability for this particular purpose.

- What was the most challenging part and why?

  - I got stuck for some time configuring the nginx as a reverse proxy, as this is something that I do not do on a daily basis and I needed some learning and practice until I got it working. However, the SSL part was pretty straightforward.
