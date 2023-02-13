---
title: "Docker Desktop"
teaching: 20
exercises: 0
questions:
- "What is Docker Desktop?"
- "What can it be used for?"
- "Why can't it replace the cli?"
objectives:
- "Show Docker Desktop and its components."
- "Understand what images and containers are."
- "Visualize the process of image aquisition, container execution and where it ends."
- "Understand the ephimeral nature of containers."
- "Have a glimpse at containers that allow interaction."
- "Understand the importance of cleaning up in docker."
- "Understand the limitations of Docker Desktop."
keypoints:
- "Docker Desktop is a great dashboard that allows us to understand and visualize the lifecycle of images and containers."
- "Images are snapshots of an environment, easily distributable and ready to be used as *templates* for containers."
- "Containers are executions of the images, often with configuration added on top, and usually meant for single use."
- "Running a container usually implies creating a new copy, so it is important to clean up regularly."
- "Docker Desktop could potentially be all you need to use if you only *consume* images out of the box."
- "However, it is very limited in most cases (even for *consumers*), and rarely allows the user to configure and interact with the containers adequately."
---

**This episode is meant to be instructional, that is, you do not *need* to follow along.**

We will present the Docker Desktop dashboard, as it will be useful to understand key concepts of docker, such as images and containers.
However, it is important to note that while it is mostly is free, some features are offered as premium.
Also, it is not fully functional on all operating systems; it can produce conflicts with the docker engine on Linux, for example.

## Getting images
Setting up docker in windows or mac will have installed Docker Desktop by default.
If you open the application you will likely see something like this:
# TO DO: Image 0!
You'll notice that the panel on the left has a tab for 'Images' and another for 'Containers'.
These will be the focus for the episode, and we will ignore most other features.

On the top you'll also find a search icon, which links to Docker Hub,
and allows us to search for the images we saw in the previous episode directly from here.

*Note that there are two tabs, one for containers and one for images.
Make sure that you select the right tab when you search!
# TO DO: Image 1!

You can search through the name only,
# TO DO: Image 2!

or include the owner. You can then select the tag from the dropdown menu.
# TO DO: Image 3!

Once you find the image you were looking for, you can either download it (pull), or directly run it.

We'll start by just downloading `hello-world:latest`.

The 'Images' tab on the left panel will show all the images in your system, so you will be able to see the one we downloaded here.
# TO DO: Image 4!

From this tab we can see some information about the images on disk, and run them, but we can also inspect the images.
Clicking on the image will open a window with information on how the image is built, and examine its packages and vulnerabilities.
# TO DO: Image 5!

The `hello-world` image does not seem too interesting from here.
If you go to DockerHub you'll find links to the github site, where you'll see it is not as simpleas it looks.
Nevertheless, this is a very nice and quick way to explore an image.
If we pull the `docker/getting-started` image and inspect it, for example, we can see that it detects some vulnerabilities:
# TO DO: Image 6!
You can even further inspect the vulnerable layers by looking at the command
# TO DO: Image 7!

This all looks rather scary, and it is important that we are careful with the images that we download.
It is therefore quite useful to be able to analize them like this.
This image, in particular, is from a verified publisher (Docker Inc. no less!), and has been downloaded over 10M times, so we'll be safe.

## Running containers
The images that we just downloaded are inmutable files, they are snapshots of an environment, distributed to be used as *templates* to create 'containers'.
The containers are, essentially, images being *run*.
They are executions of the image, and because they are running, they are no longer 'static'.

Let's run the `hello-world` image by either clicking the 'Run' button in the 'Actions' column, from the Images tab.
# TO DO: Image 8!

A prompt will ask you to confirm 'Run' or modify some optional settings.
# TO DO: Image 9!

The optional settings allow you to modify the container name, so that you can easily identify it afterwards.
Lets add an appropriate name and confirm with the 'Run' button.
# TO DO: Image 10!

You will likely be taken to a 'Logs' tab inside the container that you just ran.
The logs show the output of this particular image, 'Hello from Docker!' among other things.

If you look carefully, the 'Containers' tab on the left is highlighted.
We are looking at a container now, not an image, and so we were re-located.

Exploring the 'Inspect' tab will show us some information, but for now we are more interested in what the 'Terminal' and 'Stats' tabs have to say.
They both seem to indicate that we need to *run* or *start* the container.
# TO DO: Image 11! Can images 11-14 be in tabs?
# TO DO: Image 12!
# TO DO: Image 13!
# TO DO: Image 14!

Indeed, if we look carefully, we will find an 'Exited (0)' status under the container name, and a 'Start' button near the top-right corner.
However, if we click on that button we will see the output duplicated in the logs, and the 'Exited (0)' status again.
# TO DO: Image 15!

If we go back to the images tab and run the image again (let's not bother giving it a name this time), we'll see that the same thing hapens.
We get the 'Hello from Docker!', and the container exits.
# TO DO: Image 16!

The nature of most containers is *ephimeral*.
They are meant to execute a process, and when the process is completed, they exit.
We can confirm this by clicking on the 'Containers' tab on the left.
This will exit the container inspection and show us all the containers.
Both containers in the list have a status 'Exited'.
# TO DO: Image 17!

Some of you may be wondering why if we have only run the `hello-world` image, you can see there are two containers.
One of the containers we named, and the other has some gibberish as a name (Docker generated this randomly).
As mentioned before, the *image* is used as a template, and as many *containers* as we want can be created from it.
If we go back to the 'Images' tab and run `hello world` again, we'll see a new container appear.

## Interacting with containers

Not all containers are as short lived as the one we've been using.
If we run the `docker/getting-started` image that we had pulled earlier, we will see something different happen.
You can immediately notice the status under the container name is 'RUNNING' now.
The 'Logs' tab is not too informative, but the 'Inspect' tab already shows more information.
A process called 'NginX' is running.
The 'Terminal' and 'Stats' tabs changed the most.
Since the container is still running, the stats get shown, and we are able to launch a terminal *inside* the container.
# TO DO: Image 18! Can images 18-21 be in tabs?
# TO DO: Image 19!
# TO DO: Image 20!
# TO DO: Image 21!

Before trying to do anything in the terminal, let's look at the container list by clicking on the 'Containers' tab on the left.
You'll see the green icon of the container indicating that it is still live, and indication of how long it's been running for.
# TO DO: Image 22!

Clicking on the container name again will take us back to the 'Logs' tab in the container.
Lets try and interact with the terminal inside the container.
If you print the working directory with `pwd` you'll get the base directory: `\`.
You can also list the contents with `ls`, and the `docker-entrypoint` files are a dead giveaway that we are inside the container.
At this point this container is very much like a VM.
We can modify things, like for example making a directory with `mkdir`, and see it has been created with `ls` again.
# TO DO: Image 23!

But we can do more than that, we can install things. For example, you'll notice that `htop` is not installed.
Since the `getting-started` image is based on alpine, we can install it using `apk add htop`, and we can now use it.
# TO DO: Image 24! Can images 24-25 be in tabs?
# TO DO: Image 25!

The container does not need to stay alive forever, and you can see that there is a 'stop' icon on the top right.
If we stop the container, we get a familiar empty tab in 'Terminal' and 'Stats'.
The 'Containers' tab on the left will also show the container status as 'Exited'
# TO DO: Image 26! Can images 26-28 be in tabs?
# TO DO: Image 27!
# TO DO: Image 28!

Now lets say I want to run the `getting-started` image again. So I go to the 'Images' tab, and click run.
Now lets go to the 'Terminal' tab, and try and find our directory with `ls`. The directory is not there.
We'd also installed `htop`. so lets have a go at running it. Not there either.
# TO DO: Image 29!

If this is not surprising to you, it means you're getting the hang of it.
When we re-ran the *image*, we created a **new** *container*.
The new container is created from the template saved in the image, and so 'our' changes have banished.
This becomes very clear when we go back to the 'Containers' tab on the left.
We can see that the first container we created from the `getting-started` image is there, next to
the new container (which is still running, by the way).
# TO DO: Image 30!

## Reviving containers
We *can* get the old container running again, although this is rarely something we'd *want* to do.
In docker desktop, all we need to do is click on the 'Start' button from the 'Containers' list.
The terminal will appear empty, because it is a new session, but you will even be able to 'recall' commands.
# TO DO: Image 31! Can images 31-32 be in tabs?
# TO DO: Image 32!

## Cleaning up
The `hello-world` image was nice and useful to test docker was working, but it is now rather useless.
If I want to delete it, the 'Images' tab on the left has a convenient bin icon to do so.
Clicking on it will prompt you for confirmation, but it will fail.
# TO DO: Image 33! In GIF?
# TO DO: Image 34!
# TO DO: Image 35!

You'll probably notice that the status of the image is 'In use'.
That seems trange though, given that all the containers from that image excited immediately.

Lets have a look at the 'Containers' tab. It shows a list of 5 containers now.
Three of them came from the `hello-world` image, and are stopped.
Two of them came from the `getting-started` image, and are running.

We've only been using Docker for 15 minutes though! You may see how this can become a problem...
Particularly so because we were a bit sloppy and did not name the containers.
Let's try and get rid of the containers then.
We can conveniently select them all with the tickbox at the top, and an option to 'Delete' shows up.
Clicking on it will prompt for confirmation, and we can go ahead and accept.
# TO DO: Image 36! In GIF?
# TO DO: Image 37!
# TO DO: Image 38!
All our containers are now gone. Forever.

***Warning:*** You have to be careful here, this action deleted even the containers that were running.
You can filter the containers before you select them "all".

On the up-side, the 'Images' tab shows both the `hello-world` and the `getting-started` images as 'Unused' now.
For docker, an image is 'In use' as long as at least one container has been created from it.
We have just deleted all the containers created from either of these images.
This tells Docker that they are no longer being used, and can therefore be safely deleted.
# TO DO: Image 39! In GIF?
# TO DO: Image 40!
# TO DO: Image 41!
# TO DO: Image 42!

## Limitations - Why not Docker Desktop?

We have seen many of the neat and functional bits of Docker Desktop, and it can be mighty appealing,
particularly if you lean towards the use of graphical interfaces.
However, we've not touched on its weaknesses.
We'll just need to point at one to feel the need to throw everything overboard.

Let's go ahead and run the only image we have already pulled, `alpine`.
# TO DO: Image 43! Can images 43-47 be in tabs?
# TO DO: Image 44!
# TO DO: Image 45!
# TO DO: Image 46!
# TO DO: Image 47!
That was fast, and uneventful.
Not even a single output to the 'Logs'.
No way to open a terminal inside Alpine.

Just to be clear though, this Docker image does contain the whole Alpine OS.
In Docker Desktop, however, there is no way to interact with it.

Let's try something different.
There's a program called `cowsay` that lets you print messages as if a cow was saying them.
Searching for that image shows that there is one by `beatrixxx32` with a reasonable number of downloads.
# TO DO: Image 48!
So lets pull that image and run it.
# TO DO: Image 49! Can images 49-52 be in tabs?
# TO DO: Image 50!
# TO DO: Image 51!
# TO DO: Image 52!
# TO DO: Image 53!
We do get a cow this time, but it is not saying anything.
But it does not know *what* to say.
Going back to the cowsay image search, you may notice that in 'Usage' the command line asks for "your message".
We are not using a command though, we just clicked *run*.
Maybe we missed something in the optional settings!
# TO DO: Image 54!
No, it does not seem like it.
No matter what we do, we cannot make the cow say anything from here.

Are the alpine and cowsay images useless? No, definitely not.
However, they are expecting some sort of input or command, which we cannot provide from Docker Desktop.

This is the case for most images, and so Docker Desktop (as it is now) cannot really be used for much more than as a nice dashboard.





{% include links.md %}
