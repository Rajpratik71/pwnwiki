**PwnWiki.io** - __The notes section of the pentesters mind.__

This is a collection TTPs (tools, tactics, and procedures) for what to do after access has been gained to victim systems during the course of performing penetration/red team testing.

- - - - - -
### Live Online Copy:
You can find a copy of the project online at: http://PwnWiki.io

### Offline Use:
This is the really cool thing about this wiki: when you do a ```git clone``` of it you get a full wiki on your local system. Do you work on a network that has no Internet access? We gotcha covered.

  1. Clone the repository or pull the archive ([download zip](https://github.com/pwnwiki/pwnwiki.github.io/archive/master.zip)) of the repo
  2. Open index.html
  3. Most modern browsers don't allow the access of local files from a locally loaded HTML file. On Windows you can use [Mongoose Tiny](http://cesanta.com/downloads.html) or [HFS](http://www.rejetto.com/hfs/) to host the files locally. On OSX and Linux `python -m SimpleHTTPServer` seems to work just fine.

**Referenced tools can be found here: https://github.com/mubix/post-exploitation (If they aren't built into the OS).**

If you have Docker installed, you can run an nginx container to serve the pwnwiki files locally.

  1. If you are just starting out, after cloning this repo you can build a Docker container
     using the included ``Dockerfile``:

     ```$ docker build --build-arg AUTHOR=$USER -t pwnwiki .
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
     Successfully built 532d0daa82d9```

  2. Run the container, mapping port `80` to some random high-numbered port:

     ```$ docker run -d -p 1337:80 --name pwnwiki pwnwiki
     bf4cec957eb6a66142ae993d741213176c621f547a705d2f5747ded1619f4d21
     $ docker ps
     CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                           NAMES
     bf4cec957eb6        pwnwiki             "/bin/sh -c 'nginx -g"   3 seconds ago       Up 1 seconds        443/tcp, 0.0.0.0:1337->80/tcp   pwnwiki```

  3. Open a browser to the port you chose on `localhost` (or `127.0.0.1`). On a Mac, do:

     ```$ open http://127.0.0.1:1337/```

     ![pwnwiki from Docker container](images/docker-pwnwiki.png)

  4. You can stop the container with: `docker kill pwnwiki` or `docker stop pwnwiki`

  5. Restart the container with: `docker restart pwnwiki`

  6. Remove the container with: `docker rm pwnwiki`


- - - - - -
### Submitting Content
We want/need your help! Please contribute to this project is via GitHub (https://github.com/pwnwiki/pwnwiki.github.io). That allows us to get your project-ready content incorporated into the wiki fast. Check out the https://github.com/pwnwiki/pwnwiki.github.io/wiki page for details on how to contribute.

We realize that not everyone can/wants to submit content via GitHub and that's cool. If your go-to content is not up here and you don't want to spend the time becoming a Git Jedi, just visit our [Google Form](https://docs.google.com/forms/d/1N7-jRjnUXoz-UwB2h0du2IrskFJW6hBGs4YsTwvEncE/viewform). Due to the large amount of submissions and content, there may be a delay between your posting and us getting your content into the project. Thanks for your submissions and your patience! 

- - - - - -
### Curators:

  * [@mubix](https://twitter.com/mubix) [gimmick:TwitterFollow](@mubix)
  * [@WebBreacher](https://twitter.com/webbreacher) [gimmick:TwitterFollow](@WebBreacher)
  * [@tekwizz123](https://twitter.com/tekwizz123) [gimmick:TwitterFollow](@tekwizz123)
  * [@jakx_](https://twitter.com/jakx_) [gimmick:TwitterFollow](@jakx_)
  * [@TheColonial](https://twitter.com/TheColonial) [gimmick:TwitterFollow](@TheColonial)
  * [@Wireghoul](https://twitter.com/Wireghoul) [gimmick:TwitterFollow](@Wireghoul)
  
If you would like to become a curator, please contact [mubix@hak5.org](mailto:mubix@hak5.org)

[gimmick:ForkMeOnGitHub ({ color: 'red',  position: 'right' })](http://www.github.com/pwnwiki/pwnwiki.github.io/)
