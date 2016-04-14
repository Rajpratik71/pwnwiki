### Serving pwnwiki content locally using Docker:

Using [Docker](https://www.docker.com) on Linux, Mac OS X, or Windows, you can create a container
that serves the pwnwiki content with a full web server (in this case, using `nginx`) that is running
locally requiring no network access (or allowing your red team to access the files on a local VLAN
by setting up your own addressing/routing rules.)

To do this with native Linux Docker, Docker for Mac<sup>2</sup>, or Docker for Windows<sup>2</sup>, follow these steps:

  1. If you are just starting out, after cloning this repo you can build a Docker container
     using the included ``Dockerfile``:


         $ docker build --build-arg AUTHOR=$USER -t pwnwiki .
         Sending build context to Docker daemon 2.756 MB
         Step 1 : FROM nginx
          ---> eb4a127a1188
         Step 2 : ARG AUTHOR
          ---> Running in c67365cb04bc
          ---> d296e2400018
         Removing intermediate container c67365cb04bc
         Step 3 : ENV AUTHOR $AUTHOR
          ---> Running in 42ed09005251
          ---> e154c0d18452
         Removing intermediate container 42ed09005251
         Step 4 : WORKDIR /usr/share/nginx/html
          ---> Running in 492e89bad75f
          ---> 05e768762146
         Removing intermediate container 492e89bad75f
         Step 5 : COPY . /usr/share/nginx/html
          ---> fe0ca06ed4eb
         Removing intermediate container 3c97e45d4fc7
         Step 6 : CMD nginx -g 'daemon off;'
          ---> Running in 374cfeee7e49
          ---> 8817fb6fdcc1
         Removing intermediate container 374cfeee7e49
         Step 7 : EXPOSE 80
          ---> Running in 3f0a44a85240
          ---> 532d0daa82d9
         Removing intermediate container 3f0a44a85240
         Successfully built 532d0daa82d9
    
  2. Run the container, mapping port `80` to some random high-numbered port:

         $ docker run -d -p 1337:80 --name pwnwiki pwnwiki
         bf4cec957eb6a66142ae993d741213176c621f547a705d2f5747ded1619f4d21
         $ docker ps
         CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                           NAMES
         bf4cec957eb6        pwnwiki             "/bin/sh -c 'nginx -g"   3 seconds ago       Up 1 seconds        443/tcp, 0.0.0.0:1337->80/tcp   pwnwiki```

  3. Open a browser to the port you chose on `localhost` (or `127.0.0.1`). On a Mac with Docker for Mac, you can do:

     ```$ open http://127.0.0.1:1337/```

     ![pwnwiki from Docker container](images/docker-pwnwiki.png)

  4. You can stop the container with: `docker kill pwnwiki` or `docker stop pwnwiki`

  5. Restart the container with: `docker restart pwnwiki`

  6. Remove the container with: `docker rm pwnwiki`

There is a [helper script](pwnwiki) to perform these steps. Just run `./pwnwiki` from a shell prompt.

[Footnote 2]: Using Docker Machine will also work on Mac or Windows, but you will have to go
through an extra step to determine the IP address to use to get to the `nginx`
server in the Docker container. These instructions assume use of the native
Docker for Mac or Docker for Windows apps.

