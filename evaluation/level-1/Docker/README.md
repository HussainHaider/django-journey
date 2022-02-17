### Question 1
Alpine: It is based on the Alpine Linux an OS hat was built specifically for use inside of containers.
Slim: It is the down version of full images. It only has limited and necessary libraries/packages. 
Stretch, Buster, Jessie, Bullseye: These are the codenames of different Debian releases. version 11 -> Bullseye | version 10 -> Buster | version 9 -> Stretch | version 8 -> Jessie.

Alpine image is to make the image size as small as possible.  The base image will be smaller than 5MB.
For slim images use it if have space constraints and do not need the full version.
For Stretch, Buster, Jessie, Bullseye choose one of these images if the code is compatible with a specific version of the Debian operating system.

### Question 2
CMD: It contains commands with parameters that can be changed/overridden from the Docker CLI when running a container.
ENTRYPOINT: Parameters that cannot be overridden when Docker Containers run with CLI parameters.

### Question 3
Run command mainly used to build images but here a new directory is created in a container.

### Question 4
Each line is a command in a Docker file which create a layer when these commands are executed.
RUN, COPY, ADD creates layer but other instructions create intermediate images. The first layer is the base image. All layers added up to make container image and when we run these container image to run as a container then on top of layers it create a writeable conatiner layer. All of layers contribute to the size of the image except the intermediate layer. To see the layers we use 'docker size [image name]' command.