# 1. Operating System Requirements
- Operating system Used: `Ubuntu-18.04`, `Ubuntu 20.04(LTS) x64` and `CentOS-7.8`

# 2. Operating System Dependencies
Notes:
- This is for System level Dependencies and has to be done only once

## 2.1. For Ubuntu (20.04 LTS):
```bash
$ sudo apt-get install -y build-essential lsof gcc libbz2-dev libfreetype6-dev libncurses5-dev libreadline-dev libsqlite3-dev python3-dev unzip
```

System reboot is recommended after the successful above install

# 4. Clone and Checkout build

```bash
$ git clone ...
$ cd ...
$ git checkout -b <local-branch-name> origin/<remote-branch-name>  # this command can be ignored for ``develop`` branch
```

# 5. Setup The Build with Isolated Python
The below command pulls the python-3.7.12 source from the private package server and compiles in the basebuild directory, thus creates a Isolated python for the customized usage.
```bash
$ ./install_build.sh
```

The above command should output something simiar to

```
TODO
```

# 7. Run the Buildout
TODO


# 8. Developer Guide
TODO

# 10. Authors
- [Siva Cn](sivacn@protonmail.com)
