---
title: Setup
---
### Requirements
  * A Linux, Mac or Windows computer
  * More than 5 GB free hard drive space
  * If installing Docker yourself: **root / administrator access**

> ## Warning
> Docker uses root / administrator access for basic functionality. If installing Docker yourself, without root / administrator rights, it will not be possible to follow or complete this course. 
>
> If your computer has already been set up with Docker, then it may be possible to follow this course, please check locally.
{: .callout}

### Website accounts to create
Please seek help at the start of the lesson if you have not been able to establish a website account on:
- The [Docker Hub](http://hub.docker.com). We will use the Docker Hub to download pre-built container images, and for you to upload and download container images that you create, as explained in the relevant lesson episodes.

### Files to download

Download the [`docker-intro.zip`]({{ page.root }}/files/docker-intro.zip) file. _This file can alternatively be downloaded from the `files` directory in the [docker-introduction GitHub repository][docker-introduction repository]_.

Move the downloaded file to your Desktop and unzip it. It should unzip to a folder called `docker-intro`. 

### Software to install

Installing Docker on different platforms requires different procedures and generally requires root / administrator access for a successful installation. Please follow the pointers below for assistance in finding the correct installation procedures.

{::options parse_block_html="true" /}
<div>
<ul class="nav nav-tabs nav-justified" role="tablist">
<li role="presentation" class="active"><a data-os="windows" href="#windows" aria-controls="Windows"
role="tab" data-toggle="tab">Windows</a></li>
<li role="presentation"><a data-os="macos" href="#macos" aria-controls="macOS" role="tab"
data-toggle="tab">macOS</a></li>
<li role="presentation"><a data-os="linux" href="#linux" aria-controls="Linux" role="tab"
data-toggle="tab">Linux</a></li>
</ul>

<div class="tab-content">
<article role="tabpanel" class="tab-pane active" id="windows">

#### Microsoft Windows

**You must have admin rights to run Docker!** Some parts of the lesson will work without running as admin but if you are unable to `Run as administrator` on your machine some elements of this workshop might not work as described.

Ideally, you will be able to install the Docker Desktop software, following the [Docker website's documentation](https://docs.docker.com/docker-for-windows/install/). Note that the instructions for installing Docker Desktop on Windows 10 Home Edition are different from other versions of Windows 10.

Note that the above installation instructions highlight a minimum version or "build" that is required to be able to install Docker on your Windows 10 system. See [Which version of Windows operating system am I running?](https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808) for details of how to find out which version/build of Windows 10 you have.

If you are unable to follow the above instructions to install Docker Desktop on your Windows system, the final release of the deprecated Docker Toolbox version of Docker for Windows can be downloaded from the [releases page of the Docker Toolbox GitHub repository](https://github.com/docker/toolbox/releases). (Download the `.exe` file for the Windows installer). _Please note that this final release of Docker Toolbox includes an old version of Docker and you are strongly advised not to attempt to use this for any production use. It will, however, enable you to follow along with the lesson material._

> ## Warning: Git Bash
> If you are using Git Bash as your terminal on Windows then you should be aware that you may run
> into issues running some of the commands in this lesson as Git Bash will automatically re-write
> any paths you specify at the command line into Windows versions of the paths and this will confuse
> the Docker container you are trying to use. For example, if you enter the command:
> ```
> docker run alpine cat /etc/os-release
> ```
> Git Bash will change the `/etc/os-release` path to `C:\etc\os-release\` before passing the command
> to the Docker container and the container will report an error. If you want to use Git Bash then you
> can request that this path translation does not take place by adding an extra `/` to the start of the
> path. i.e. the command would become:
> ```
> docker run alpine cat //etc/os-release
> ```
> This should suppress the path translation functionality in Git Bash.
{: .callout}
</article>
<article role="tabpanel" class="tab-pane" id="macos">


Please install docker following these [instructions](https://docs.docker.com/desktop/install/mac-install/).

</article>

<article role="tabpanel" class="tab-pane" id="linux">

### Installation ###

[Install Docker Engine](https://docs.docker.com/engine/install/) provides an overview of supported Linux distributions and pointers to relevant installation information. 

Additionally, a generic installation option is provided using a [convenience script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script).
### Enable non-root access ###

To use Docker as a non-root user, some [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) must be taken.


> ## Warning: Extra action if you install Docker using Snap
> [Snap](https://snapcraft.io/) is an app management system for linux - which is popular on
> Ubuntu and other systems. Docker is available via Snap - if you have installed it using
> this service you will need to take the following steps, to ensure docker will work properly.
> ~~~
> mkdir ~/tmp
> export TMPDIR=~/tmp
> ~~~
> {: .language-bash}
> These commands will let you use docker in the current terminal instance, but you will have to run "export TEMPDIR=~/tmp" in every new terminal you want to use docker in.
> An alternative is to append that command at the end of your bashrc file with
> ~~~
> echo "export TEMPDIR=~/tmp" >> ~/bashrc
> ~~~
> this will configure each new instance of a terminal to run that command at the start of every new terminal instance.
{: .callout}

</article>
</div>
</div>

### Verify Installation

To quickly check if the Docker and client and server are working run the following command in a new terminal or ssh session:
~~~
$ docker version
~~~
{: .language-bash}
~~~
Client:
 Version:           20.10.2
 API version:       1.41
 Go version:        go1.13.8
 Git commit:        20.10.2-0ubuntu2
 Built:             Tue Mar  2 05:52:27 2021
 OS/Arch:           linux/arm64
 Context:           default
 Experimental:      true

Server:
 Engine:
  Version:          20.10.2
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.13.8
  Git commit:       20.10.2-0ubuntu2
  Built:            Tue Mar  2 05:45:16 2021
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.4.4-0ubuntu1
  GitCommit:        
 runc:
  Version:          1.0.0~rc95-0ubuntu1~21.04.1
  GitCommit:        
 docker-init:
  Version:          0.19.0
  GitCommit:        
~~~
{: .output}

The above output shows a successful installation and will vary based on your system.  The important part is that the "Client" and the "Server" parts are both working and returns information.  It is beyond the scope of this document to debug installation problems but common errors include the user not belonging to the `docker` group and forgetting to start a new terminal or ssh session.

### A quick tutorial on copy/pasting file contents from episodes of the lesson
Let's say you want to copy text off the lesson website and paste it into a file named `myfile` in the current working directory of a shell window. This can be achieved in many ways, depending on your computer's operating system, but routes I have found work for me:
- macOS and Linux: you are likely to have the `nano` editor installed, which provides you with a very straightforward way to create such a file, just run `nano myfile`, then paste text into the shell window, and press <kbd>control</kbd>+<kbd>x</kbd> to exit: you will be prompted whether you want to save changes to the file, and you can type <kbd>y</kbd> to say "yes".
- Microsoft Windows running `cmd.exe` shells:
  - `del myfile` to remove `myfile` if it already existed;
  - `copy con myfile` to mean what's typed in your shell window is copied into `myfile`;
  - paste the text you want within `myfile` into the shell window;
  - type <kbd>control</kbd>+<kbd>z</kbd> and then press <kbd>enter</kbd> to finish copying content into `myfile` and return to your shell;
  - you can run the command `type myfile` to check the content of that file, as a double-check.
- Microsoft Windows running PowerShell:
  - The `cmd.exe` method probably works, but another is to paste your file contents into a so-called "here-string" between `@'` and `'@` as in this example that follows (the ">" is the prompt indicator):

        > @'
        Some hypothetical
        file content that is

        split over many

        lines.
        '@ | Set-Content myfile -encoding ascii

{% include links.md %}

{% comment %}
<!--  LocalWords:  myfile kbd links.md md endcomment
-->
{% endcomment %}
